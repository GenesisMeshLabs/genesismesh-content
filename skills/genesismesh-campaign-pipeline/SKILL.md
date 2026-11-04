---
name: genesismesh-campaign-pipeline
description: End-to-end Genesis Mesh content campaign creation inside genesismesh-content. Use when asked to create, plan, draft, produce, or publish a Genesis Mesh campaign with campaign folders, article.md, voiceover.md, voiceover.ssml, Azure TTS narration, Revid video generation, thumbnails, youtube.md, patreon.md, campaign.json, or VOICE_PLAN.md updates.
---

# Genesis Mesh Campaign Pipeline

Use this skill from the repository root.

The default deliverable is a short, substantive article, branded cover, source links and a LinkedIn draft. “Campaign” is the existing repository label, not a requirement to produce a multimedia campaign. Keep articles as short as the substance allows, with no rigid word count. Keep generated/private files out of Git.

## Hard Rules

- Default to article + cover + source links + LinkedIn draft. Voiceover, audio, video, Revid, YouTube assets and media-specific approvals are optional and apply only when the user requests that media. Do not ask for optional media approval or make missing media block an article.
- Read and apply `references/editorial-evidence-standard.md` and `references/design-system.md` before drafting. Evidence, technical review, visual review and explicit publication approval are mandatory release gates.
- Every substantive article must explain a concrete, sourced Genesis Mesh flow, its authority boundary, actual SDK/API calls or artifacts, a failure path and limitations. Word count is guidance, not a substitute for substance.
- Write evergreen public-facing articles: generally describe capabilities without individual SDK names or version numbers, unless the user requests them or they are necessary to avoid material ambiguity. Clearly separate implemented capabilities from planned broader coverage; never imply parity that is not implemented. Keep exact SDK/platform coverage, pinned revisions and dated release checks in the internal evidence ledger; precise source links need not put versions in the prose.
- Pin code, docs and tests to inspected revisions; separate documented, implemented, test-covered and actually tested behavior. Verify package/release availability independently from repository heads. Research, incident reports and formal models are not product guarantees.
- Inventory all relevant SDK languages, gateway, Network Authority, CLI and edge surfaces. Do not assume parity. Trace exact fallback triggers, exclusions, opt-in flags, freshness limits and reconnect behavior for the version recorded in the evidence ledger; distinguish queued evidence from queued actions.
- Include citations beside material claims, a reproducible “Check it yourself” section, and verified Website, documentation, demo and GitHub links. If a public demo is unavailable, say so and supply a documented local example instead.
- For reader-facing walkthroughs and guides, prefer the verified canonical page on `docs.genesismesh.org`, with the exact relevant anchor when available. Open the page and verify its content and anchor; never derive or guess a URL from a repository path. Keep direct GitHub links for code/tests and pinned internal evidence. If no canonical docs counterpart can be verified, use a valid repository document and label it explicitly as repository documentation.
- Use the existing branded series thumbnail layout and supplied logo, palette and typography; inspect actual final pixels at full size and 320 × 180. Keep hooks and diagrams no stronger than the evidence.
- Do not publish or push campaign drafts to the public repository until those gates pass. Existing generator scripts do not enforce approval.
- Keep Genesis Mesh framed as portable trust for sovereign systems. Read `MESSAGING.md` before drafting.
- Ask until the article is good enough. Do not proceed from `article.md` to voiceover until the user approves the article.
- Create/update `campaign.json` when required by the chosen repository workflow or scripts; do not populate unused media fields or fabricate media assets for an article-only deliverable.
- When Revid video is explicitly requested, run Revid `estimate` before `render`; do not run `render --yes` until the user explicitly accepts the estimate.
- Keep rendered MP4s in `videos/renders/`, narration in `campaigns/**/audio/`, Revid jobs in `videos/revid-jobs/`, and final upload thumbnails in `videos/thumbnails/`. Do not create campaign-level `renders/` folders.
- Treat `videos/` as the production workspace: scripts in `videos/scripts/`, committed upload thumbnails in `videos/thumbnails/`, ignored MP4s/review frames in `videos/renders/`, and ignored provider state in `videos/revid-jobs/`.
- Keep `patreon.md` editorial. YouTube titles can be search/click optimized; Patreon titles do not need to match YouTube.
- Do not commit `.env`, audio, MP4s, Revid jobs, drafts, temporary upload URLs, or provider responses.

