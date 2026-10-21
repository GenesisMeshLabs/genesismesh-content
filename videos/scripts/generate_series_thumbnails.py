"""Generate thumbnails for the campaigns from 10 onward.

Each thumbnail is written to the campaign folder as thumbnail.png. It serves
both the Patreon post and the YouTube video. Every group has its own accent
colour and a drawn motif, so the series is recognisable as a set and each
group stands apart.

    python videos/scripts/generate_series_thumbnails.py            # all
    python videos/scripts/generate_series_thumbnails.py 13-governed # folders matching
"""
from pathlib import Path
import math
import random
import sys

from PIL import Image, ImageDraw, ImageFilter

from generate_thumbnails import font, cover_image

ROOT = Path(__file__).resolve().parents[2]
CAMPAIGNS = ROOT / "campaigns"
LOGO = ROOT / "shared" / "images" / "brand" / "logo-reverse.png"
BRAND_BG = ROOT / "shared" / "images" / "brand" / "background.png"
MARKETING = ROOT / "shared" / "images" / "marketing"

W, H = 1280, 720
INK = (7, 8, 7)
WHITE = (255, 255, 255)
LIME = (217, 255, 97)

# group key -> (series label, accent colour, background)
GROUPS = {
    "origins": ("ORIGINS", LIME, MARKETING / "marketing-agent-network.png"),
    "opener": ("SINCE THE FIRST CAMPAIGNS", LIME, MARKETING / "marketing-hero-trust-fabric.png"),
    "policy": ("POLICY AND EVIDENCE", (97, 218, 255), MARKETING / "marketing-provenance-chain.png"),
    "governed": ("GOVERNED CHANGES", (255, 190, 80), BRAND_BG),
    "edge": ("TRUST AT THE EDGE", (255, 128, 102), BRAND_BG),
    "running": ("RUNNING IT FOR REAL", (178, 150, 255), MARKETING / "marketing-independent-operators.png"),
    "proof": ("PROOF, NOT PROMISES", LIME, MARKETING / "marketing-protocol-interoperability.png"),
}

# campaign folder (relative to campaigns/) -> (group, part label, hook text)
SPECS = {
    "10-genesis-mesh-did-not-start-with-genesis-mesh": ("origins", "", "BEFORE IT\nHAD A NAME", "network"),
    "11-after-the-signature": ("opener", "", "AFTER THE\nSIGNATURE", "signature"),
    "12-policy-and-evidence/01-policy-you-can-read": ("policy", "1/2", "POLICY YOU\nCAN READ", "documents"),
    "12-policy-and-evidence/02-allowed-is-not-done": ("policy", "2/2", "ALLOWED IS\nNOT DONE", "links"),
    "13-running-it-for-real/01-a-front-door-not-an-authority": ("running", "1/5", "A FRONT DOOR,\nNOT AN\nAUTHORITY", "door"),
    "13-running-it-for-real/02-watch-trust-cross-a-boundary": ("running", "2/5", "WATCH TRUST\nCROSS A\nBOUNDARY", "two_nodes"),
    "13-running-it-for-real/03-staying-up-without-giving-up-the-keys": ("running", "3/5", "STAY UP.\nKEEP THE\nKEYS.", "servers"),
    "13-running-it-for-real/04-a-contract-that-holds": ("running", "4/5", "A CONTRACT\nTHAT HOLDS", "documents"),
    "13-running-it-for-real/05-verify-what-you-run": ("running", "5/5", "VERIFY WHAT\nYOU RUN", "sealed_box"),
    "14-governed-changes/01-lost-misread-or-erased": ("governed", "1/5", "LOST,\nMISREAD OR\nERASED", "chain"),
    "14-governed-changes/02-changes-that-happen-anyway": ("governed", "2/5", "CHANGES THAT\nHAPPEN\nANYWAY", "eye"),
    "14-governed-changes/03-rotate-forward-never-back": ("governed", "3/5", "ROTATE\nFORWARD,\nNEVER BACK", "rotate"),
    "14-governed-changes/04-an-audit-that-doesnt-trust-the-audited": ("governed", "4/5", "AN AUDIT\nTHAT DOESN'T\nTRUST YOU", "magnifier"),
    "14-governed-changes/05-new-key-same-past": ("governed", "5/5", "NEW KEY,\nSAME PAST", "key"),
    "15-trust-at-the-edge/01-permission-before-the-link-goes-down": ("edge", "1/2", "PERMISSION\nBEFORE THE\nLINK DROPS", "edge"),
    "15-trust-at-the-edge/02-the-device-asks-first": ("edge", "2/2", "THE DEVICE\nASKS FIRST", "chip"),
    "16-proof-not-promises/01-five-languages-one-verdict": ("proof", "1/4", "FIVE\nLANGUAGES.\nONE VERDICT.", "converge"),
    "16-proof-not-promises/02-what-a-proof-proves": ("proof", "2/4", "WHAT A PROOF\nPROVES", "lemma"),
    "16-proof-not-promises/03-finding-our-own-flaws-first": ("proof", "3/4", "FINDING OUR\nOWN FLAWS\nFIRST", "bug"),
    "16-proof-not-promises/04-the-rules-cant-live-in-one-head": ("proof", "4/4", "THE RULES\nCAN'T LIVE IN\nONE HEAD", "bricks"),
}


