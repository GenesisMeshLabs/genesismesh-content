# Genesis Mesh Content Pipeline

This folder is for articles, campaign assets, voiceover scripts, generated audio, and generated videos.

The campaign structure is split into horizontal narrative campaigns first, then use-case campaigns. This keeps Genesis Mesh positioned as portable trust infrastructure for sovereign systems, not as an AI-only product.

```text
genesismesh-content/
  MESSAGING.md
  campaigns/
    01-why-genesismesh/
    02-portable-trust/
    03-sovereign-systems/
    04-recognition-and-revocation/
    05-auditable-trust-state/
    06-protocol-interoperability/
    07-trust-api-and-sdks/
    08-use-cases/
      01-ai-agents/
      02-edge-infrastructure/
      03-supply-chain-trust/
      04-enterprise-integration/
      05-data-access-governance/
  shared/
    images/
      brand/
      marketing/
    examples/
      gifs/
    templates/
  videos/
    scripts/
      generate_tts.py
      generate_video.py
      generate_revid_video.py
      .env
    revid-jobs/
    renders/
    thumbnails/
    source/
```

## Positioning

Short slogan:

```text
Genesis Mesh: portable trust for sovereign systems.
```

Use `MESSAGING.md` as the top-level messaging contract before drafting or generating campaign content.

Campaign rules:

- Lead with systems, trust, sovereignty, recognition, revocation, and auditability.
- Treat AI agents as one use case, not the top-level frame.
- Avoid marketplace, token, reputation-score, central-registry, blockchain, and agent-framework language.
- Keep claims aligned with `genesismesh/VISION.md` and `genesismesh/docs/development/strategy.md`.

## Dynamic Voiceover

The text-to-speech step reads each campaign's voiceover. Use `voiceover.md` for drafting and `voiceover.ssml` for production delivery. If `voiceover.ssml` exists, the TTS script uses it. Otherwise it falls back to `voiceover.md`.

Voice is dynamic:

- Set a default voice in `videos/scripts/.env`.
- Override it per campaign in `campaign.json`.
- Override it per command with `--voice`.
- Replace the TTS provider later without changing campaign content.

The current script targets Azure AI Speech using the Speech SDK.

SSML is useful for campaign speeches because it controls pauses, emphasis, pacing, and pronunciation while keeping the article draft readable.

Minimal campaign SSML:

```xml
<speak version="1.0" xml:lang="en-US">
  <voice name="en-US-Adam:DragonHDLatestNeural">
    Genesis Mesh is <emphasis level="moderate">portable trust</emphasis> for sovereign systems.
    <break time="600ms"/>
    Systems can connect today. But trust still breaks at the boundary.
  </voice>
</speak>
```

Expected `.env` keys:

```text
AZURE_SPEECH_KEY=...
AZURE_SPEECH_ENDPOINT=https://<resource>.cognitiveservices.azure.com/
AZURE_SPEECH_VOICE=en-US-Adam:DragonHDLatestNeural
```

Generate audio using the stable campaign slug from `campaign.json`:

```powershell
python .\videos\scripts\generate_tts.py portable-trust
python .\videos\scripts\generate_tts.py use-cases/ai-agents
```

The output goes to:

```text
campaigns/<campaign>/audio/narration.wav
```

## Dynamic Video

The video step reads `campaign.json`, takes the configured images, requires generated narration by default, and renders a video with `ffmpeg`.

Generate video with audio:

```powershell
python .\videos\scripts\generate_video.py portable-trust
```

Render a deliberate silent draft:

```powershell
python .\videos\scripts\generate_video.py portable-trust --no-audio
```

The output goes to:

```text
videos/renders/<campaign-slug>.mp4
```

## Revid Video Generation

`generate_revid_video.py` is the optional higher-polish video path. Use it for stock footage, moving AI images, richer captions, and social-video variants.

Cost posture:

- Revid render calls consume credits. The Revid API documents a base render cost plus generation costs.
- Always run `estimate` before `render`.
- Azure Speech remains the default TTS path because it is cheaper for this workspace.
- Revid voice generation is opt-in with `--revid-voice`.
- Revid background music is opt-in with `--music`.
- `stock-video` is the default media type because it avoids AI visual-generation cost; use `moving-image` or `ai-video` deliberately when the campaign needs it.

Estimate credits:

```powershell
python .\videos\scripts\generate_revid_video.py estimate portable-trust
```

Render with default cost controls:

```powershell
python .\videos\scripts\generate_revid_video.py render portable-trust --yes
```

Render with Revid-generated voice and moving AI images:

```powershell
python .\videos\scripts\generate_revid_video.py estimate portable-trust --media-type moving-image --revid-voice
python .\videos\scripts\generate_revid_video.py render portable-trust --media-type moving-image --revid-voice --yes
```

Poll a render:

```powershell
python .\videos\scripts\generate_revid_video.py poll <revid-project-id>
```

## Campaign Workflow

1. Check `MESSAGING.md`.
2. Update `campaign.json` metadata: status, audience, channels, primary message, call to action, and source docs.
3. Edit `article.md`.
4. Edit `voiceover.md`.
5. Add or update `voiceover.ssml` when the speech is ready for production TTS.
6. Adjust `campaign.json` images, voice, and timing.
7. Generate narration with `generate_tts.py`.
8. Generate a fast local video with `generate_video.py`, or estimate and render a polished Revid video with `generate_revid_video.py`.
9. Review the rendered video before publishing.

Each campaign should keep this structure:

```text
article.md
campaign.json
voiceover.md
voiceover.ssml
audio/
renders/
```

`source_docs` entries in `campaign.json` refer to source paths in the upstream `genesismesh` repository unless the file also exists in this content repo.

Shared GIFs from the Genesis Mesh docs live in `shared/examples/gifs/` and can be added to campaigns later as proof/demo material.
