# AGENT.md - Genesis Mesh Content

This repository contains campaign articles, messaging guardrails, voiceover scripts, SSML, shared media assets, and video-generation tooling for Genesis Mesh.

## Messaging Rules

- Use `MESSAGING.md` as the source of truth before creating or editing campaign content.
- Frame Genesis Mesh as portable trust infrastructure for sovereign systems.
- Treat AI agents as one use case, not the top-level category.
- Avoid marketplace, token, reputation-score, central-registry, blockchain, cloud-vendor, and agent-framework framing.
- Keep public claims aligned with upstream `genesismesh` source docs and current SDK/package status.

## Content Structure

- Draft long-form article work can live under `drafts/`; this directory is ignored locally.
- Publishable campaign content lives under `campaigns/`.
- Reusable agent workflows live under `skills/`; use `skills/genesismesh-campaign-pipeline/SKILL.md` for end-to-end campaign creation.
- Keep `article.md`, `voiceover.md`, and `voiceover.ssml` separate:
  - `article.md` is for human reading.
  - `voiceover.md` is the editable narration draft.
  - `voiceover.ssml` is the production TTS script.

## Video Tooling

Two video paths are supported:

- `generate_video.py`: local `ffmpeg` slideshow from existing campaign images and generated narration.
- `generate_revid_video.py`: Revid API workflow for AI motion images, stock-video scenes, richer subtitles, music, and Revid voices.

Use Revid when the campaign needs more polished motion, stock footage, subtitle styling, or voice variety. Use the local renderer for fast deterministic drafts and regression checks.

Cost rules:

- Run Revid `estimate` before `render`.
- Revid `render` requires `--yes` because it can spend credits.
- Azure Speech is the default TTS path because this workspace has Azure credits.
- Revid voice generation is opt-in only with `--revid-voice`.
- Revid music is opt-in only with `--music`.
- Prefer `stock-video` first for polished footage without AI visual-generation cost.
- Use `moving-image` or `ai-video` deliberately when the extra Revid credits are worth it.

## Secrets and Generated Output

Never commit:

- `videos/scripts/.env`
- API keys
- generated narration WAV files
- rendered MP4 files
- Revid job responses under `videos/revid-jobs/`
- generated/private draft artifacts unless explicitly promoted

Do not print secrets in terminal output or documentation.