def _motif_area():
    return (790, 90, 1230, 620)


def motif_network(draw, accent, seed):
    rng = random.Random(seed)
    x0, y0, x1, y1 = _motif_area()
    pts = [(rng.randint(x0, x1), rng.randint(y0, y1)) for _ in range(14)]
    for i, a in enumerate(pts):
        near = sorted(pts, key=lambda b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)[1:3]
        for b in near:
            draw.line((a, b), fill=accent + (150,), width=3)
    for p in pts:
        r = rng.choice((9, 12, 16))
        draw.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=INK + (255,), outline=accent + (255,), width=4)


def motif_documents(draw, accent, seed):
    rng = random.Random(seed)
    for i in range(3):
        x, y = 830 + i * 46, 150 + i * 70
        draw.rounded_rectangle((x, y, x + 280, y + 340), 18, fill=(16, 20, 22, 245), outline=accent + (255,), width=4)
        for j in range(5):
            ly = y + 50 + j * 46
            draw.rounded_rectangle((x + 30, ly, x + 30 + rng.randint(120, 220), ly + 14), 7, fill=accent + (120 if i < 2 else 220,))
    # seal on the front document
    cx, cy = 1150, 520
    draw.ellipse((cx - 52, cy - 52, cx + 52, cy + 52), fill=accent + (255,))
    draw.line((cx - 24, cy + 2, cx - 6, cy + 22, cx + 28, cy - 20), fill=INK + (255,), width=10, joint="curve")


def motif_chain(draw, accent, seed, anchor=True):
    # blocks linked in a chain, optionally anchored
    xs = [830, 930, 1030, 1130]
    base = 220 if anchor else 300
    for i, x in enumerate(xs):
        y = base + (i % 2) * 40
        draw.rounded_rectangle((x, y, x + 80, y + 80), 14, fill=(20, 18, 12, 245), outline=accent + (255,), width=5)
        draw.text((x + 24, y + 18), "#", font=font(40), fill=accent + (255,))
        if i:
            px = xs[i - 1] + 80
            py = base + 40 + ((i - 1) % 2) * 40
            draw.line((px, py, x, y + 40), fill=accent + (200,), width=5)
    if not anchor:
        return
    # anchor below the last block
    cx, top = 1170, 400
    draw.line((cx, top, cx, top + 170), fill=WHITE + (255,), width=10)
    draw.ellipse((cx - 20, top - 20, cx + 20, top + 20), outline=WHITE + (255,), width=9)
    draw.line((cx - 50, top + 60, cx + 50, top + 60), fill=WHITE + (255,), width=10)
    draw.arc((cx - 85, top + 70, cx + 85, top + 200), 20, 160, fill=WHITE + (255,), width=10)


