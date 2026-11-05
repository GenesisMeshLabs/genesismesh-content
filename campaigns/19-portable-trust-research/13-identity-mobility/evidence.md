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

## Expanded revision verification - 2026-11-05

On 2026-11-05 the author reopened the canonical sovereign identity specification, security model and dormant-packages decision and compared their substantive requirements with the retained pinned public route and peer identity source. The independent reviewer rechecked GitHub: core main remains a54b2d81f205c9b0203158f846f7ad44dc677063 and latest release remains v1.9.1, published 2026-11-04. The research abstract was reopened. The page describes required trust fields, not all descriptive fields, as the genesis comparison boundary.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

An inventory agent starts on an engineer's laptop, moves to a warehouse edge machine, then runs in a cloud account. In this illustrative case, the operator wants the inventory service to recognize the same administrative domain after each move. A new address should not silently create a new trust relationship, and a familiar name should not excuse an unfamiliar key.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

That problem motivates the proposed [Agent Identity URI Scheme](https://arxiv.org/abs/2601.14567), which separates naming from network location. Genesis Mesh does not claim to implement its `agent://` scheme. Its relevant mechanism is a more specific one: a sovereign domain publishes identity material that another operator can check against a cryptographic anchor.

Evidence: https://arxiv.org/abs/2601.14567

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

In Genesis Mesh, a sovereign is an independently administered trust domain. Its Network Authority is the operator's online service for membership credentials and trust material. The [sovereign identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) distinguishes the domain's stable `sovereign_id` from its public `endpoint`. The endpoint helps another system find the service; it does not establish that the service deserves trust.

Evidence: https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

For the inventory operator, this means keeping two questions separate. Where can the authority be reached today? Which authority does the receiving service recognize? Updating a hostname can answer the first without answering the second. A successful connection to the new machine is useful operational evidence, but it is not proof that the machine represents the same domain.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

The concrete documents are available through `GET /sovereign.json` and `GET /genesis`. The [public route implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) exposes the identity metadata and genesis block. The former includes the sovereign and network names, root public key, genesis Network Authority key, current signing-key information and advertised endpoint.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C08

Those fields do not all carry the same authority. The identity document is unsigned. The [specification's verification requirements](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) tell consumers to compare the required trust fields with the root-signed genesis block: `sovereign_id`, `network_name`, `root_public_key` and `network_authority.public_key`. Descriptive metadata and the endpoint cannot replace that check.

Evidence: https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

The consumer needs a trusted root key obtained through its own onboarding or recognition process. Downloading a root key from the same untrusted endpoint being evaluated is not independent confirmation. In the warehouse example, the receiving inventory service should already know which domain it intends to recognize and retain the trust material needed to check that claim.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

The [identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) also separates key roles. The root anchors the domain, the Network Authority signs operational trust material, operator keys authorize administrative work, and node keys identify individual participants. Keeping those roles separate makes the migration discussion precise: moving an application is not the same operation as replacing its domain root or rotating an authority's signing key.

Evidence: https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

The public identity route reports both the original authority key and current signing-key information. That distinction matters after a succession. The [route source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) also advertises the key-history endpoint. A reader should follow the documented history verification rather than treating whichever key appears in a fresh response as trusted merely because it is newer.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C13

Consider two migration outcomes. In the first, the endpoint changes while the required trust fields still match the verified genesis material. The operator can update reachability without inventing a new domain identity. In the second, the replacement server presents the old name with a different root. That is a trust change requiring review, even when the server answers correctly and the application appears healthy.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

This mechanism establishes domain continuity; it does not transfer a running process, copy private keys safely or disable the old host. Those are migration responsibilities. The operator must decide how the new workload receives credentials, which old access paths are retired and how to recover if both instances remain active. No identity document answers those deployment questions on its own.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

A node's credential also has its own lifecycle. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes certificate signatures, validity, network, revocation state and transport-key binding checks. A stable sovereign identifier does not make a stale or revoked node credential acceptable, and a valid node credential does not decide whether a particular inventory operation is allowed.

Evidence: https://docs.genesismesh.org/concepts/security-model.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C17

The receiving service remains the authority for its resource. It must consume the verified identity and apply its own access rules before returning inventory data. The reference peer packages are [internal and maintained for fixes without new features](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html); this article makes no claim of universal workload mobility across runtimes.

Evidence: https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

For the inventory rollout, a useful acceptance record would therefore identify the expected sovereign, the verified root, the new endpoint and the credential the new node presents. The receiving operator can review those items independently of the application's functional test. A successful stock lookup demonstrates that a request worked; it does not replace the trust checks that made the request acceptable.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C20

Use a disposable authority you operate, an independently trusted copy of its root public key and the [documented identity verification procedure](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html). Fetch `/sovereign.json` and `/genesis`, verify the root signature and compare the four required trust fields.

Evidence: https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C21

Inspect an endpoint-only change separately from a root mismatch. The first should preserve the verified domain anchor. The second must trigger review rather than automatic acceptance of the familiar name. Keep private keys out of public test artifacts and record which root the consumer expected. This documented procedure was not executed in this review.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2601.14567
- https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py
- https://docs.genesismesh.org/concepts/security-model.html
- https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
