from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CAMPAIGNS = ROOT / "campaigns"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def next_number(parent: Path) -> int:
    numbers: list[int] = []
    for child in parent.iterdir() if parent.exists() else []:
        if not child.is_dir():
            continue
        match = re.match(r"^(\d+)-", child.name)
        if match:
            numbers.append(int(match.group(1)))
    return (max(numbers) + 1) if numbers else 1


def safe_slug(stable_slug: str) -> str:
    return stable_slug.replace("/", "-")


def rel_prefix(kind: str) -> str:
    return "../../../" if kind == "use-case" else "../../"


def default_images(prefix: str) -> list[str]:
    return [
        f"{prefix}shared/images/marketing/marketing-hero-trust-fabric.png",
        f"{prefix}shared/images/marketing/marketing-independent-operators.png",
        f"{prefix}shared/images/marketing/marketing-provenance-chain.png",
    ]


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a Genesis Mesh campaign folder.")
    parser.add_argument("--type", choices=["horizontal", "use-case"], required=True)
    parser.add_argument("--slug", required=True, help="URL/file slug without numeric prefix")
    parser.add_argument("--title", required=True)
    parser.add_argument("--status", default="draft")
    args = parser.parse_args()

    base_slug = slugify(args.slug)
    parent = CAMPAIGNS / "08-use-cases" if args.type == "use-case" else CAMPAIGNS
    number = next_number(parent)
    folder = parent / f"{number:02d}-{base_slug}"
    folder.mkdir(parents=True, exist_ok=False)
    (folder / "audio").mkdir()
    (folder / "audio" / ".gitkeep").write_text("", encoding="utf-8")

    stable_slug = f"use-cases/{base_slug}" if args.type == "use-case" else base_slug
    file_slug = safe_slug(stable_slug)
    prefix = rel_prefix(args.type)
    campaign = {
        "slug": stable_slug,
        "title": args.title,
        "status": args.status,
        "audience": ["builders", "security", "enterprise"],
        "channels": ["website", "linkedin", "video", "article"],
        "primary_message": "",
        "call_to_action": "",
        "source_docs": [
            "genesismesh/VISION.md",
            "genesismesh/docs/development/strategy.md",
        ],
        "slogan": "Genesis Mesh: portable trust for sovereign systems.",
        "voice": "",
        "voice_role": "",
        "duration_seconds_per_image": 5,
        "images": default_images(prefix),
        "thumbnail": f"{prefix}videos/thumbnails/{file_slug}.png",
        "output": f"{prefix}videos/renders/{file_slug}-revid-stock.mp4",
        "publishing": {
            "youtube": {
                "video_id": "",
                "url": "",
                "title": "",
                "thumbnail": f"{prefix}videos/thumbnails/{file_slug}.png",
                "thumbnail_text": "",
                "render": f"{prefix}videos/renders/{file_slug}-revid-stock.mp4",
            },
            "patreon": {
                "url": "",
                "title": args.title,
            },
        },
    }

    (folder / "campaign.json").write_text(
        json.dumps(campaign, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_if_missing(folder / "article.md", f"# {args.title}\n\n")
    write_if_missing(folder / "voiceover.md", f"# {args.title}\n\n")
    write_if_missing(
        folder / "voiceover.ssml",
        '<speak version="1.0" xml:lang="en-US">\n'
        '  <voice name="">\n'
        "  </voice>\n"
        "</speak>\n",
    )
    write_if_missing(folder / "youtube.md", f"# YouTube Metadata - {args.title}\n\n")
    write_if_missing(folder / "patreon.md", f"# {args.title}\n\n[YouTube video link]\n")

    print(folder.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
