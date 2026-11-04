# Evidence ledger: idea 23

Review date: 2026-11-04. Author: Codex draft researcher. Independent source review is recorded separately against final hashes. This is a source-review packet, not a product certification or a passing test report.

## Research scope

[PayOff: A Regulated Central Bank Digital Currency with Private Offline Payments](https://arxiv.org/abs/2408.06956) — 2024-08-13 arXiv v1.

The original abstract was inspected for the design and stated limitations. No performance figures, replication or reuse of the payment protocol is claimed.

## Revisions and availability

Core: `a54b2d81f205c9b0203158f846f7ad44dc677063`. TypeScript: `8154ca7ac459ffbcd22d35900ca72f8093165bfc`. Both are in the coordinated 1.9.1 source train. The [release snapshot](../source-release-snapshot.json) records actual GitHub release tags and assets.

The [independent registry review](../source-review.md) verifies PyPI genesis-mesh 1.9.1 (2026-11-04 08:59 UTC), npm genesis-mesh-sdk 1.9.1 (08:59 UTC), and NuGet genesismesh-sdk-dotnet 1.9.1 (09:46 UTC). No packages were installed or scenario tests run in this review.

The public website and trust demo were viewed without authentication on 2026-11-04. The demo reported runtime 1.9.0 while the release train is 1.9.1; articles assert interface availability only. The website's 1.8.1 label is stale. No Patreon publication date has been assigned to this new article.

## Material claims

### 23-1

Exact article wording: It can issue a signed `CapabilityGrant` for a registered bearer key, defined capabilities, a validity interval, a maximum number of uses and a closed parameter envelope.

Affected sections/assets: Grant issuance beta; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/grants.py#L266).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L242). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered; grant routes are beta. Evidence store, out-of-band records and grants must be enabled, with an authorized operator and registered executor key. Uses are not money.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 23-2

Exact article wording: A holder operating within a grant records a signed `GrantExecutionEvidence`.

Affected sections/assets: Record schema; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/grants.py#L383).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L336). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered. The outcome is the holder's signed report, not independent proof of physical state or settlement.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 23-3

Exact article wording: The admission rules include capability and envelope checks, budget, time-token ordering and validity, upload timing and known revocation.

Affected sections/assets: Admission checks; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/grants.py#L766).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L382). **Not executed** in this review.
- Scope, limitations and decision: Implemented and test-covered. use_problem assumes earlier signature, bearer, digest and chain-position checks. Some checks depend on available history. It is not described as a complete standalone verifier.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 23-4

Exact article wording: A disconnected holder cannot learn a revocation that happened after its last update.

Affected sections/assets: Offline limit; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/operations/grants.md).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L543). **Not executed** in this review.
- Scope, limitations and decision: Offline information limit supported by the operating guide. No universal fallback, tamper-proof clock or state, immediate revocation or payment double-spend prevention is claimed.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

### 23-5

Exact article wording: Assigning an order to admitted records is not distributed payment settlement.

Affected sections/assets: Domain boundary; article.md, identical patreon.md and corresponding bounded LinkedIn wording.

- Implementation: [inspected symbol or model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L366).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L436). **Not executed** in this review.
- Scope, limitations and decision: Explicit domain distinction: ordering admitted evidence does not settle money or undo an already performed action.
- Availability: underlying source is in the pinned 1.9.1 release train. Telecom, EV and payment adaptations remain illustrative, not implemented by this work. No complete SDK parity or live feature availability is asserted.

## Documentation and source comparison

- [Canonical guide](https://docs.genesismesh.org/examples/pre-issued-grants.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/pre-issued-grants.md). No guessed section anchors are used.
- [Canonical guide](https://docs.genesismesh.org/operations/grants.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/operations/grants.md). No guessed section anchors are used.

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

Grant routes are explicitly qualified as beta in the article and Patreon copy. The canonical [public contract](https://docs.genesismesh.org/reference/public-contract.html) was opened and checked on 2026-11-04. This classification does not establish production deployment or complete SDK parity.
