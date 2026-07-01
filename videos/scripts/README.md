# Video Scripts

These scripts turn campaign text and assets into narration and simple slideshow videos.

## Setup

Install Python dependencies for Azure TTS:

```powershell
python -m pip install -r .\videos\scripts\requirements.txt
```

Install `ffmpeg` and make sure it is on `PATH`.

## Environment

The scripts load `videos/scripts/.env` automatically. Do not commit real keys.

Supported names:

```text
AZURE_SPEECH_KEY=
AZURE_SPEECH_ENDPOINT=https://<resource>.cognitiveservices.azure.com/
AZURE_SPEECH_VOICE=en-US-Adam:DragonHDLatestNeural
REVID_API_KEY=
REVID_API_BASE=https://www.revid.ai/api/public/v3
REVID_VOICE_ID=
```

Aliases also work: `AZURE_TTS_KEY`, `SPEECH_KEY`, `speech_key`, `AZURE_TTS_ENDPOINT`, `SPEECH_ENDPOINT`, `endpoint_url`, `AZURE_TTS_VOICE`, `speech_voice`.

## Generate Narration

The TTS script prefers `voiceover.ssml` when present and falls back to `voiceover.md` for draft narration.

The campaign voice map lives in `VOICE_PLAN.md`. The current set uses distinct Azure `DragonHDLatestNeural` voices per campaign.

```powershell
python .\videos\scripts\generate_tts.py portable-trust
```

Nested use-case campaigns are supported:

```powershell
python .\videos\scripts\generate_tts.py use-cases/ai-agents
```

Override the voice for one render:

```powershell
python .\videos\scripts\generate_tts.py portable-trust --voice "en-US-Adam:DragonHDLatestNeural"
```

The output is:

```text
campaigns/<campaign>/audio/narration.wav
```

SSML files should be Azure-compatible:

```xml
<speak version="1.0" xml:lang="en-US">
  <voice name="en-US-Adam:DragonHDLatestNeural">
    Put production narration here.
    <break time="500ms"/>
    Use emphasis only where the delivery needs it.
  </voice>
</speak>
```

## Generate Video

```powershell
python .\videos\scripts\generate_video.py portable-trust
```

By default, `generate_video.py` requires `audio/narration.wav`. Generate TTS first. For a deliberate visual-only draft:

```powershell
python .\videos\scripts\generate_video.py portable-trust --no-audio
```

The output path comes from the campaign's `campaign.json`.

## Generate Revid Video

Use Revid for higher-polish campaign videos with stock footage, moving AI images, richer subtitles, and optional Revid voices.

Credit rules:

- Run `estimate` before `render`.
- Azure TTS remains the default voice path for this repo.
- Revid voice is disabled by default; enable it with `--revid-voice`.
- Revid music is disabled by default; enable it with `--music`.
- `stock-video` is the default media type to avoid AI visual-generation cost.
- Use `moving-image` or `ai-video` only when the campaign needs AI-generated visuals.

Estimate:

```powershell
python .\videos\scripts\generate_revid_video.py estimate portable-trust
```

Render:

```powershell
python .\videos\scripts\generate_revid_video.py render portable-trust --yes
```

Use moving AI images and Revid voice deliberately:

```powershell
python .\videos\scripts\generate_revid_video.py estimate portable-trust --media-type moving-image --revid-voice
python .\videos\scripts\generate_revid_video.py render portable-trust --media-type moving-image --revid-voice --yes
```

Poll and download when ready:

```powershell
python .\videos\scripts\generate_revid_video.py poll <revid-project-id>
```

Job responses are written under `videos/revid-jobs/` and ignored by Git.
