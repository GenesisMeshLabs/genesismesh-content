from pathlib import Path
import argparse
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "videos" / "thumbnails"
LOGO = ROOT / "shared" / "images" / "brand" / "logo-reverse.png"
BRAND_BG = ROOT / "shared" / "images" / "brand" / "background.png"
MARKETING = ROOT / "shared" / "images" / "marketing"


THUMBNAILS = [
    ("why-genesismesh", "TRUST BREAKS\nAT THE BOUNDARY", MARKETING / "social-card.png"),
    ("portable-trust", "TRUST THAT\nTRAVELS", MARKETING / "marketing-hero-trust-fabric.png"),
    ("sovereign-systems", "WHO OWNS\nTHE TRUST?", MARKETING / "marketing-independent-operators.png"),
    ("recognition-and-revocation", "CUT OFF TRUST\nWITH PROOF", MARKETING / "marketing-provenance-chain.png"),
    ("auditable-trust-state", "EVERY DECISION\nLEAVES PROOF", MARKETING / "marketing-provenance-chain.png"),
    ("protocol-interoperability", "ONE TRUST LAYER.\nMANY RUNTIMES.", MARKETING / "marketing-protocol-interoperability.png"),
    ("trust-api-and-sdks", "VERIFY TRUST\nIN CODE", MARKETING / "marketing-protocol-interoperability.png"),
    ("use-cases-ai-agents", "AGENTS NEED\nPROOF", MARKETING / "marketing-agent-network.png"),
    ("use-cases-edge-infrastructure", "IDENTITY DRIFTS\nAT THE EDGE", BRAND_BG),
    ("use-cases-supply-chain-trust", "SIGNING IS\nNOT ENOUGH", MARKETING / "marketing-supply-chain-trust.png"),
    ("use-cases-enterprise-integration", "NO CENTRAL\nBROKER", MARKETING / "marketing-independent-operators.png"),
    ("use-cases-data-access-governance", "PERMISSIONS ARE\nNOT ENOUGH", MARKETING / "marketing-provenance-chain.png"),
]


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    candidates = []
    if os.environ.get("WINDIR"):
        windows_fonts = Path(os.environ["WINDIR"]) / "Fonts"
        candidates.extend([
            windows_fonts / ("arialbd.ttf" if bold else "arial.ttf"),
            windows_fonts / ("segoeuib.ttf" if bold else "segoeui.ttf"),
        ])
    candidates.extend([
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"),
    ])
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def cover_image(path: Path, size=(1280, 720)) -> Image.Image:
    image = Image.open(path).convert("RGB")
    image_ratio = image.width / image.height
    target_ratio = size[0] / size[1]
    if image_ratio > target_ratio:
        height = image.height
        width = int(height * target_ratio)
        left = (image.width - width) // 2
        image = image.crop((left, 0, left + width, height))
    else:
        width = image.width
        height = int(width / target_ratio)
        top = (image.height - height) // 2
        image = image.crop((0, top, width, top + height))
    return image.resize(size, Image.Resampling.LANCZOS)


def draw_text_with_shadow(draw: ImageDraw.ImageDraw, xy, text, font_obj, fill):
    x, y = xy
    for offset in [(5, 5), (3, 3)]:
        draw.multiline_text((x + offset[0], y + offset[1]), text, font=font_obj, fill=(0, 0, 0), spacing=8)
    draw.multiline_text((x, y), text, font=font_obj, fill=fill, spacing=8)


def make_thumbnail(slug: str, text: str, background: Path) -> None:
    base = cover_image(background).filter(ImageFilter.GaussianBlur(radius=4.2))
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    draw.rectangle((0, 0, 1280, 720), fill=(0, 0, 0, 150))
    draw.rectangle((0, 0, 820, 720), fill=(7, 8, 7, 238))
    draw.polygon([(820, 0), (1010, 0), (820, 720), (650, 720)], fill=(7, 8, 7, 170))
    draw.line((820, 0, 650, 720), fill=(217, 255, 97, 180), width=5)
    draw.rectangle((0, 650, 1280, 720), fill=(217, 255, 97, 235))

    logo = Image.open(LOGO).convert("RGBA").resize((104, 104), Image.Resampling.LANCZOS)
    overlay.alpha_composite(logo, (52, 42))

    label_font = font(34)
    small_font = font(26)
    title_font = font(92 if max(len(line) for line in text.splitlines()) < 16 else 76)

    draw.text((174, 66), "GENESIS MESH", font=label_font, fill=(255, 255, 255))
    draw.rectangle((62, 176, 194, 188), fill=(217, 255, 97))
    draw_text_with_shadow(draw, (62, 225), text, title_font, (255, 255, 255))
    draw.text((62, 668), "PORTABLE TRUST FOR SOVEREIGN SYSTEMS", font=small_font, fill=(7, 8, 7))

    image = Image.alpha_composite(base.convert("RGBA"), overlay)
    OUT.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(OUT / f"{slug}.png", quality=95)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Genesis Mesh campaign thumbnails.")
    parser.add_argument("--slug", help="Generate one thumbnail slug instead of the built-in campaign set")
    parser.add_argument("--text", help="Thumbnail hook text. Use \\n for a line break.")
    parser.add_argument("--background", help="Background image path for --slug, relative to repo root or absolute")
    args = parser.parse_args()

    if args.slug:
        if not args.text or not args.background:
            raise SystemExit("--slug requires --text and --background")
        background = Path(args.background)
        if not background.is_absolute():
            background = ROOT / background
        make_thumbnail(args.slug, args.text.replace("\\n", "\n"), background)
        return

    for slug, text, background in THUMBNAILS:
        make_thumbnail(slug, text, background)


if __name__ == "__main__":
    main()
