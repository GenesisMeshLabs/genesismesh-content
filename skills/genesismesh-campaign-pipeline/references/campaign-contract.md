# Campaign Contract

## Folder Shape

Horizontal campaign:

```text
campaigns/NN-slug/
  article.md
  campaign.json
  youtube.md
  patreon.md
  voiceover.md
  voiceover.ssml
  audio/.gitkeep
```

Use case:

```text
campaigns/08-use-cases/NN-slug/
  article.md
  campaign.json
  youtube.md
  patreon.md
  voiceover.md
  voiceover.ssml
  audio/.gitkeep
```

## Stable Slugs

Horizontal stable slug:

```text
slug
```

Use-case stable slug:

```text
use-cases/slug
```

Generated filenames use slash-safe slugs:

```text
slug
use-cases-slug
```

## Path Rules

Horizontal relative paths from campaign folder:

```text
../../videos/thumbnails/<safe-slug>.png
../../videos/renders/<safe-slug>-revid-stock.mp4
../../shared/images/marketing/<image>.png
```

Use-case relative paths from campaign folder:

```text
../../../videos/thumbnails/<safe-slug>.png
../../../videos/renders/<safe-slug>-revid-stock.mp4
../../../shared/images/marketing/<image>.png
```

## Campaign JSON Fields

Required baseline:

```json
{
  "slug": "portable-trust",
  "title": "Portable Trust",
  "status": "draft",
  "audience": ["builders", "security", "enterprise"],
  "channels": ["website", "linkedin", "video", "article"],
  "primary_message": "",
  "call_to_action": "",
  "source_docs": [],
  "slogan": "Genesis Mesh: portable trust for sovereign systems.",
  "voice": "",
  "voice_role": "",
  "duration_seconds_per_image": 5,
  "images": [],
  "thumbnail": "../../videos/thumbnails/portable-trust.png",
  "output": "../../videos/renders/portable-trust-revid-stock.mp4",
  "publishing": {
    "youtube": {
      "video_id": "",
      "url": "",
      "title": "",
      "thumbnail": "../../videos/thumbnails/portable-trust.png",
      "thumbnail_text": "",
      "render": "../../videos/renders/portable-trust-revid-stock.mp4"
    },
    "patreon": {
      "url": "",
      "title": ""
    }
  }
}
```

## Messaging Guardrails

Prefer:

- portable trust
- sovereign systems
- recognition and revocation
- verifiable trust state
- protocol interoperability
- signed evidence
- independent operators

Avoid framing Genesis Mesh as only:

- an AI agent framework
- a marketplace
- a central identity provider
- a cloud vendor product
- a blockchain/reputation-score system
