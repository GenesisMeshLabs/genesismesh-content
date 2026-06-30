"""Create campaign videos through the Revid API.

Usage:
    python videos/scripts/generate_revid_video.py payload portable-trust
    python videos/scripts/generate_revid_video.py render portable-trust
    python videos/scripts/generate_revid_video.py status <revid-job-id>
    python videos/scripts/generate_revid_video.py poll <revid-job-id>

Required env values can be set in videos/scripts/.env:
    REVID_API_KEY

Optional env values:
    REVID_API_BASE=https://www.revid.ai/api/public/v3
    REVID_VOICE_ID=<voice-id>
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGNS = ROOT / "campaigns"
ENV_FILE = Path(__file__).resolve().parent / ".env"
JOBS_DIR = ROOT / "videos" / "revid-jobs"
DEFAULT_API_BASE = "https://www.revid.ai/api/public/v3"
USER_AGENT = "GenesisMeshContent/1.0 (+https://github.com/GenesisMeshLabs/genesismesh-content)"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def campaign_dir(slug: str) -> Path:
    path = CAMPAIGNS / slug
    if path.exists():
        return path
    matches: list[Path] = []
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


def read_campaign(path: Path) -> dict:
    campaign_file = path / "campaign.json"
    if not campaign_file.exists():
        raise SystemExit(f"Missing campaign.json: {campaign_file}")
    return json.loads(campaign_file.read_text(encoding="utf-8"))


def read_text_source(campaign_path: Path, source: str) -> tuple[str, Path]:
    candidates = {
        "voiceover": campaign_path / "voiceover.md",
        "article": campaign_path / "article.md",
    }
    if source == "auto":
        ordered = [campaign_path / "voiceover.md", campaign_path / "article.md"]
    elif source in candidates:
        ordered = [candidates[source]]
    else:
        ordered = [Path(source)]

    for candidate in ordered:
        if candidate.exists():
            text = candidate.read_text(encoding="utf-8").strip()
            if text:
                return text, candidate
            raise SystemExit(f"Text source is empty: {candidate}")
    raise SystemExit("No text source found. Expected voiceover.md or article.md.")


def api_base() -> str:
    return os.environ.get("REVID_API_BASE", DEFAULT_API_BASE).rstrip("/")


def api_key() -> str:
    key = os.environ.get("REVID_API_KEY")
    if not key:
        raise SystemExit("Set REVID_API_KEY in videos/scripts/.env")
    return key


def request_json(method: str, path: str, payload: dict | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{api_base()}{path}",
        data=body,
        method=method,
        headers={
            "key": api_key(),
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Revid API error {exc.code}: {detail}") from exc
    if not raw.strip():
        return {}
    return json.loads(raw)


def estimate_json(payload: dict) -> dict:
    req = urllib.request.Request(
        f"{api_base()}/calculate-credits",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Revid estimate error {exc.code}: {detail}") from exc
    return json.loads(raw) if raw.strip() else {}


def build_payload(args: argparse.Namespace) -> dict:
    path = campaign_dir(args.campaign)
    campaign = read_campaign(path)
    script, source_path = read_text_source(path, args.source)

    payload: dict = {
        "workflow": "script-to-video",
        "source": {
            "text": script,
        },
        "media": {
            "type": args.media_type,
            "quality": args.quality,
            "density": args.density,
            "animation": args.animation,
        },
        "voice": {
            "enabled": args.revid_voice,
        },
        "captions": {
            "enabled": not args.no_subtitles,
            "preset": args.caption_preset,
            "position": args.caption_position,
        },
        "music": {} if args.music else None,
        "render": {
            "resolution": args.resolution,
            "compression": args.compression,
            "frameRate": args.frame_rate,
        },
        "options": {
            "disableVoice": not args.revid_voice,
            "disableAudio": not args.music,
            "preventSummarization": True,
            "outputCount": 1,
        },
        "aspectRatio": args.ratio,
        "metadata": {
            "campaign": campaign.get("slug", args.campaign),
            "title": campaign.get("title", campaign.get("slug", args.campaign)),
            "source": str(source_path.relative_to(ROOT)).replace("\\", "/"),
            "generator": "genesismesh-content/videos/scripts/generate_revid_video.py",
            "tts": "azure-by-default",
        },
    }
    if not args.music:
        payload.pop("music")
    voice_id = args.voice_id or campaign.get("revid_voice_id") or os.environ.get("REVID_VOICE_ID")
    if voice_id:
        payload["voice"]["voiceId"] = voice_id
    if args.revid_voice and not voice_id:
        print("Warning: --revid-voice is set but no voice ID was provided; Revid may use its default voice.", file=sys.stderr)
    if args.extra:
        payload.update(json.loads(args.extra))
    return payload


def find_job_id(response: dict) -> str | None:
    for key in ("id", "jobId", "job_id", "renderId", "render_id", "videoId", "video_id"):
        value = response.get(key)
        if isinstance(value, str) and value:
            return value
    data = response.get("data")
    if isinstance(data, dict):
        return find_job_id(data)
    return None


def find_video_url(response: dict) -> str | None:
    for key in ("videoUrl", "video_url", "url", "downloadUrl", "download_url"):
        value = response.get(key)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            return value
    data = response.get("data")
    if isinstance(data, dict):
        return find_video_url(data)
    return None


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def download(url: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as response:
        out.write_bytes(response.read())


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("campaign", help="Campaign slug from campaign.json")
    common.add_argument("--source", default="auto", help="auto, voiceover, article, or a file path")
    common.add_argument("--media-type", default="stock-video", help="stock-video, moving-image, ai-video, motion-graphics, or custom")
    common.add_argument("--quality", default="standard", help="standard, pro, or ultra")
    common.add_argument("--density", default="medium", help="low, medium, or high")
    common.add_argument("--animation", default="soft", help="none, soft, dynamic, or depth; applies to moving-image")
    common.add_argument("--ratio", default="16:9", help="9:16, 16:9, 1:1, 4:5, or auto")
    common.add_argument("--caption-preset", default="Wrap 1", help="Revid caption/subtitle preset")
    common.add_argument("--caption-position", default="bottom", help="Caption position")
    common.add_argument("--voice-id", help="Revid voice ID override")
    common.add_argument("--revid-voice", action="store_true", help="Use Revid voice generation instead of Azure/local TTS")
    common.add_argument("--no-subtitles", action="store_true")
    common.add_argument("--music", action="store_true", help="Enable Revid background music. Disabled by default to control credits.")
    common.add_argument("--resolution", default="1080p", help="720p, 1080p, or 4k")
    common.add_argument("--compression", type=float, default=18)
    common.add_argument("--frame-rate", type=float, default=30)
    common.add_argument("--extra", help="JSON object merged into the Revid payload")

    sub.add_parser("payload", parents=[common], help="Print the Revid request payload without calling the API")
    sub.add_parser("estimate", parents=[common], help="Estimate Revid credit cost without starting a render")
    render = sub.add_parser("render", parents=[common], help="Start a Revid render job")
    render.add_argument("--yes", action="store_true", help="Confirm credit spend and start the Revid render")

    status = sub.add_parser("status", help="Fetch Revid job status")
    status.add_argument("job_id")

    poll = sub.add_parser("poll", help="Poll Revid job status until completion or timeout")
    poll.add_argument("job_id")
    poll.add_argument("--interval", type=int, default=15)
    poll.add_argument("--timeout", type=int, default=1800)
    poll.add_argument("--out", help="Optional mp4 output path when a video URL is returned")

    args = parser.parse_args()
    load_env(ENV_FILE)

    if args.command == "payload":
        print(json.dumps(build_payload(args), indent=2, ensure_ascii=False))
        return 0

    if args.command == "estimate":
        response = estimate_json(build_payload(args))
        print(json.dumps(response, indent=2, ensure_ascii=False))
        return 0

    if args.command == "render":
        if not args.yes:
            raise SystemExit(
                "Refusing to start a Revid render without --yes.\n"
                "Run estimate first, then render with --yes when you accept the credit spend."
            )
        payload = build_payload(args)
        response = request_json("POST", "/render", payload)
        job_id = find_job_id(response)
        if job_id:
            save_json(JOBS_DIR / f"{job_id}.json", {"request": payload, "response": response})
            print(f"Revid render started: {job_id}")
            print(f"Job file: {JOBS_DIR / f'{job_id}.json'}")
        else:
            print("Revid render response did not include a recognized job id.", file=sys.stderr)
        print(json.dumps(response, indent=2, ensure_ascii=False))
        return 0

    if args.command == "status":
        response = request_json("GET", f"/status?pid={args.job_id}")
        save_json(JOBS_DIR / f"{args.job_id}.status.json", response)
        print(json.dumps(response, indent=2, ensure_ascii=False))
        return 0

    if args.command == "poll":
        deadline = time.time() + args.timeout
        while time.time() < deadline:
            response = request_json("GET", f"/status?pid={args.job_id}")
            save_json(JOBS_DIR / f"{args.job_id}.status.json", response)
            status_value = str(response.get("status") or response.get("state") or "").lower()
            print(f"{args.job_id}: {status_value or 'unknown'}")
            url = find_video_url(response)
            if url and status_value in {"ready", "completed", "complete", "done", "success", "succeeded"}:
                out = Path(args.out) if args.out else ROOT / "videos" / "renders" / f"revid-{args.job_id}.mp4"
                download(url, out)
                print(f"Downloaded: {out}")
                return 0
            if status_value in {"failed", "error", "canceled", "cancelled"}:
                print(json.dumps(response, indent=2, ensure_ascii=False), file=sys.stderr)
                return 1
            time.sleep(args.interval)
        raise SystemExit(f"Timed out waiting for Revid job: {args.job_id}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
