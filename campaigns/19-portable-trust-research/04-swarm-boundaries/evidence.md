# Evidence review: A swarm needs boundaries, not just coordination

Reviewed: 2026-11-05. Original campaign idea: 9. This packet covers the reviewed expansion of an already published article; its saved platform copy is verified below. Evidence level: current primary documentation, pinned implementation and test-source inspection. No product tests, examples, live actions or hardware exercises were run.

## Scope and current checks

The user authorized revision of the existing live post while retaining its title, URL, public audience and cover. The concrete deployment scenario remains illustrative. Genesis Mesh supplies authority and evidence mechanisms; the article does not claim a swarm scheduler, AgentNet integration, ready-made deployment connector, production federation proof or shipped cross-owner phone-approval experience.

The core head remains `a54b2d81f205c9b0203158f846f7ad44dc677063`. The core release and all six recorded source/release revisions were rechecked on 2026-11-05 and remained unchanged. Source head, published package/release and deployed runtime are separate observations. No test-execution or deployment claim follows from release availability.

Current reader documentation was reopened on 2026-11-05: delegation chains, the SDK overview/capability matrix, governed changes and the public contract. Boundary-policy, mediation and security pages were also inspected during the same-day campaign review. Direct code links remain pinned; living documentation links are not immutable snapshots.

## Material claims

Exact wording below is rendered Markdown, with link and code formatting removed. Each claim applies to article.md and identical patreon.md; the LinkedIn draft makes only narrower corresponding claims.

### Claim 9-1
- Exact wording / scope: The chain verifier checks linkage, signatures, capability containment and expiry ceilings.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603
- Verification and limits: Rendered Markdown wording. Capability equality is allowed. Expiry containment does not establish current root validity or current authorization.
- Review status: source-based independent revision review passed.

### Claim 9-2
- Exact wording / scope: The root agreement and the actual execution request still need their own verification.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390
- Verification and limits: Supplied-chain validation is distinct from current-use policy. No live graph revocation or alternate-path search is inferred.
- Review status: source-based independent revision review passed.

### Claim 9-3
- Exact wording / scope: The boundary-policy workflow lets an operator publish rules and obtain a signed BoundaryDecision for a request.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/services/boundary_policy.py
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_boundary_policy.py
- Verification and limits: Rendered wording. Current service code fetched on 2026-11-05. Executor binds trusted input facts and actual operation; no deployed phone-approval flow claimed.
- Review status: source-based independent revision review passed.

### Claim 9-4
- Exact wording / scope: A signed ExecutionMediationRequest references a stored decision and carries an invocation token and command.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/mediation.py#L24-L55
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py#L730-L864
- Verification and limits: Rendered wording. decision_id references the stored BoundaryDecision; the request does not embed that decision object.
- Review status: source-based independent revision review passed.

### Claim 9-5
- Exact wording / scope: The guard checks the authorization artifacts and command policy before mediated subprocess execution.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L126-L267
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py#L730-L864
- Verification and limits: Rendered wording. Advisory route permits bypass. Mandatory mode requires verified host/credential/network restrictions; no kernel or hardware attestation.
- Review status: source-based independent revision review passed.

### Claim 9-6
- Exact wording / scope: Its token-use counter is process-local and resets on restart.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py#L53-L111
- Verification and limits: Rendered wording. No durable or distributed invocation-budget guarantee.
- Review status: source-based independent revision review passed.

### Claim 9-7
- Exact wording / scope: The guard does not fetch newly recorded revocations; expiry and other local checks still apply.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py
- Verification and limits: Corrects the old absolute usable-until-expiry sentence: another local check may refuse earlier. Pinned code supplies the precise implementation reference.
- Review status: source-based independent revision review passed.

### Claim 9-8
- Exact wording / scope: In a supported governed integration, the controller obtains a decision, performs the permitted action and submits signed ExecutionEvidence.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/concepts/governed-changes.md
- Verification and limits: Rendered wording. The executor signs the report; the NA checks/links/keeps it. Collection requires relevant features; evidence store off by default. Signed payloads do not establish complete real-world truth.
- Review status: source-based independent revision review passed.

### Claim 9-9
- Exact wording / scope: The current capability matrix identifies TypeScript, Rust and .NET as governed clients; Go remains a verifier plus thin client.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/sdk/index.md
- Verification and limits: Rendered wording. Canonical matrix reopened on 2026-11-05. .NET governed support independently confirmed from v1.9.0 release; old concept/public-contract package prose lags that release. Shared version does not imply parity.
- Review status: source-based independent revision review passed.

