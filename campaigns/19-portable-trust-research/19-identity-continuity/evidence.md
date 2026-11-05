# Evidence ledger: idea 19

Review date: 2026-11-05. Author: Codex draft researcher. Independent source review is recorded separately against final hashes. This is a source-review packet, not a product certification or a passing test report.

## Research scope

[AgentDID: Trustless Identity Authentication for AI Agents](https://arxiv.org/abs/2604.25189) — 2026-04-28, arXiv v1.

The original paper's abstract and metadata were inspected. The authors describe challenge-response state verification. The article does not claim replication, performance parity, AgentDID interoperability or independent measurement by Genesis Mesh.

## Revisions and availability

Core: `a54b2d81f205c9b0203158f846f7ad44dc677063`. TypeScript: `8154ca7ac459ffbcd22d35900ca72f8093165bfc`. Both are in the coordinated 1.9.1 source train. The [release snapshot](../source-release-snapshot.json) records actual GitHub release tags and assets.

The [independent registry review](../source-review.md) verifies PyPI genesis-mesh 1.9.1 (2026-11-04 08:59 UTC), npm genesis-mesh-sdk 1.9.1 (08:59 UTC), and NuGet genesismesh-sdk-dotnet 1.9.1 (09:46 UTC). No packages were installed or scenario tests run in this review.

The public website and trust demo were viewed without authentication on 2026-11-04. The demo reported runtime 1.9.0 while the release train is 1.9.1; articles assert interface availability only. The website's 1.8.1 label is stale. No Patreon publication date has been assigned to this new article.

## Material claims

### 19-1

Exact article wording: Genesis Mesh's reference implementation provides a narrower mechanism: a signed `ModelAttestation`.

Affected sections/assets: Record fields and construction; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/attestation.py#L47).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_verifiable_logic_attestation.py#L135). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered. The record contains declared configuration. Hashing does not establish the actual runtime or protect predictable inputs against guessing.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 19-2

Exact article wording: The `verify_model_attestation` function checks the signature and expiry, then compares the declared model, prompt hash and tool hash with the configured allowlists.

Affected sections/assets: Declaration checks; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L86).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_verifiable_logic_attestation.py#L187). **Not executed** in this review.
- Scope, limitations and decision: Implemented. Empty allowlists permit any value. The model version tag is recorded but not allowlisted. require_bound_token checks presence rather than equality with an expected invocation token. All these limits appear in the public article.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 19-3

Exact article wording: A `LogicAttestationGate` can add that check to a local boundary evaluation.

Affected sections/assets: Opt-in Python integration; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L143).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_verifiable_logic_attestation.py#L370). **Not executed** in this review.
- Scope, limitations and decision: Implemented, opt-in Python gate. No automatic gateway or SDK parity, hardware measurement or remote-attestation guarantee is claimed.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 19-4

Exact article wording: The relying application still authenticates the caller and controls execution.

Affected sections/assets: Identity-to-authorization boundary; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/context.py#L44).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_attestation_boundary.py#L233). **Not executed** in this review.
- Scope, limitations and decision: Bounded to documented attestation-backed evaluation. Subject equality is not caller authentication; the relying application owns that boundary.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 19-5

Exact article wording: A valid result says the signed declaration satisfied the configured checks.

- Implementation basis: [inspected source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L86).
- Test basis: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_verifiable_logic_attestation.py#L187); not executed.
- Scope and inference: The update-review section is an illustrative operator procedure derived from the actual verifier checks. It does not claim measurement, deployment enforcement or automatic refusal of stale declarations outside the consuming application.
- Affected assets: article.md, identical Patreon copy and the bounded LinkedIn summary. Expanded wording awaits independent review.

## Documentation and source comparison

- [Canonical guide](https://docs.genesismesh.org/examples/verifiable-logic-attestation.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/verifiable-logic-attestation.md). No guessed section anchors are used.
- [Canonical guide](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/attestation-backed-evaluation.md). No guessed section anchors are used.

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

Reader URL inventory: campaign.json source_docs and the article citations. Final asset hashes and release gates are recorded in review.md. Recheck release/deployment evidence before any later material revision or publication claim.


## Final beta qualification

Logic-attestation functions are explicitly qualified as beta in the article and Patreon copy. The canonical [public contract](https://docs.genesismesh.org/reference/public-contract.html) was opened and checked on 2026-11-04. This classification does not establish production deployment or complete SDK parity.

## Expanded revision and current-source check

On 2026-11-05, the six current implementation heads and latest GitHub releases were rechecked: core, TypeScript, Rust, .NET, Go and gateway retain the exact revisions in the matrix above, with latest tags v1.9.1. Primary research abstracts were reopened. Canonical public-contract, logic-attestation, recognition, governed-action, pre-issued-grant, selective-disclosure, attestation-backed-evaluation, declarative-policy, installation and SDK-overview pages were opened and their relevant content inspected. The public contract still classifies logic-attestation and selective-disclosure functions, and grant routes, as beta.

Targeted pinned verifier/source reads reconfirmed logic-attestation limits, direct treaty recognition, governedAction callback boundaries and unsalted deterministic capability leaf hashing. PyPI currently reports 1.9.1. The web tool could not reopen npm/NuGet JSON endpoints or the website/demo; their earlier dated observations above are retained rather than represented as new successful checks. The repository-wide reviewer is refreshing shared availability evidence.

The expanded article follows the user's request for roughly 900 words, canonical documentation links throughout and a final Further reading section. New scenario detail is expressly illustrative integration guidance, not a new product capability. No package, test, demo, payment or deployment was executed. Independent source-based technical and editorial review of the expanded wording passed; final asset hashes are recorded in review.md.
