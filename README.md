# Genesis Mesh Content Pipeline

This folder is for articles, campaign assets, voiceover scripts, generated audio, and generated videos.

The campaign structure is split into horizontal narrative campaigns first, then use-case campaigns. This keeps Genesis Mesh positioned as portable trust infrastructure for sovereign systems, not as an AI-only product.

```text
genesismesh-content/
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
      .env
    renders/
    thumbnails/
    source/
```

## Positioning

Short slogan:

```text
Genesis Mesh: portable trust for sovereign systems.
```

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

## Campaign Workflow

1. Edit `article.md`.
2. Edit `voiceover.md`.
3. Add or update `voiceover.ssml` when the speech is ready for production TTS.
4. Adjust `campaign.json` images, voice, and timing.
5. Generate narration with `generate_tts.py`.
6. Generate video with `generate_video.py`.
7. Review the rendered video before publishing.

Shared GIFs from the Genesis Mesh docs live in `shared/examples/gifs/` and can be added to campaigns later as proof/demo material.