### Claim 9-10
- Exact wording / scope: Expect a valid two-hop chain to verify and an attempt to widen capabilities to fail.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/delegation-chain-demo.py
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603
- Verification and limits: Documented source demo with controlled scenario clock, not executed in this review. Subsequent deployment handoff/outage/withdrawal checks are proposed integration work.
- Review status: source-based independent revision review passed.

## Research context

[AgentNet](https://arxiv.org/abs/2504.00587), v2 dated 2025-05-29, studies decentralized evolutionary coordination using changing agent graphs and task routing. Its abstract was reopened on 2026-11-05. The article uses it only as motivation for distributed coordination. Its task-performance, privacy, robustness and scalability results are not transferred to Genesis Mesh, and no integration is asserted.

## Surface and availability matrix

| Surface | Inspected revision / official release | Relevance and limitation |
|---|---|---|
| Python Network Authority, core library and CLI | `a54b2d81f205c9b0203158f846f7ad44dc677063`; [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) | NA policy/evidence service and documented source demo. Delegation/guard CLI and related artifacts are beta in the pinned contract. No standalone Python SDK parity inferred. |
| TypeScript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc`; [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) | Governed client according to current matrix; no universal feature parity asserted. |
| Rust SDK | `b67c248717d5d99aca6f4dad320692f3f6c07c69`; [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) | Governed client with distinct surface. Library and verifier/edge release artifacts do not prove a running deployment. |
| .NET | `241d99b7508b378ce7c613dfc0baeed7cc5df56c`; [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) | Governed client since [v1.9.0](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0), not future coverage. Current matrix and release supersede stale core scope prose. |
| Go | `ade949888eacd0ccc16126941427e1211f82aec8`; [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) | Verifier plus thin client; no governed-action/evidence-outbox wrapper parity. Raw authenticated routes are a different integration surface. |
| Gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9`; [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) | Separate gateway, not the GenesisGuard sidecar and not the deployment executor in this scenario. |
| Edge agent | Rust repository above; beta | Not used in this flow. No grant execution, reconnect, durable queue or fallback behavior is attributed to it. |
| PHP | Not part of the supported release train | Not used; no parity claim. |
| Public demo | Public UI previously verified; no scenario run | Linked only as a public entry point. UI availability does not prove the current source version is deployed or this workflow works end to end. |

The [current SDK matrix](https://docs.genesismesh.org/sdk/index.html) identifies TypeScript, Rust and .NET as governed clients. The [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) and [public-contract page](https://docs.genesismesh.org/reference/public-contract.html) retain older .NET package-scope prose. The newer matrix and .NET release are used for availability. The pinned [machine-readable contract](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/contract/public-surface.json), fetched on 2026-11-05, classifies `trust delegate`, `trust guard`, `DelegatedAgreementRecord` and `ExecutionMediationRequest` as beta.

## Reader check and limits

The source checkout and documented dependencies are prerequisites. The delegation demo supplies example records/keys and a controlled scenario clock. Expected: valid two-hop chain accepted; capability expansion refused. Its manual flow requires a dual-signed root, operator keys and recognition-graph exports. Root verification and current-use authorization remain separate.

The proposed harmless-callback denial test, staging/production comparison and withdrawal-between-assignment-and-execution test were not performed. They are requirements to check in a deployment integration, not reported product successes. No direct deployment command or external side effect was executed.

## Revision decisions

- Replaced broad “capability and validity subsets” wording with source-accurate capability containment and expiry ceilings.
- Marked delegation and GenesisGuard as beta.
- Replaced “a revoked token remains usable until expiry” with the precise no-new-revocation-fetch limit while retaining other local checks.
- Replaced vague planned-client-coverage language with the current governed-client matrix.
- Added inline canonical guides and a final Further reading section; pinned code/test citations remain distinct.
- Preserved the existing title, public URL, audience, published date, identifiers and cover. The authorized live update was saved and verified below.
- Independent review of this expanded article, LinkedIn draft and exact claim ledger passed.

## Patreon synchronization

Verified 2026-11-05: the approved revision was saved to the existing [Patreon post](https://www.patreon.com/GenesisMeshLabs/posts/swarm-needs-not-174297241) and reopened. Its rendered body and all 19 links matched the approved source; the cover and public access were preserved. The post remains public and published at its existing URL; its recorded original publication date remains 2026-11-04. LinkedIn remains an unpublished draft.

Approved Markdown SHA-256: `a8ce405afb2d7117bdab6fa0027cd19eae6f8bd149af391bc6bb86e8231f5608`. Rendered-body SHA-256 after collapsing whitespace: `765bca6d18a2bc16994dcf05b8b2c49d94acbf16ceb642d5b317e2056c05e37d`. This is verification of the saved publication copy, not execution of a product example or proof that a scheduled post has been released.
