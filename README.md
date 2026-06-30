# Genesis Mesh Content Pipeline

This folder is for articles, campaign assets, voiceover scripts, generated audio, and generated videos.

The campaign structure is split into horizontal narrative campaigns first, then use-case campaigns. This keeps Genesis Mesh positioned as portable trust infrastructure for sovereign systems, not as an AI-only product.

```text
genesismesh-content/
  campaigns/
    why-genesismesh/
    portable-trust/
    sovereign-systems/
    recognition-and-revocation/
    auditable-trust-state/
    protocol-interoperability/
    trust-api-and-sdks/
    use-cases/
      ai-agents/
      edge-infrastructure/
      supply-chain-trust/
      enterprise-integration/
      data-access-governance/
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

The text-to-speech step reads each campaign's `voiceover.md`. Voice is dynamic:

- Set a default voice in `videos/scripts/.env`.
- Override it per campaign in `campaign.json`.
- Override it per command with `--voice`.
- Replace the TTS provider later without changing campaign content.

The current script targets Azure AI Speech using the Speech SDK.

Expected `.env` keys:

```text
AZURE_SPEECH_KEY=...
AZURE_SPEECH_ENDPOINT=https://<resource>.cognitiveservices.azure.com/
AZURE_SPEECH_VOICE=en-US-Adam:DragonHDLatestNeural
```

Generate audio:

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
3. Adjust `campaign.json` images, voice, and timing.
4. Generate narration with `generate_tts.py`.
5. Generate video with `generate_video.py`.
6. Review the rendered video before publishing.

Shared GIFs from the Genesis Mesh docs live in `shared/examples/gifs/` and can be added to campaigns later as proof/demo material.