def motif_edge(draw, accent, seed):
    # authority on top, devices below, one link cut
    ax, ay = 1010, 170
    draw.ellipse((ax - 60, ay - 60, ax + 60, ay + 60), fill=(22, 14, 12, 245), outline=accent + (255,), width=6)
    draw.text((ax - 34, ay - 26), "NA", font=font(44), fill=WHITE + (255,))
    devices = [(850, 500), (1010, 540), (1170, 500)]
    for i, (dx, dy) in enumerate(devices):
        if i == 2:
            # broken link: dashes with a gap
            for t in range(0, 10):
                if 4 <= t <= 5:
                    continue
                a = (ax + (dx - ax) * t / 10, ay + 60 + (dy - 40 - ay - 60) * t / 10)
                b = (ax + (dx - ax) * (t + 0.6) / 10, ay + 60 + (dy - 40 - ay - 60) * (t + 0.6) / 10)
                draw.line((a, b), fill=accent + (230,), width=6)
        else:
            draw.line((ax, ay + 60, dx, dy - 40), fill=accent + (200,), width=6)
        draw.rounded_rectangle((dx - 52, dy - 40, dx + 52, dy + 40), 12, fill=(22, 14, 12, 245), outline=WHITE + (255,), width=5)
        draw.ellipse((dx - 9, dy - 9, dx + 9, dy + 9), fill=accent + (255,))


def motif_door(draw, accent, seed):
    # a gateway: frame with a door and a key-less lock, requests flowing in
    x0, y0, x1, y1 = 900, 150, 1160, 590
    draw.rounded_rectangle((x0, y0, x1, y1), 24, fill=(18, 14, 28, 245), outline=accent + (255,), width=7)
    draw.rounded_rectangle((x0 + 50, y0 + 70, x1 - 50, y1), 16, outline=WHITE + (255,), width=6)
    draw.ellipse((x1 - 92, 380, x1 - 68, 404), fill=accent + (255,))
    for i, y in enumerate((260, 340, 420)):
        draw.line((800, y, x0 - 20, y), fill=accent + (160 + i * 30,), width=6)
        draw.polygon([(x0 - 20, y - 14), (x0 - 20, y + 14), (x0 + 2, y)], fill=accent + (255,))


def motif_converge(draw, accent, seed):
    # several implementations converging on one verdict
    cx, cy = 1150, 370
    srcs = [(840, 160), (820, 280), (815, 400), (825, 520), (850, 620)]
    for sx, sy in srcs:
        draw.line((sx, sy, cx, cy), fill=accent + (150,), width=5)
        draw.ellipse((sx - 26, sy - 26, sx + 26, sy + 26), fill=INK + (255,), outline=WHITE + (255,), width=5)
    draw.ellipse((cx - 70, cy - 70, cx + 70, cy + 70), fill=accent + (255,))
    draw.line((cx - 32, cy + 2, cx - 8, cy + 30, cx + 38, cy - 28), fill=INK + (255,), width=13, joint="curve")


PANEL = (20, 20, 24, 245)


def motif_eye(draw, accent, seed):
    cx, cy = 1010, 360
    draw.ellipse((cx - 190, cy - 110, cx + 190, cy + 110), outline=WHITE + (255,), width=8)
    draw.ellipse((cx - 70, cy - 70, cx + 70, cy + 70), fill=accent + (255,))
    draw.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), fill=INK + (255,))
    draw.rounded_rectangle((850, 520, 1170, 560), 10, fill=PANEL, outline=accent + (200,), width=3)


