"""Generate a simple campaign video from images and optional narration.

Requires ffmpeg on PATH.

Usage:
    python videos/scripts/generate_video.py portable-trust
    python videos/scripts/generate_video.py use-cases/ai-agents
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGNS = ROOT / "campaigns"


def campaign_dir(slug: str) -> Path:
    path = CAMPAIGNS / slug
    if path.exists():
        return path
    matches = []
    for candidate in CAMPAIGNS.rglob("campaign.json"):
        try:
            campaign = json.loads(candidate.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if candidate.parent.name == slug or campaign.get("slug") == slug:
            matches.append(candidate.parent)
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        choices = "\n".join(str(match.relative_to(CAMPAIGNS)).replace("\\", "/") for match in matches)
        raise SystemExit(f"Campaign slug is ambiguous. Use one of:\n{choices}")
    raise SystemExit(f"Campaign not found: {path}")


def resolve_campaign_path(campaign_path: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (campaign_path / path).resolve()


def run(cmd: list[str]) -> None:
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


def probe_duration_seconds(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign", help="Campaign slug under campaigns/")
    parser.add_argument("--no-audio", action="store_true", help="Render without narration")
    parser.add_argument("--out", help="Optional output mp4 path")
    args = parser.parse_args()

    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg is required. Install it and make sure ffmpeg is on PATH.")

    campaign_path = campaign_dir(args.campaign)
    campaign_file = campaign_path / "campaign.json"
    if not campaign_file.exists():
        raise SystemExit(f"Missing campaign.json: {campaign_file}")

    campaign = json.loads(campaign_file.read_text(encoding="utf-8"))
    duration = float(campaign.get("duration_seconds_per_image", 5))
    images = [resolve_campaign_path(campaign_path, item) for item in campaign.get("images", [])]
    missing = [str(path) for path in images if not path.exists()]
    if missing:
        raise SystemExit("Missing image(s):\n" + "\n".join(missing))
    if not images:
        raise SystemExit("No images configured in campaign.json")

    output = Path(args.out) if args.out else resolve_campaign_path(campaign_path, campaign.get("output", f"../../videos/renders/{campaign_path.name}.mp4"))
    output.parent.mkdir(parents=True, exist_ok=True)

    audio = campaign_path / "audio" / "narration.wav"
    if args.no_audio:
        use_audio = False
    elif audio.exists():
        use_audio = True
    else:
        rel = str(campaign_path.relative_to(CAMPAIGNS)).replace("\\", "/")
        raise SystemExit(
            "No narration found. Generate audio first:\n"
            f"  python .\\videos\\scripts\\generate_tts.py {rel}\n"
            "Or render a deliberate silent draft with --no-audio."
        )
    if use_audio:
        duration = max(duration, (probe_duration_seconds(audio) + 0.5) / len(images))

    with tempfile.TemporaryDirectory(prefix="gm-video-") as tmp:
        tmp_path = Path(tmp)
        list_file = tmp_path / "slides.txt"
        lines: list[str] = []
        for image in images:
            normalized = str(image).replace("\\", "/")
            lines.append(f"file '{normalized}'")
            lines.append(f"duration {duration}")
        lines.append(f"file '{str(images[-1]).replace(chr(92), '/')}'")
        list_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

        silent = tmp_path / "silent.mp4"
        run([
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_file),
            "-vf",
            "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
            "-r",
            "30",
            str(silent),
        ])

        if use_audio:
            run([
                "ffmpeg",
                "-y",
                "-i",
                str(silent),
                "-i",
                str(audio),
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-shortest",
                str(output),
            ])
        else:
            shutil.copy2(silent, output)

    print(f"Video rendered: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
