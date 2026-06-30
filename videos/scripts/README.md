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
AZURE_SPEECH_KEY=...
AZURE_SPEECH_ENDPOINT=https://<resource>.cognitiveservices.azure.com/
AZURE_SPEECH_VOICE=en-US-Adam:DragonHDLatestNeural
```

Aliases also work: `AZURE_TTS_KEY`, `SPEECH_KEY`, `speech_key`, `AZURE_TTS_ENDPOINT`, `SPEECH_ENDPOINT`, `endpoint_url`, `AZURE_TTS_VOICE`, `speech_voice`.

## Generate Narration

The TTS script prefers `voiceover.ssml` when present and falls back to `voiceover.md` for draft narration.

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
