# Evidence ledger: idea 22

Review date: 2026-11-04. Author: Codex draft researcher. Independent source review is recorded separately against final hashes. This is a source-review packet, not a product certification or a passing test report.

## Research scope

[A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) — 2026-08-30 arXiv v1.

The original abstract and metadata were inspected. Findings about models and implementation witnesses remain the authors' results. No universal vulnerability or automatic Genesis Mesh fix is claimed.

## Revisions and availability

Core: `a54b2d81f205c9b0203158f846f7ad44dc677063`. TypeScript: `8154ca7ac459ffbcd22d35900ca72f8093165bfc`. Both are in the coordinated 1.9.1 source train. The [release snapshot](../source-release-snapshot.json) records actual GitHub release tags and assets.

The [independent registry review](../source-review.md) verifies PyPI genesis-mesh 1.9.1 (2026-11-04 08:59 UTC), npm genesis-mesh-sdk 1.9.1 (08:59 UTC), and NuGet genesismesh-sdk-dotnet 1.9.1 (09:46 UTC). No packages were installed or scenario tests run in this review.

The public website and trust demo were viewed without authentication on 2026-11-04. The demo reported runtime 1.9.0 while the release train is 1.9.1; articles assert interface availability only. The website's 1.8.1 label is stale. No Patreon publication date has been assigned to this new article.

## Material claims

Concise revision: each quotation below appears in the revised article. The same claims apply to the identical Patreon copy; LinkedIn uses a narrower summary. Existing dated source and release checks remain the baseline. No product examples or tests were executed.

### 22-1

Exact article wording: Its signed `BoundaryDecision` can contain a `PolicyBinding` identifying policy versions, gate outcomes and `context_digest`, the hash of the canonical request context.

- Implementation: [inspected source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/boundary_policy.py#L225).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_boundary_policy.py#L603); not executed.
- Scope, limits and authority boundary: Policy-aware evaluation produces this binding. ContextRecord canonical JSON is hashed with SHA-256; the legacy decide route does not carry it. Merchant and monetary fields are proposed application parameters.
- Evidence level: source-inspected implementation and test assertions; no runtime result is claimed. The relevant release and surface matrix below controls availability, not the illustrative application.

### 22-2

Exact article wording: A verified denial prevents the callback.

- Implementation: [inspected source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L360).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts); not executed.
- Scope, limits and authority boundary: Ordinary governedAction path verifies decision, expected policies and applicable attestation, compares context identifiers and rechecks expiry after resource history. No fallback or universal SDK claim.
- Evidence level: source-inspected implementation and test assertions; no runtime result is claimed. The relevant release and surface matrix below controls availability, not the illustrative application.

### 22-3

Exact article wording: The helper does not automatically compare every purchase field or recompute `context_digest`.

- Implementation: [inspected source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L426).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts); not executed.
- Scope, limits and authority boundary: Consumer-supplied callback owns execution arguments. Freezing and comparing purchase data, checking relevant signed binding and rejecting changed terms are proposed adapter requirements. This is not an implemented payment integration.
- Evidence level: source-inspected implementation and test assertions; no runtime result is claimed. The relevant release and surface matrix below controls availability, not the illustrative application.

### 22-4

Exact article wording: Evidence delivery and the payment operation remain separate: repairing a failed evidence upload must not buy the service again.

- Implementation: [inspected source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L439).
- Tests: [inspected test source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts); not executed.
- Scope, limits and authority boundary: Design inference from separate action and evidence stages. Executor metadata reports observed outcome; provider idempotency, reconciliation and fulfillment require separate evidence.
- Evidence level: source-inspected implementation and test assertions; no runtime result is claimed. The relevant release and surface matrix below controls availability, not the illustrative application.

## Documentation and source comparison

- [Canonical guide](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/declarative-boundary-policy.md). No guessed section anchors are used.
- [Canonical guide](https://docs.genesismesh.org/sdk/typescript/governance.html) opened and its content inspected through the live site's links. [Pinned source document](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/sdk/typescript/governance.md). No guessed section anchors are used.

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

## Concise revision record

The article was shortened at the user's request on 2026-11-04. Secondary mechanisms and repeated caveats were removed; the retained claim quotations above supersede the earlier wording. Same-session primary-source, pinned implementation, canonical-documentation and release checks remain applicable. No new capability or deployment claim was added. The condensed revision awaits independent review against its updated hashes.
