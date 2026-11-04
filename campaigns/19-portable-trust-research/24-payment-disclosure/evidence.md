# Evidence ledger: idea 24

Review date: 2026-11-04. Author: Codex draft researcher. Independent source review is recorded separately against final hashes. This is a source-review packet, not a product certification or a passing test report.

## Research scope

[Offline Digital Euro: a Minimum Viable CBDC using Groth-Sahai proofs](https://arxiv.org/abs/2407.13776) — 2024-07-01 arXiv v1.

The original abstract was inspected. The proposed protocol and initial implementation are separated from Genesis Mesh. The article makes no current central-bank deployment, regulatory or policy assertion.

## Revisions and availability

Core: `a54b2d81f205c9b0203158f846f7ad44dc677063`. TypeScript: `8154ca7ac459ffbcd22d35900ca72f8093165bfc`. Both are in the coordinated 1.9.1 source train. The [release snapshot](../source-release-snapshot.json) records actual GitHub release tags and assets.

The [independent registry review](../source-review.md) verifies PyPI genesis-mesh 1.9.1 (2026-11-04 08:59 UTC), npm genesis-mesh-sdk 1.9.1 (08:59 UTC), and NuGet genesismesh-sdk-dotnet 1.9.1 (09:46 UTC). No packages were installed or scenario tests run in this review.

The public website and trust demo were viewed without authentication on 2026-11-04. The demo reported runtime 1.9.0 while the release train is 1.9.1; articles assert interface availability only. The website's 1.8.1 label is stale. No Patreon publication date has been assigned to this new article.

## Material claims

### 24-1

Exact article wording: The verifier checks the commitment's signature, the revealed capability's leaf hash and the Merkle path back to the committed root.

Affected sections/assets: Merkle membership; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L219).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py#L256). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered Merkle membership. No formal zero-knowledge, holder authentication, settlement or balance guarantee is claimed.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 24-2

Exact article wording: The commitment schema includes `agreement_id`, `issuer_sovereign_id`, `capability_count` and a timestamp. The proof includes a prover identifier.

Affected sections/assets: Actual disclosure; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py#L20).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py). **Not executed** in this review.
- Scope, limitations and decision: Actual schema inspected. This corrects the walkthrough's broad wording about hiding the agreement identifier. Public prose explicitly says these identifiers remain visible.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 24-3

Exact article wording: Genesis Mesh's `SelectiveDisclosureGate` checks two important relationships after proof verification: the commitment's agreement must match the request's agreement, and the revealed capability must match the requested capability.

Affected sections/assets: Request binding; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L308).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered local gate. Trusted keys, current permission and payment replay protection are outside this limited claim.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 24-4

Exact article wording: For its configurable policy gates, `disclose_input` defaults to false: the gate's recorded input describes presence and type rather than copying the raw value.

Affected sections/assets: Input minimization; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/boundary_policy.py#L106).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_boundary_policy.py#L685). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered. The input-recording code is https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/registry.py#L183 . It does not hide request facts from the authority or govern every other log.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 24-5

Exact article wording: The scheme uses deterministic hashes.

Affected sections/assets: Information limit; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L94).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py#L136). **Not executed** in this review.
- Scope, limitations and decision: Implementation inspected. The privacy limitation is an inference: predictable values and visible identifiers prevent treating absence of plaintext as proof against guessing. No exploitation test is claimed.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

## Documentation and source comparison

- [Canonical guide](https://docs.genesismesh.org/examples/selective-disclosure.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/selective-disclosure.md). No guessed section anchors are used.
- [Canonical guide](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/declarative-boundary-policy.md). No guessed section anchors are used.

Known drift: the current SDK overview documents .NET governed-client support from 1.9.0, while some older concept/example/public-contract narrative still says it only verifies. The article avoids that stale statement. The selective-disclosure introduction overstates identifier privacy; idea 24 follows the actual record models. Logic-attestation wording is limited to declared configuration, with no measured-runtime claim.

## Relevant surface inventory

| Surface | Revision and availability | Relevance and limits |
|---|---|---|
| Python core / Network Authority | a54b2d81f205c9b0203158f846f7ad44dc677063; PyPI 1.9.1 | Ledger models, verification and policy code inspected. HTTP policy evaluation runs at the authority. Grant and disclosure routes are beta. |
| Python CLI / local examples | Same core revision; Python 3.12+ in manifest and installation guide | Documented commands linked, but examples not executed. Local gate examples do not establish automatic distributed enforcement. |
| TypeScript | 8154ca7ac459ffbcd22d35900ca72f8093165bfc; npm 1.9.1 | Governed-action code and tests inspected for ideas 21/22. The callback and evidence stages remain separate. |
| Rust SDK | b67c248717d5d99aca6f4dad320692f3f6c07c69; GitHub 1.9.1 | Current SDK overview describes a governed client. These articles do not claim an independently verified Rust payment integration or identical fallback behavior. |
| .NET | 241d99b7508b378ce7c613dfc0baeed7cc5df56c; NuGet 1.9.1 | Current overview documents governed-client support from 1.9.0. Broader code paths are not asserted or tested here. |
| Go | ade949888eacd0ccc16126941427e1211f82aec8; GitHub 1.9.1 | Verifier plus thin client in current overview. No native governed callback or grant-holder parity assumed. |
| PHP source | c346d1ece0111b210006049d772fb39c3833e370; source 0.56.0 | Independent review found no GitHub release/tag or Packagist package. No PHP availability claim; not used in these flows. |
| Gateway | 2e6486ee6a6481adca1be3b9dae70a4ef32036f9; GitHub 1.9.1 binaries | Neither policy authority nor application executor. No routing/proxy behavior asserted in these articles. |
| Edge binary | Rust repository 1.9.1 assets; beta | Relevant deployment possibility for idea 23 only. No specific automatic fallback or payment-wallet behavior claimed. |
| Public demo | Browser-observed runtime 1.9.0 | Available trust UI only. No agent-configuration, telecom, EV, payment or privacy scenario execution claimed. |

SDK matrix: [canonical overview](https://docs.genesismesh.org/sdk/index.html), with [pinned source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/sdk/index.md). Contract: [pinned public contract](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/reference/public-contract.md). Beta/stability classification is distinct from dated narrative about SDK coverage.

## Observed verification and reader procedure

Read-only GitHub source fetches and primary paper/documentation reads were performed. Fields, functions and test assertions were inspected. No product runtime, payment operation or publication was mutated by this author. All application scenes are explicitly illustrative.

The reader procedure uses documented commands, prerequisites, expected acceptance and refusal cases, and an explicit statement that it was not executed in this review. The article contains no financial or legal recommendation or regulatory-compliance claim.

Reader URL inventory: links.json. Final hashes and release gates: review.md and hashes.json. Recheck release/deployment evidence before any later material revision or publication claim.


## Final beta qualification

Selective-disclosure functions are explicitly qualified as beta in the article and Patreon copy; the concluding privacy-property sentence uses clear comma punctuation. The canonical [public contract](https://docs.genesismesh.org/reference/public-contract.html) was opened and checked on 2026-11-04. This classification does not establish production deployment or complete SDK parity.