def motif_rotate(draw, accent, seed):
    cx, cy, r = 1010, 360, 170
    draw.arc((cx - r, cy - r, cx + r, cy + r), 200, 340, fill=accent + (255,), width=16)
    draw.arc((cx - r, cy - r, cx + r, cy + r), 20, 160, fill=WHITE + (255,), width=16)
    # arrow heads
    draw.polygon([(cx + 150, cy - 105), (cx + 190, cy - 40), (cx + 115, cy - 45)], fill=accent + (255,))
    draw.polygon([(cx - 150, cy + 105), (cx - 190, cy + 40), (cx - 115, cy + 45)], fill=WHITE + (255,))
    draw.rounded_rectangle((cx - 60, cy - 40, cx + 60, cy + 40), 12, fill=PANEL, outline=accent + (255,), width=5)
    draw.text((cx - 30, cy - 26), "v2", font=font(40), fill=WHITE + (255,))


def motif_magnifier(draw, accent, seed):
    motif_documents(draw, accent, seed)
    cx, cy, r = 980, 330, 105
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(0, 0, 0, 120), outline=WHITE + (255,), width=12)
    draw.line((cx + 75, cy + 75, cx + 170, cy + 170), fill=WHITE + (255,), width=22)


def motif_key(draw, accent, seed):
    # an old key fading, a new key bright
    for dx, alpha, colour in ((-60, 90, WHITE), (60, 255, accent)):
        cx, cy = 900 + dx + 60, 300 + (dx > 0) * 140
        draw.ellipse((cx - 60, cy - 60, cx + 60, cy + 60), outline=colour + (alpha,), width=14)
        draw.line((cx + 60, cy, cx + 280, cy), fill=colour + (alpha,), width=16)
        draw.line((cx + 220, cy, cx + 220, cy + 50), fill=colour + (alpha,), width=16)
        draw.line((cx + 260, cy, cx + 260, cy + 40), fill=colour + (alpha,), width=16)


def motif_servers(draw, accent, seed):
    for i in range(3):
        y = 170 + i * 120
        draw.rounded_rectangle((850, y, 1170, y + 90), 14, fill=PANEL, outline=(accent if i != 1 else WHITE) + (255,), width=5)
        for j in range(3):
            draw.ellipse((880 + j * 36, y + 35, 900 + j * 36, y + 55), fill=accent + (255 if i != 1 else 60,))
    # the failed one is crossed out
    draw.line((1060, 300, 1140, 370), fill=(255, 90, 90, 255), width=10)
    draw.line((1140, 300, 1060, 370), fill=(255, 90, 90, 255), width=10)
    draw.rounded_rectangle((850, 540, 1170, 600), 14, fill=accent + (255,))
    draw.text((935, 552), "DATABASE", font=font(32), fill=INK + (255,))


def motif_two_nodes(draw, accent, seed):
    for cx, label in ((880, "A"), (1140, "B")):
        draw.ellipse((cx - 80, 280 - 80, cx + 80, 280 + 80), fill=PANEL, outline=accent + (255,), width=7)
        draw.text((cx - 18, 252), label, font=font(52), fill=WHITE + (255,))
    draw.line((960, 260, 1060, 260), fill=accent + (255,), width=7)
    draw.polygon([(1060, 248), (1060, 272), (1078, 260)], fill=accent + (255,))
    draw.line((1060, 300, 960, 300), fill=WHITE + (255,), width=7)
    draw.polygon([(960, 288), (960, 312), (942, 300)], fill=WHITE + (255,))
    draw.rounded_rectangle((870, 440, 1150, 600), 16, fill=PANEL, outline=WHITE + (255,), width=5)
    draw.line((935, 520, 990, 570, 1090, 470), fill=accent + (255,), width=12, joint="curve")


