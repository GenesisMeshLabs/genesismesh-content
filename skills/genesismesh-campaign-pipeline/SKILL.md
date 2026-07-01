---
name: genesismesh-campaign-pipeline
description: End-to-end Genesis Mesh content campaign creation inside genesismesh-content. Use when asked to create, plan, draft, produce, or publish a Genesis Mesh campaign with campaign folders, article.md, voiceover.md, voiceover.ssml, Azure TTS narration, Revid video generation, thumbnails, youtube.md, patreon.md, campaign.json, or VOICE_PLAN.md updates.
---

# Genesis Mesh Campaign Pipeline

Use this skill from the repository root.

The goal is a complete campaign folder that can move from concept to publishable assets while keeping generated/private files out of Git.

## Hard Rules

- Keep Genesis Mesh framed as portable trust for sovereign systems. Read `MESSAGING.md` before drafting.
- Ask until the article is good enough. Do not proceed from `article.md` to voiceover until the user approves the article.
- Create `campaign.json` early because repo scripts depend on it, then update it at the end.
- Run Revid `estimate` before `render`; do not run `render --yes` until the user explicitly accepts the estimate.
- Keep rendered MP4s in `videos/renders/`, narration in `campaigns/**/audio/`, Revid jobs in `videos/revid-jobs/`, and final upload thumbnails in `videos/thumbnails/`. Do not create campaign-level `renders/` folders.
- Treat `videos/` as the production workspace: scripts in `videos/scripts/`, committed upload thumbnails in `videos/thumbnails/`, ignored MP4s/review frames in `videos/renders/`, and ignored provider state in `videos/revid-jobs/`.
- Keep `patreon.md` editorial. YouTube titles can be search/click optimized; Patreon titles do not need to match YouTube.
- Do not commit `.env`, audio, MP4s, Revid jobs, drafts, temporary upload URLs, or provider responses.

## Required Context

Read these before acting:

- `MESSAGING.md`
- `README.md`
- `videos/scripts/VOICE_PLAN.md`
- `skills/genesismesh-campaign-pipeline/references/campaign-contract.md`

Inspect nearby campaign examples:

- Horizontal: `campaigns/01-why-genesismesh/`
- Use case: `campaigns/08-use-cases/01-ai-agents/`

## Workflow

### 1. Classify and Create Folder

Ask whether the campaign is:

- horizontal/top-level narrative, or
- use case under `campaigns/08-use-cases/`.

Create the next ordered folder:

- horizontal: `campaigns/<NN>-<slug>/`
- use case: `campaigns/08-use-cases/<NN>-<slug>/`

Use the helper to avoid numbering/path mistakes:

```powershell
python .\skills\genesismesh-campaign-pipeline\scripts\scaffold_campaign.py --type horizontal --slug portable-trust --title "Portable Trust"
python .\skills\genesismesh-campaign-pipeline\scripts\scaffold_campaign.py --type use-case --slug healthcare-trust --title "Use Case: Healthcare Trust"
```

After scaffolding, adjust `campaign.json` as the campaign becomes concrete.

### 2. Interrogate Until Article Is Approved

Gather at least:

- audience
- primary message
- problem
- promised outcome
- call to action
- source docs or repo evidence
- intended channels
- whether the tone is technical, founder-note, enterprise/security, or developer-facing

Draft `article.md`. Ask focused follow-up questions when the article has weak claims, vague audience, missing proof, or messaging drift. Iterate until the user approves.

### 3. Generate Voiceover

Create `voiceover.md` from the approved article without reducing substance unnecessarily. It may be more spoken and structured than the article, but it must preserve the argument.

Then create `voiceover.ssml`:

- use the selected Azure voice in the `<voice name="...">`
- add measured pauses with `<break time="..."/>`
- use emphasis sparingly
- keep SSML valid XML

### 4. Select Voice

Use `videos/scripts/VOICE_PLAN.md`.

Prefer an unused DragonHDLatestNeural voice when available. Reuse only when it best fits the campaign. Update `VOICE_PLAN.md` with:

- campaign folder or slug
- voice name
- short role description

Also write `voice` and `voice_role` into `campaign.json`.

### 5. Generate Azure TTS

Run:

```powershell
python .\videos\scripts\generate_tts.py <campaign-slug>
```

For nested use cases, use the stable slug from `campaign.json`, for example:

```powershell
python .\videos\scripts\generate_tts.py use-cases/healthcare-trust
```

Verify `campaigns/<campaign>/audio/narration.wav` exists.

### 6. Generate Revid Video

Estimate first:

```powershell
python .\videos\scripts\generate_revid_video.py estimate <campaign-slug> --workflow audio-to-video --media-type stock-video --density high --caption-preset Elegant --ratio 16:9
```

Show the estimate to the user. Only after explicit approval, render:

```powershell
python .\videos\scripts\generate_revid_video.py render <campaign-slug> --workflow audio-to-video --media-type stock-video --density high --caption-preset Elegant --ratio 16:9 --yes
```

Poll the returned job id:

```powershell
python .\videos\scripts\generate_revid_video.py poll <revid-project-id> --out .\videos\renders\<slug>-revid-stock.mp4
```

Update `campaign.json` output and publishing render paths to the final file.

### 7. Generate Thumbnail

Use or update:

```text
videos/scripts/generate_thumbnails.py
```

Generate a single new campaign thumbnail:

```powershell
python .\videos\scripts\generate_thumbnails.py --slug <safe-slug> --text "TRUST THAT\nTRAVELS" --background shared/images/marketing/marketing-hero-trust-fabric.png
```

For the built-in campaign set, run without arguments.

Final thumbnail path:

```text
videos/thumbnails/<slug>.png
```

Thumbnail copy should imply a problem or outcome. Keep it short, branded, and readable at small size.

### 8. Create Publishing Files

Create campaign-root files:

- `youtube.md`
- `patreon.md`

`youtube.md` should include title, description, tags, category, thumbnail path, render path, and a video URL placeholder if not uploaded yet.

`patreon.md` should use an editorial title and founder-note/article framing. Include the YouTube URL when available, otherwise `[YouTube video link]`.

### 9. Finalize Campaign JSON

Make sure `campaign.json` includes:

- `slug`, `title`, `status`
- `audience`, `channels`
- `primary_message`, `call_to_action`, `source_docs`
- `slogan`
- `voice`, `voice_role`
- `images`
- `thumbnail`
- `output`
- `publishing.youtube`
- optionally `publishing.patreon`

Validate JSON:

```powershell
Get-Content -Raw .\campaigns\<path>\campaign.json | ConvertFrom-Json > $null
```

## Final Checks

Before calling the campaign complete:

- article approved by user
- voiceover and SSML created
- `VOICE_PLAN.md` updated
- TTS generated
- Revid estimate shown and render approved
- video rendered or an explicit pending job noted
- thumbnail generated
- `youtube.md` and `patreon.md` created
- `campaign.json` finalized and valid
- `git status --short --ignored` checked for accidental secrets or generated binaries
