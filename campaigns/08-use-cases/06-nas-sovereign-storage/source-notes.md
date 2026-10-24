# NAS campaign: editorial sources and integration status

Reviewed against core version 1.8.0, commit `9a923c4a259e0dbf5be674dc57ddce35aa192f74`, on 2026-10-24.

Status: article draft for review. This campaign describes a proposed NAS integration, not a tested deployment or a supported NAS package.

## Sources

Paths below are relative to the upstream `genesismesh` repository, following this content repository's `source_docs` convention.

| Source | Supports |
|---|---|
| `VISION.md` | Portable trust and operator-owned authority |
| `docs/development/strategy.md` | Core positioning; a VPN or application can be built around the trust primitives |
| `docs/concepts/use-cases.md` | Sovereign hosting; connectivity alone may be served by a simpler tool |
| `docs/concepts/routing.md` | Authenticated application messages and multi-hop routing, not transparent file-protocol tunnelling |
| `docs/examples/attestation-backed-evaluation.md` | Engine-bound signed claims; caller authentication remains the relying application's job |
| `docs/examples/declarative-boundary-policy.md` | Gate semantics, signed policy bindings, mandatory evaluation settings and selector coverage limits |
| `genesis_mesh/trust/context/engine.py` | Signed boundary decisions and default decision lifetime |
| `genesis_mesh/gossip/crl_gossip.py` | Periodic revocation dissemination; no universal instantaneous cutoff guarantee |
| `docs/concepts/rust-gateway.md` | Existing gateway verifies trust and exposes scoped authority services; it is not a NAS file proxy |
| `ops/go-to-market.md` | Distinguish protocol proof from pain relief delivered by an enforcing integration |

## Claims to preserve

- NAS-facing enforcement is proposed. Collection identifiers and read/upload capabilities are application design examples.
- The relying service authenticates the caller, maps identities to requests, enforces the decision and retains native storage permissions.
- A policy binding records which policies the authority applied. It does not independently prove that none was omitted or that a file operation ran.
- Revocation enforcement depends on current state, decision validity and session handling. Previously downloaded data cannot be recalled.
- Connectivity, internet exposure, NAT traversal and transfer throughput require a separately specified and tested deployment.
- No native NAS package, phone client, transparent SMB/WebDAV tunnel or vendor compatibility is claimed.

## First documentation proof

Target after an integration works: `genesismesh/docs/examples/nas-access-governance.md`.

- Choose one host and a test dataset; document versions and the enforcement service.
- Map one read capability and a signed collection claim to a specific storage operation.
- Authenticate the real caller and prevent paths that bypass the enforcement service.
- Require policy-aware evaluation and cover mandatory request fields with a capability-selected policy.
- Exercise allow, wrong collection, revoked identity and stale/unavailable authority state.
- Measure propagation and document existing-session behavior, expiry and recovery.
- Document reachable endpoints and the actual connectivity path.
- Separate authorization evidence from execution evidence.

## Production handoff

`article.md` is the review source. `patreon.md` is its editorial publication draft.

The narration and SSML remain scaffold placeholders; YouTube metadata remains pending video production. Voice selection, narration and video follow article approval. No publication or provider render has been performed.

The cover uses the same deterministic generator as the newer article series: `videos/scripts/generate_series_thumbnails.py`. Its `storage` group uses the brand lime accent, the shared logo and a NAS-and-key motif. Run the script with `08-use-cases/06-nas-sovereign-storage` to regenerate the campaign's `thumbnail.png`; copy that output to `videos/thumbnails/use-cases-nas-sovereign-storage.png` for the canonical video upload asset.
