# Evidence review: idea 11

Scope: Sovereign wire identity, unsigned metadata, signed genesis anchoring and operator review of root mismatch; no automatic agent/workload migration.

## Evidence snapshot and release status

Review date: 2026-11-04. Core source inspected at a54b2d81f205c9b0203158f846f7ad44dc677063. GitHub v1.9.1 is published; the independent reviewer resolved its annotated tag to this exact commit and confirmed PyPI genesis-mesh 1.9.1 publication. Source version, published package and live deployment are different observations. No package, binary, test, script or demo was executed during this article review.

The independently checked release/train metadata is in ../source-release-snapshot.json and ../source-review.md. The older standard's dated 1.8.1 matrix is historical, not the availability matrix used here.

## Surface inventory

| Surface | Current snapshot / availability | Relevance and boundary |
| --- | --- | --- |
| NA and Python reference / CLI | Core a54b2d81f205c9b0203158f846f7ad44dc677063; v1.9.1 GitHub/PyPI verified | The concrete reference flows and tests cited below. Source inspection, not live execution. |
| TypeScript SDK | 8154ca7ac459ffbcd22d35900ca72f8093165bfc; v1.9.1 GitHub/npm verified | A governed client per current SDK matrix. No TypeScript parity or operation-specific behavior is asserted in this article. |
| Rust SDK | b67c248717d5d99aca6f4dad320692f3f6c07c69; v1.9.1 GitHub assets/Git dependency, beta | No transfer of Python/example behavior to Rust is claimed. Not on crates.io. |
| .NET SDK | 241d99b7508b378ce7c613dfc0baeed7cc5df56c; v1.9.1 GitHub/NuGet verified | Governed client since 1.9.0 per current matrix. Old guide prose saying only TypeScript/Rust is stale; no parity assertion here. |
| Go SDK | ade949888eacd0ccc16126941427e1211f82aec8; v1.9.1 GitHub tag verified | Thin client/offline verifier per matrix; no governed-client parity claim. |
| Gateway | 2e6486ee6a6481adca1be3b9dae70a4ef32036f9; v1.9.1 GitHub binaries, beta | Separate implementation; not the Python peer runtime or NA decision service. No gateway behavior inferred here. |
| Edge | Rust repo v1.9.1 release assets, beta | Only relevant where propagation comparison mentions documented next-sync timing. No uniform fallback, clock, or revocation behavior claimed across clients. |
| PHP | Independent reviewer found source 0.56.0, no release/tag, Packagist 404 | Not a claimed released surface or demonstrated flow in this article. |
| Demos / conformance | Source procedures and tests; not executed | Test source means test-covered, not passed here. No performance, interoperability or hosted security result asserted. |

Current matrix: https://docs.genesismesh.org/sdk/index.html and pinned source https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/sdk/index.md. Registry observations were made by the independent source reviewer and are recorded in the common review, not inferred from matching version strings.

## Public access and examples

Canonical documentation pages were reached through the live documentation navigation, opened and compared with their relevant source content on 2026-11-04. Whole-page links are used; no guessed anchors. Root anonymously inspected https://genesismesh.org/ and https://mesh.genesismesh.org/. The website displayed 1.8.1, the console displayed 1.9.0 and Operational/Ready, while the source releases are 1.9.1. These are page-availability observations only. No article claims a hosted scenario succeeded. These anonymous page observations were recorded by the publication reviewer on 2026-11-04.

Reader procedures require a disposable source checkout and the development dependencies in the installation guide. Source-based test commands select actual inspected test files. Local demo commands are copied from the linked documentation. All are explicitly marked not executed. Failure outcomes are documented or asserted in inspected test source; they are not new runtime results.


## Exact claim ledger for the concise revision

Each entry quotes the final saved paragraph verbatim. Illustrative scenes are not deployment evidence. Source observations and releases remain as recorded above; no product test was executed during this shortening pass.

### C01

An inventory agent moves from a laptop to an edge machine, then to the cloud. In this illustrative case, its operator wants a new address without silently creating a new trust relationship.

Sources: Illustrative scenario; no factual deployment claim.

Classification: Illustrative operator scenario; no customer or deployment assertion.

### C02

The proposed [Agent Identity URI Scheme](https://arxiv.org/abs/2601.14567) studies this separation; Genesis Mesh does not claim to implement its `agent://` scheme.

Sources: S01

Classification: Primary research context only; no product guarantee or integration inferred.

### C03

In Genesis Mesh, a sovereign is an independently administered trust domain. Its Network Authority is the operator's service for membership credentials and trust material. The [identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) gives the domain a stable `sovereign_id`; its `endpoint` is only a reachability hint.

Sources: S02

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

### C04

The important artifact is the root-signed genesis block. A consumer starts with a trusted root key, verifies genesis, and compares the required trust fields returned by `GET /sovereign.json` with it. That identity document is unsigned: its descriptive fields cannot replace the cryptographic anchor. The [public route](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) exposes both documents.

Sources: S03

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

### C05

An address change therefore need not change the domain's identity. A root-key mismatch is different: it requires operator review, not silent acceptance because the name or URL looks familiar. The receiving system still decides whether a verified identity may access its resources.

Sources: S03

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

### C06

This is domain continuity, not automatic workload or private-key migration. The operator must secure key provisioning and retire old access paths. A node key and certificate are separate from the sovereign's root; the reference peer packages remain [internal, maintained for fixes without new features](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html).

Sources: S04

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

### C07

Use an authority you operate, its independently trusted root key and the [documented identity procedure](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html). Fetch `/sovereign.json` and `/genesis`, verify genesis and compare the required trust fields.

Sources: S02

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

### C08

An endpoint-only change should preserve the anchor. A changed root must trigger review, even if `sovereign_id` is unchanged. This documented procedure was not executed in this review.

Sources: S02

Classification: Previously inspected documentation and/or implementation; tests establish source coverage only. The paragraph states its operative limits.

## Inspected sources retained by this revision

- S01: https://arxiv.org/abs/2601.14567
- S02: https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html
- S03: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py
- S04: https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html

## Revision decision

The article was shortened at the user's request without new capability claims. Secondary tours and repeated explanation were removed. Exact article/Patreon parity is preserved. Publication states and covers are unchanged. Independent review of this concise revision is pending; repository publication is coordinated by the parent. No new Patreon or LinkedIn action is authorized by this record.
