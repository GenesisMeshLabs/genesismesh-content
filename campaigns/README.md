# Campaigns

Campaign content must follow the top-level `MESSAGING.md` guardrails.

Status: 01 to 10 are published on Patreon, and 01 to 08 also have YouTube videos. From 11 onward, each campaign is published on Patreon first, with YouTube later.

The folder names are ordered for GitHub browsing, while scripts use the stable `slug` in each `campaign.json`.

## Horizontal Campaigns

These are the main Genesis Mesh narratives.

| Folder | Slug | Role |
|---|---|---|
| `01-why-genesismesh` | `why-genesismesh` | Problem framing: systems can connect, but cannot carry trust across boundaries. |
| `02-portable-trust` | `portable-trust` | Core thesis: trust should move between independent systems without one central owner. |
| `03-sovereign-systems` | `sovereign-systems` | Operator control: keys, policy, recognition, revocation, and trust decisions stay sovereign. |
| `04-recognition-and-revocation` | `recognition-and-revocation` | Trust lifecycle: it is not enough to trust once; you must cut trust off with proof. |
| `05-auditable-trust-state` | `auditable-trust-state` | Evidence: every trust decision should be verifiable later. |
| `06-protocol-interoperability` | `protocol-interoperability` | Protocol proof: Genesis Mesh is not tied to one runtime or language. |
| `07-trust-api-and-sdks` | `trust-api-and-sdks` | Developer entry: stable Trust API and SDKs make the primitives usable. |

## Use Cases

These come after the horizontal campaigns.

| Folder | Slug | Role |
|---|---|---|
| `08-use-cases/01-ai-agents` | `use-cases/ai-agents` | Agents consume trust primitives; Genesis Mesh is not an agent framework. |
| `08-use-cases/02-edge-infrastructure` | `use-cases/edge-infrastructure` | Distributed infrastructure needs identity, revocation, and trust paths. |
| `08-use-cases/03-supply-chain-trust` | `use-cases/supply-chain-trust` | Maintainer attestations, release gates, and revocation after compromise. |
| `08-use-cases/04-enterprise-integration` | `use-cases/enterprise-integration` | Enterprises keep local authority while recognizing external trust. |
| `08-use-cases/05-data-access-governance` | `use-cases/data-access-governance` | Data access carries intent, policy, evidence, and verification. |

## Published Posts

These were published on Patreon before they had campaign folders. `article.md` keeps the published text.

| Folder | Published | Role |
|---|---|---|
| `09-portable-trust-for-peer-to-peer` | [Patreon, 2026-07-02](https://www.patreon.com/GenesisMeshLabs/posts/portable-trust-162655968) | Peer-to-peer systems decentralize connectivity, not trust; portable trust fills that gap. |
| `10-genesis-mesh-did-not-start-with-genesis-mesh` | [Patreon, 2026-08-27](https://www.patreon.com/GenesisMeshLabs/posts/genesis-mesh-did-167836569) | Origins: from the Intelligent Agents Network PoC to the trust and authority problem. |

## What Changed Since v0.53

The series covering v0.53 to v1.7, in publishing order. Each numbered group can become a YouTube playlist. These are published on Patreon first; each folder has `article.md`, `patreon.md` and `thumbnail.png`.

| Folder | Title | Covers | Role |
|---|---|---|---|
| `11-after-the-signature` | After the Signature | v0.53 to v1.7 | Series opener: governed change is portable trust carried through time. |
| `12-policy-and-evidence/01-policy-you-can-read` | Policy You Can Read | v0.58 | Signed, versioned policy; decisions name the rules behind them. |
| `12-policy-and-evidence/02-allowed-is-not-done` | Allowed Is Not Done | v0.59 | Decisions and their execution in one history per resource. |
| `13-running-it-for-real/01-a-front-door-not-an-authority` | A Front Door, Not an Authority | v0.56 to v0.64 | The gateway verifies, scopes and forwards without becoming an authority. |
| `13-running-it-for-real/02-watch-trust-cross-a-boundary` | Watch Trust Cross a Boundary | v0.65 | The live demo across two independently signed sovereigns. |
| `13-running-it-for-real/03-staying-up-without-giving-up-the-keys` | Staying Up Without Giving Up the Keys | v0.60 | Optional high availability over a shared database. |
| `13-running-it-for-real/04-a-contract-that-holds` | A Contract That Holds | v0.62 to v1.0 | A public contract that tests enforce for the 1.x line. |
| `13-running-it-for-real/05-verify-what-you-run` | Verify What You Run | v1.1 | Signed images and a local governed authority. |
| `14-governed-changes/01-lost-misread-or-erased` | Lost, Misread or Erased | v1.2 | Evidence outbox, strict verifiers and store anchors. |
| `14-governed-changes/02-changes-that-happen-anyway` | Changes That Happen Anyway | v1.3 | Observations, judgments and break-glass. |
| `14-governed-changes/03-rotate-forward-never-back` | Rotate Forward, Never Back | v1.4 | Remediation by rotating forward, and second-person reviews. |
| `14-governed-changes/04-an-audit-that-doesnt-trust-the-audited` | An Audit That Doesn't Trust the Audited | v1.5 | Audit packs, completeness and an independent verifier. |
| `14-governed-changes/05-new-key-same-past` | New Key, Same Past | v1.5 | Key succession and its limits. |
| `15-trust-at-the-edge/01-permission-before-the-link-goes-down` | Permission Before the Link Goes Down | v1.6 | Pre-issued grants for offline action. |
| `15-trust-at-the-edge/02-the-device-asks-first` | The Device Asks First | v1.7 | The edge agent. |
| `16-proof-not-promises/01-five-languages-one-verdict` | Five Languages, One Verdict | v0.61 to v1.3 | Implementations judge each other's records. |
| `16-proof-not-promises/02-what-a-proof-proves` | What a Proof Proves | v0.53.1, v0.61.1 | Formal models, their scope and a falsified property. |
| `16-proof-not-promises/03-finding-our-own-flaws-first` | Finding Our Own Flaws First | v1.0.2 to v1.7 | Published flaws and fixes, and the review process. |
| `16-proof-not-promises/04-the-rules-cant-live-in-one-head` | The Rules Can't Live in One Head | after v1.7 | The engineering gates that keep regressions out. |
