# Evidence review: idea 15

Scope: Python reference delegation construction/verification and deterministic local guard. No automatic swarm integration, current revocation check in chain verification, general scope-dictionary attenuation or complete containment guarantee is claimed.

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


## Claim-level ledger

### R01 Research context

Exact article wording:

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) evaluates multi-agent systems under an untrusted-model assumption: confinement should survive a compromised model. Its broker and experimental results belong to that research. They are not a containment certification for Genesis Mesh or for an application using it.

Source: https://arxiv.org/abs/2609.00267
Evidence: original arXiv abstract/metadata inspected; research proposal/prototype, not Genesis Mesh implementation. No quoted performance numbers or prevention guarantees are transferred. Decision: retain bounded research hook.

### C01

Exact claim or sentence excerpt: For later hops, the delegator must be the previous hop's recipient.

Affected: article.md, identical patreon.md and derived linkedin.md.

Sources inspected:
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py

Evidence level: documented and/or implemented on the pinned reference source; test-covered only where the linked test asserts it. No test was executed. Availability: published core source/package as above; deployment unverified. Decision: retain with the article's stated scope and limits.

### C02

Exact claim or sentence excerpt: A deterministic guard checks a signed request, a stored decision, an invocation token and an explicit command allowlist before starting a process.

Affected: article.md, identical patreon.md and derived linkedin.md.

Sources inspected:
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py

Evidence level: documented and/or implemented on the pinned reference source; test-covered only where the linked test asserts it. No test was executed. Availability: published core source/package as above; deployment unverified. Decision: retain with the article's stated scope and limits.

## Detailed implementation and counterexamples

verify_delegation_chain enforces capabilities as set-subset, expiry ceiling, parent linkage/digest, root signatures and later-hop delegator continuity. It does not establish arbitrary resource/parameter restriction enforcement. Guard implementation and tests inspect request/decision/token signatures, bearer/agreement matching and command allowlist. Daemon stores invocation counts in memory, no durable count; docs specify revocation unseen until token expiry. Mandatory mediation additionally needs operator-enforced removal of bypass routes. The article uses 'capability subset/expiry ceiling', not the guide's overbroad strict/full validity-window claims.

## Direct implementation and test inventory

- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py
- Test source, inspected not executed: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py
- Test source, inspected not executed: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py

## Reader documentation verified

- https://docs.genesismesh.org/examples/delegation-chain.html
- https://docs.genesismesh.org/examples/process-level-mediation.html
- https://docs.genesismesh.org/installation.html

## Review limits

Independent reviewer must confirm final wording and derived assets. No product testing or live deployment certification is inferred. New Patreon publication and scheduling are not authorized. Current user instruction authorizes repository publication of the complete list after review; root coordinates that action. No publication performed by this author.

## Research version and compatibility check

Primary paper: https://arxiv.org/abs/2609.00267v1 ; revised/submitted 2026-08-31. Threat model, gap analysis and broker evaluation; no containment benchmark or prevention claim transferred.

Beta public surfaces: trust delegate create/cosign/verify and trust guard start/request/verify. Inspected contract: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/contract/public-surface.json . Canonical public contract opened: https://docs.genesismesh.org/reference/public-contract.html . Article explicitly identifies beta scope.