def motif_sealed_box(draw, accent, seed):
    x0, y0 = 860, 220
    draw.polygon([(x0, y0 + 60), (x0 + 150, y0), (x0 + 300, y0 + 60), (x0 + 150, y0 + 120)], fill=(40, 34, 60, 255), outline=accent + (255,))
    draw.polygon([(x0, y0 + 60), (x0 + 150, y0 + 120), (x0 + 150, y0 + 330), (x0, y0 + 270)], fill=PANEL, outline=accent + (255,))
    draw.polygon([(x0 + 300, y0 + 60), (x0 + 150, y0 + 120), (x0 + 150, y0 + 330), (x0 + 300, y0 + 270)], fill=(28, 24, 40, 255), outline=accent + (255,))
    cx, cy = x0 + 225, y0 + 200
    draw.ellipse((cx - 55, cy - 55, cx + 55, cy + 55), fill=accent + (255,))
    draw.line((cx - 25, cy + 2, cx - 6, cy + 24, cx + 30, cy - 20), fill=INK + (255,), width=10, joint="curve")


def motif_hourglass(draw, accent, seed):
    cx = 1010
    draw.line((cx - 140, 160, cx + 140, 160), fill=WHITE + (255,), width=12)
    draw.line((cx - 140, 580, cx + 140, 580), fill=WHITE + (255,), width=12)
    draw.polygon([(cx - 120, 170), (cx + 120, 170), (cx + 12, 370), (cx - 12, 370)], outline=WHITE + (255,), fill=PANEL)
    draw.polygon([(cx - 12, 370), (cx + 12, 370), (cx + 120, 570), (cx - 120, 570)], outline=WHITE + (255,), fill=PANEL)
    draw.polygon([(cx - 70, 260), (cx + 70, 260), (cx + 10, 360), (cx - 10, 360)], fill=accent + (255,))
    draw.polygon([(cx - 90, 570), (cx + 90, 570), (cx + 40, 500), (cx - 40, 500)], fill=accent + (255,))


def motif_chip(draw, accent, seed):
    x0, y0, s = 880, 230, 260
    draw.rounded_rectangle((x0, y0, x0 + s, y0 + s), 22, fill=PANEL, outline=accent + (255,), width=7)
    for i in range(5):
        o = 40 + i * 45
        for (a, b, c, d) in ((x0 + o, y0 - 40, x0 + o, y0), (x0 + o, y0 + s, x0 + o, y0 + s + 40),
                             (x0 - 40, y0 + o, x0, y0 + o), (x0 + s, y0 + o, x0 + s + 40, y0 + o)):
            draw.line((a, b, c, d), fill=WHITE + (255,), width=8)
    draw.text((x0 + 70, y0 + 95), "EDGE", font=font(52), fill=accent + (255,))


def motif_lemma(draw, accent, seed):
    # a drawn "for all" sign: an inverted A
    draw.line((880, 170, 1010, 470), fill=accent + (255,), width=26)
    draw.line((1140, 170, 1010, 470), fill=accent + (255,), width=26)
    draw.line((925, 290, 1095, 290), fill=accent + (255,), width=22)
    draw.rounded_rectangle((860, 520, 1180, 580), 12, fill=PANEL, outline=WHITE + (255,), width=4)
    draw.text((885, 530), "proved | falsified", font=font(30), fill=WHITE + (255,))


def motif_bug(draw, accent, seed):
    cx, cy = 1010, 360
    draw.ellipse((cx - 80, cy - 120, cx + 80, cy + 120), fill=PANEL, outline=accent + (255,), width=8)
    draw.ellipse((cx - 50, cy - 175, cx + 50, cy - 95), fill=PANEL, outline=accent + (255,), width=8)
    for dy in (-60, 0, 60):
        draw.line((cx - 80, cy + dy, cx - 170, cy + dy - 30), fill=WHITE + (255,), width=9)
        draw.line((cx + 80, cy + dy, cx + 170, cy + dy - 30), fill=WHITE + (255,), width=9)
    draw.line((cx - 200, cy + 210, cx + 200, cy - 210), fill=(255, 90, 90, 255), width=14)


def motif_bricks(draw, accent, seed):
    for row in range(5):
        y = 560 - row * 82
        offset = 0 if row % 2 == 0 else 60
        for col in range(3 - (row > 2)):
            x = 840 + offset + col * 125
            draw.rounded_rectangle((x, y, x + 115, y + 70), 8, fill=PANEL, outline=(accent if row < 4 else WHITE) + (255,), width=5)


