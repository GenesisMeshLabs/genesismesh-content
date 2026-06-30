"""Generate Azure Speech narration from a campaign's voiceover.md.

Usage:
    python videos/scripts/generate_tts.py portable-trust
    python videos/scripts/generate_tts.py use-cases/ai-agents

Required env values can be set in videos/scripts/.env:
    AZURE_SPEECH_KEY
    AZURE_SPEECH_ENDPOINT
    AZURE_SPEECH_VOICE
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGNS = ROOT / "campaigns"
ENV_FILE = Path(__file__).resolve().parent / ".env"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def campaign_dir(slug: str) -> Path:
    path = CAMPAIGNS / slug
    if not path.exists():
        matches = []
        for candidate in CAMPAIGNS.rglob("campaign.json"):
            try:
                campaign = json.loads(candidate.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if candidate.parent.name == slug or campaign.get("slug") == slug:
                matches.append(candidate.parent)
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            choices = "\n".join(str(match.relative_to(CAMPAIGNS)).replace("\\", "/") for match in matches)
            raise SystemExit(f"Campaign slug is ambiguous. Use one of:\n{choices}")
        raise SystemExit(f"Campaign not found: {path}")
    return path


def read_campaign(path: Path) -> dict:
    campaign_file = path / "campaign.json"
    if not campaign_file.exists():
        raise SystemExit(f"Missing campaign.json: {campaign_file}")
    return json.loads(campaign_file.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign", help="Campaign slug under campaigns/")
    parser.add_argument("--out", help="Optional output wav path")
    parser.add_argument("--voice", help="Override Azure voice for this render")
    args = parser.parse_args()

    load_env(ENV_FILE)

    path = campaign_dir(args.campaign)
    campaign = read_campaign(path)
    voiceover_file = path / "voiceover.md"
    if not voiceover_file.exists():
        raise SystemExit(f"Missing voiceover.md: {voiceover_file}")

    text = voiceover_file.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit(f"Voiceover is empty: {voiceover_file}")

    speech_key = (
        os.environ.get("AZURE_SPEECH_KEY")
        or os.environ.get("AZURE_TTS_KEY")
        or os.environ.get("SPEECH_KEY")
        or os.environ.get("speech_key")
    )
    endpoint_url = (
        os.environ.get("AZURE_SPEECH_ENDPOINT")
        or os.environ.get("AZURE_TTS_ENDPOINT")
        or os.environ.get("SPEECH_ENDPOINT")
        or os.environ.get("endpoint_url")
    )
    voice = (
        args.voice
        or campaign.get("voice")
        or os.environ.get("AZURE_SPEECH_VOICE")
        or os.environ.get("AZURE_TTS_VOICE")
        or os.environ.get("speech_voice")
        or "en-US-Adam:DragonHDLatestNeural"
    )

    if not speech_key or not endpoint_url:
        raise SystemExit("Set AZURE_SPEECH_KEY and AZURE_SPEECH_ENDPOINT in videos/scripts/.env")

    try:
        import azure.cognitiveservices.speech as speechsdk
    except ImportError as exc:
        raise SystemExit("Install Azure Speech SDK: python -m pip install azure-cognitiveservices-speech") from exc

    parsed = urlparse(endpoint_url)
    base_endpoint = f"{parsed.scheme}://{parsed.netloc}"

    out_path = Path(args.out) if args.out else path / "audio" / "narration.wav"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=base_endpoint)
    speech_config.speech_synthesis_voice_name = voice
    audio_config = speechsdk.audio.AudioOutputConfig(filename=str(out_path))
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized: {out_path}")
        return 0

    if result.reason == speechsdk.ResultReason.Canceled:
        details = result.cancellation_details
        print(f"Speech synthesis canceled: {details.reason}", file=sys.stderr)
        if details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {details.error_details}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
