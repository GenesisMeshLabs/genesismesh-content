# Genesis Mesh Campaign Design System

Required for every new or revised campaign cover, thumbnail, diagram and derived visual. Use with the [editorial evidence standard](editorial-evidence-standard.md): a visual claim needs the same evidence as prose.

## Existing source of truth

Reuse `shared/images/brand/logo-reverse.png` on dark backgrounds, `logo.png` on appropriate light backgrounds, and the supplied SVG variants for scalable use. Do not redraw, stretch, recolor, crop or generate a substitute logo. Approved imagery lives in `shared/images/marketing/` and `shared/images/brand/background.png`.

The concrete series implementation is `videos/scripts/generate_series_thumbnails.py`; the original standalone implementation is `videos/scripts/generate_thumbnails.py`. This document records the existing system inspected at content-repository revision `614e3630dfe61e480b4200b2d0e181376408b4f6`. Inspect the current scripts before production and update this reference intentionally if the system changes. Do not mix their layouts accidentally.

## Brand tokens

- Canvas: 1280 × 720 pixels, 16:9, RGB PNG for the final thumbnail.
- Ink: `#070807`; primary text: `#FFFFFF`; primary lime: `#D9FF61`.
- Series accents: policy/evidence `#61DAFF`; governed changes and authority/incidents `#FFBE50`; edge `#FF8066`; running/operations `#B296FF`; origins, opener and proof use lime.
- Match the series label and part number to the actual campaign structure. Color is a supplement, never the only way to identify a series or explain status.
- Typography: the scripts' `font()` helper prefers bold Arial/Segoe UI on Windows, DejaVu Sans on Linux and Arial on macOS. Font fallback can alter wrapping; record the actual font and inspect the output. Do not rely on the tiny default bitmap font for production.

## Series thumbnail layout

The series generator defines:

- Dark left text panel from x=0 to 760; accent divider at x=760.
- Reverse logo at (52,40), 88 × 88; “GENESIS MESH” at (158,50), 32 px.
- Series label/part at (158,92), 22 px, in the series accent.
- Accent rule at (62,168)–(194,180).
- Hook at (62,215); usually 2–3 short lines; initial 96 px for up to two lines or 84 px for more, fitted down toward 48 px. Keep its right edge at or before x=720 and height within 420 px.
- Semantic motif primarily within (790,90)–(1230,620); keep all marks inside the canvas and out of the text region.
- Accent footer at y=650–720; the line “PORTABLE TRUST FOR SOVEREIGN SYSTEMS” at (62,668), 26 px in ink.

These coordinates are the baseline, not permission to accept overflow. Prefer rewriting a long hook over shrinking text. Keep the brand, hook and meaning legible when reduced to 320 × 180. Reserve space for platform cropping/overlays; inspect the intended platform preview rather than assuming the full image always displays.

## Content and imagery

- Use one focused visual idea and a short, truthful problem/outcome hook. The thumbnail must be faithful to the article, not stronger than its evidence.
- Reuse the existing series motif where it fits; otherwise add a clear motif in the same line/panel style. Do not run a generator across all campaigns just to change one.
- Draw actual authority boundaries and distinguish signed evidence, policy decision, execution and verification in explanatory diagrams. Label arrows and actors; distinguish online/offline paths and explicit denial from unavailable service.
- A seal, check mark or chain motif is decorative unless it denotes a specific, evidenced property. It must not imply universal security, blockchain, certification or completed execution.
- Label conceptual diagrams and illustrative scenarios. Product screenshots must come from the stated version/environment with secrets and personal data removed. Never invent UI or output and present it as real.
- Prefer supplied brand/marketing assets over generic stock locks, robot heads, glowing circuitry or AI imagery that changes the portable-trust positioning. New art must fit the same palette, typography and hierarchy.
- Keep backgrounds quiet and dark enough for white text. Inspect contrast and readability in grayscale and at small size. Supply concise alt text explaining the meaningful content, not just colors.

## Files and reproducibility

For series campaigns the generator writes `campaigns/<path>/thumbnail.png` as the Patreon/article cover. When `campaign.json` exists, it also synchronizes the configured upload copy under `videos/thumbnails/`. Keep both byte-identical after approval. The standalone generator writes directly to `videos/thumbnails/<safe-slug>.png`.

Reference the final upload path in both `campaign.json.thumbnail` and `publishing.youtube.thumbnail` when YouTube is used. Keep rendered video and review frames under ignored `videos/renders/`, not in campaign folders. Do not change unrelated campaign images, hook text or numbering while producing a new cover.

Record generator revision, selected campaign/group/motif, exact hook, source asset paths, font, output path and file hash in the review packet. Retain an editable source or deterministic generation recipe. Do not publish temporary provider/download URLs.

## Visual acceptance checklist

- Inspect the actual exported image at full resolution and at 320 × 180; a script exit code is not visual approval.
- Confirm dimensions, RGB format, intact logo, correct spelling, series label/part and footer.
- Confirm no clipping, overlaps, illegible type, unexpected font fallback or ambiguous arrows.
- Verify title, hook, artwork, article and publication metadata tell the same evidenced story; compare narration too when present.
- Confirm final cover/upload copies and metadata agree; check the target platform's current upload requirements.
- Only when video/narration is requested, inspect video frames, captions, narration timing and final thumbnail together before release. Mark illustrative footage as appropriate; captions must not introduce unsupported claims.
- Record the reviewer and approved asset hashes. Changes after approval require another affected-asset review.

A campaign is not release-ready until both the editorial and visual checklists pass and publication approval covers the final assets and channels.