def motif_signature(draw, accent, seed):
    motif_network(draw, accent, seed)
    draw.rounded_rectangle((850, 470, 1190, 600), 16, fill=PANEL, outline=WHITE + (255,), width=5)
    pts = [(880, 560), (920, 510), (950, 560), (990, 500), (1030, 565), (1070, 515), (1110, 545), (1160, 520)]
    draw.line(pts, fill=accent + (255,), width=8, joint="curve")


MOTIFS = {
    "eye": motif_eye,
    "rotate": motif_rotate,
    "magnifier": motif_magnifier,
    "key": motif_key,
    "servers": motif_servers,
    "two_nodes": motif_two_nodes,
    "sealed_box": motif_sealed_box,
    "hourglass": motif_hourglass,
    "chip": motif_chip,
    "lemma": motif_lemma,
    "bug": motif_bug,
    "bricks": motif_bricks,
    "signature": motif_signature,
    "documents": motif_documents,
    "chain": motif_chain,
    "links": lambda d, a, s: motif_chain(d, a, s, anchor=False),
    "edge": motif_edge,
    "door": motif_door,
    "converge": motif_converge,
    "network": motif_network,
    "origins": motif_network,
    "opener": motif_network,
    "policy": motif_documents,
    "governed": motif_chain,
    "edge": motif_edge,
    "running": motif_door,
    "proof": motif_converge,
}


def make(folder: str, group: str, part: str, hook: str, motif: str = "", out: Path = None) -> Path:
    label, accent, background = GROUPS[group]
    motif = motif or group
    base = cover_image(background, (W, H)).filter(ImageFilter.GaussianBlur(radius=6))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    draw.rectangle((0, 0, W, H), fill=(0, 0, 0, 175))
    draw.rectangle((0, 0, 760, H), fill=INK + (240,))
    draw.line((760, 0, 760, 650), fill=accent + (200,), width=5)
    MOTIFS[motif](draw, accent, folder)

    logo = Image.open(LOGO).convert("RGBA").resize((88, 88), Image.Resampling.LANCZOS)
    overlay.alpha_composite(logo, (52, 40))
    draw.text((158, 50), "GENESIS MESH", font=font(32), fill=WHITE)
    draw.text((158, 92), f"{label}  {part}".strip(), font=font(22), fill=accent)

    draw.rectangle((62, 168, 194, 180), fill=accent)
    lines = len(hook.splitlines())
    size = 96 if lines <= 2 else 84
    while size > 48:
        box = draw.multiline_textbbox((62, 0), hook, font=font(size), spacing=10)
        if box[2] <= 720 and box[3] - box[1] <= 420:
            break
        size -= 2
    y = 215
    for offset in ((5, 5), (3, 3)):
        draw.multiline_text((62 + offset[0], y + offset[1]), hook, font=font(size), fill=(0, 0, 0), spacing=10)
    draw.multiline_text((62, y), hook, font=font(size), fill=WHITE, spacing=10)

    draw.rectangle((0, 650, W, H), fill=accent + (240,))
    draw.text((62, 668), "PORTABLE TRUST FOR SOVEREIGN SYSTEMS", font=font(26), fill=INK)

    image = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    out = out or CAMPAIGNS / folder / "thumbnail.png"
    image.save(out, optimize=True)
    return out


def main(argv):
    if not SPECS:
        raise SystemExit("SPECS is empty")
    for folder, spec in SPECS.items():
        if argv and not any(a in folder for a in argv):
            continue
        if not (CAMPAIGNS / folder).is_dir():
            raise SystemExit(f"missing campaign folder: {folder}")
        group, part, hook, *motif = spec
        print(make(folder, group, part, hook.replace("\\n", "\n"), *motif).relative_to(ROOT))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main(sys.argv[1:])