## Required Context

Read these before acting:

- `MESSAGING.md`
- `README.md`
- `videos/scripts/VOICE_PLAN.md` only when narration is requested
- `skills/genesismesh-campaign-pipeline/references/campaign-contract.md`
- `skills/genesismesh-campaign-pipeline/references/editorial-evidence-standard.md`
- `skills/genesismesh-campaign-pipeline/references/design-system.md`

`agents/openai.yaml` is UI metadata for agents that surface this skill in a picker or prompt list. It is not a workflow step and does not need to be loaded unless maintaining the skill metadata itself.

Inspect nearby campaign examples:

- Horizontal: `campaigns/01-why-genesismesh/`
- Use case: `campaigns/08-use-cases/01-ai-agents/`

## Workflow

Default article path: steps 1–2, then 7–9 as applicable. Steps 3–6 are an optional media workflow, used only when explicitly requested. Complete the article, cover, linked evidence and LinkedIn draft without waiting for unrequested media.

### 1. Classify and Create Folder

Ask whether the campaign is:

- horizontal/top-level narrative, or
- use case under `campaigns/08-use-cases/`.

Create the next ordered folder:

- horizontal: `campaigns/<NN>-<slug>/`
- use case: `campaigns/08-use-cases/<NN>-<slug>/`

For the default article-only path, inspect existing folder numbers, create the next unused directory without overwriting anything, and add only `article.md`, `linkedin.md`, and the evidence/review packet. Generate the branded cover in step 7. Add `patreon.md` only for a selected Patreon channel. Add `campaign.json` only if the chosen scripts require it, with applicable article metadata and cover paths, not voice/audio/video/YouTube placeholders. When revising an existing article, reuse its folder and preserve unrelated assets.

Do **not** run `scaffold_campaign.py` for article-only work: its current implementation always creates multimedia placeholders. No article-only mode is implemented in that helper.

Only when the user explicitly requests a full multimedia campaign, use the legacy helper to avoid numbering/path mistakes:

```powershell
python .\skills\genesismesh-campaign-pipeline\scripts\scaffold_campaign.py --type horizontal --slug portable-trust --title "Portable Trust"
python .\skills\genesismesh-campaign-pipeline\scripts\scaffold_campaign.py --type use-case --slug healthcare-trust --title "Use Case: Healthcare Trust"
```

After an explicitly requested multimedia scaffold, adjust `campaign.json` as the campaign becomes concrete. Do not use the helper just to obtain numbering or metadata for an article.

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

Create `evidence.md` with pinned implementation/docs/tests, per-surface coverage, release status and observed verification. Trace a real Genesis Mesh flow and its failure path; qualify SDK/gateway/edge differences and exact fallback semantics. Create `review.md` to track blocking issues and approval of exact revisions. Include claim-level citations, a “Check it yourself” section, and verified Website/docs/demo/GitHub links. Keep private or unreleased evidence in the ignored local review packet.

Draft `article.md`. Ask focused follow-up questions when the article has weak claims, vague audience, missing proof, or messaging drift. Iterate until the user approves.

### 3. Generate Voiceover (Optional, Only When Requested)

Create `voiceover.md` from the approved article without reducing substance unnecessarily. It may be more spoken and structured than the article, but it must preserve the argument.

Then create `voiceover.ssml`:

- use the selected Azure voice in the `<voice name="...">`
- add measured pauses with `<break time="..."/>`
- use emphasis sparingly
- keep SSML valid XML

### 4. Select Voice (Optional, Only When Requested)

Use `videos/scripts/VOICE_PLAN.md`.

Prefer an unused DragonHDLatestNeural voice when available. Reuse only when it best fits the campaign. Update `VOICE_PLAN.md` with:

- campaign folder or slug
- voice name
- short role description

Also write `voice` and `voice_role` into `campaign.json`.

### 5. Generate Azure TTS (Optional, Only When Requested)

Run:

```powershell
python .\videos\scripts\generate_tts.py <campaign-slug>
```

For nested use cases, use the stable slug from `campaign.json`, for example:

```powershell
python .\videos\scripts\generate_tts.py use-cases/healthcare-trust
```

`generate_tts.py` resolves stable slugs by scanning campaign JSON when a direct folder path does not exist, so numbered folders such as `campaigns/08-use-cases/02-healthcare-trust/` are valid. Do not assume the on-disk folder starts with the exact stable slug.

Verify `campaigns/<campaign>/audio/narration.wav` exists.

### 6. Generate Revid Video (Optional, Only When Requested)

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

Follow `references/design-system.md`. For existing series layouts, use `videos/scripts/generate_series_thumbnails.py` with a campaign-specific folder filter after adding the intended specification. It writes the campaign cover and synchronizes the configured upload copy when metadata exists. Do not regenerate unrelated campaigns. For standalone thumbnails, use or update:

```text
videos/scripts/generate_thumbnails.py
```

Generate a single new campaign thumbnail:

```powershell
python .\videos\scripts\generate_thumbnails.py --slug <safe-slug> --text "TRUST THAT\nTRAVELS" --background shared/images/marketing/marketing-hero-trust-fabric.png
```

The standalone generator without arguments regenerates the entire built-in campaign set. Do not use that batch mode unless the user explicitly requests regeneration of that set; for an individual campaign, pass its specific `--slug`, `--text` and `--background`. Likewise, never run the series generator without a campaign filter unless the user explicitly requests the full series set.

Final thumbnail path:

```text
videos/thumbnails/<slug>.png
```

Thumbnail copy should imply a problem or outcome. Keep it short, branded, and readable at small size.

### 8. Create Publishing Files

Create `linkedin.md` as a concise draft accompanying the article, with the approved article link once available. Drafting does not authorize posting. Create `patreon.md` only when Patreon is a selected channel, using the article's editorial framing. Do not insert a YouTube placeholder when no video is requested.

Create `youtube.md` only when a YouTube video is requested; include title, description, tags, category, thumbnail path, render path and a video URL placeholder until uploaded. Add the verified YouTube URL to other selected channels only when relevant.

### 9. Finalize Campaign JSON

When `campaign.json` is used, make sure it includes only the fields applicable to the selected workflow:

- `slug`, `title`, `status`
- `audience`, `channels`
- `primary_message`, `call_to_action`, `source_docs`
- `slogan`
- `voice`, `voice_role` only for requested narration
- `images`
- `thumbnail`
- `output` only for requested video
- `publishing.youtube` only for requested YouTube publication
- optionally `publishing.patreon`

Validate JSON:

```powershell
Get-Content -Raw .\campaigns\<path>\campaign.json | ConvertFrom-Json > $null
```

## Final Checks

Before calling the campaign complete:

- `evidence.md` and `review.md` complete; no unresolved blocking claims
- implementation/docs/test distinctions and current release availability checked across all relevant surfaces
- claim-level citations, reproducible reader check, and public Website/docs/demo/GitHub links verified; reader-facing walkthroughs/guides use verified canonical docs pages and exact anchors where available, with repository-document fallbacks labeled explicitly
- final thumbnail inspected at full resolution and 320 × 180 against the design system
- derived assets contain no new unsupported claims
- exact final assets and destination channels explicitly approved before publication
- article approved by user
- short substantive article, branded cover, source links and `linkedin.md` draft complete
- publishing files created only for selected channels
- `campaign.json` finalized and valid when used
- only if narration/video was requested: applicable voiceover/SSML, voice plan, TTS, approved Revid estimate/render and video checks complete or an explicit pending job noted
- `git status --short --ignored` checked for accidental secrets or generated binaries
