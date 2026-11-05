# Evidence ledger - idea 5: A signed audit log does not tell the whole story

Review date: 2026-11-05. Intended publication date: not assigned. Authoring reviewer: Codex campaign author.
Core source inspected at a54b2d81f205c9b0203158f846f7ad44dc677063. Latest core release v1.9.1 confirmed from the GitHub release API. Release availability and source-head content are distinct; no hosted deployment or cross-language parity is inferred.
Observed work: public primary-source web reads; GitHub code/test/contract inspection; local editorial review. No Genesis Mesh test, demo, deployment, payment or side effect was executed. Test-covered means assertions read, not passing test execution.

## Source and release inventory

| Surface | Pinned revision | Availability / relevance |
|---|---|---|
| genesismesh | a54b2d81f205c9b0203158f846f7ad44dc677063 | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1); Python Network Authority / CLI and source demo are the bounded implementation in this article. CLI delegation, invocation tokens and guard are beta per contract; policy HTTP operations and audit commands have their own contract classifications. |
| sdk-typescript | 8154ca7ac459ffbcd22d35900ca72f8093165bfc | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1); Maintained separate TypeScript SDK; not used by these Python examples. No transport adapter, global budget or replay guarantee inferred. |
| sdk-go | ade949888eacd0ccc16126941427e1211f82aec8 | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1); Maintained separate SDK. No delegation, guard, policy-wrapper or audit-pack parity claim made; not used by reproduction procedure. |
| sdk-rust | b67c248717d5d99aca6f4dad320692f3f6c07c69 | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1); Separate implementation; release has verifier and edge binaries. Article 5 discusses the documented verifier, not all SDK parity. Other articles make no Rust integration claims. |
| sdk-dotnet | 241d99b7508b378ce7c613dfc0baeed7cc5df56c | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1); Maintained separate SDK; governed client shipped in 1.9.0 (independent release review). No parity assumed from stale core docs; not used by this example. |
| gateway | 2e6486ee6a6481adca1be3b9dae70a4ef32036f9 | GitHub release [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1); Separate beta gateway; not the authority or enforcement mechanism used by these examples. Not relevant to the local Python flow; no proxy or fallback behavior claimed. |
| Python core API | Same core revision | Delegation/token/guard symbols scoped to inspected implementation; CLI beta is stated publicly where relevant. |
| Edge agent | sdk-rust revision above | Not relevant: these articles do not claim disconnected grant execution or edge fallback. |
| PHP | Public-surface contract identifies unsupported old SDK | Not on release train; no PHP claim. |
| Public demo | Browser-read UI, runtime displayed 1.9.0 | Public browser observation verified access; no scenario run. Does not prove latest source deployed. |

The current public-surface contract is pinned at https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/contract/public-surface.json . Some old coverage prose lags current .NET releases, so it is not used to assert absence of new .NET functionality.

## Material claims

Exact wording below follows the expanded revision (rendered Markdown where code or links occur). Each item applies to article.md, identical patreon.md, and the narrower LinkedIn summary where relevant. All code and tests remain pinned to the unchanged core revision; test sources were inspected, not executed.

### Claim 5-1
- Exact wording / scope: The evidence store is off by default.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/operations/audit-verification-walkthrough.md
- Verification and limits: Canonical walkthrough reopened; EVIDENCE_STORE=on is required for the described collection.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-2
- Exact wording / scope: The pack verifier checks the manifest, files, key history, anchored range and linked records.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L334-L535
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py
- Verification and limits: Exact rendered wording. Trusted root and independently retained anchors are external assumptions.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-3
- Exact wording / scope: Without independently held anchors, its result is narrower: integrity of the supplied material, not proof that earlier material was never removed.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L334-L535
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L265-L277
- Verification and limits: Does not claim unanchored completeness or total history.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-4
- Exact wording / scope: To look for the second kind of gap, the verifier accepts an external change log through --changes.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L1068-L1160
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L279-L325
- Verification and limits: Rendered wording. Matching only covers supplied observations and relevant identifiers/time coverage.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-5
- Exact wording / scope: Verification reports change_unmatched.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L1068-L1160
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L279-L325
- Verification and limits: Rendered wording; unmatched external change is the documented failure, not a universal proof of misconduct.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-6
- Exact wording / scope: The verifier guide is explicit about the relationship: this is a port by the same project, not a clean-room implementation from an unrelated organization.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/operations/independent-verification.md
- Verification and limits: Rendered wording; canonical docs confirm same-project hand port. No SDK parity or independent-vendor claim.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 5-7
- Exact wording / scope: Expect the intact pack to verify, the unmatched change to produce change_unmatched, and the edited file to produce manifest_digest_mismatch.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/operations/audit-verification-walkthrough.md
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py
- Verification and limits: Rendered wording; documented behavior and tests inspected, not executed.
- Decision: retained after author and independent source-based expanded-revision review.

## Research and primary reader links
- Research source: No external research hook required; first-party audit verification mechanism.
- Canonical guide: https://docs.genesismesh.org/operations/audit-verification-walkthrough.html (opened and substantive body inspected without sign-in).
- Pinned code: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py (file fetched at exact revision).
- Pinned tests: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py (test assertions inspected; not run).
- Related guides opened: https://docs.genesismesh.org/operations/independent-verification.html ; https://docs.genesismesh.org/operations/audit-verification.html ; https://docs.genesismesh.org/examples/process-level-mediation.html ; https://docs.genesismesh.org/examples/declarative-boundary-policy.html ; https://docs.genesismesh.org/examples/invocation-bound-tokens.html . Only relevant ones are linked in the article.
- Website https://genesismesh.org/ and public demo https://mesh.genesismesh.org/ were verified through the public browser UI; web-fetch root failure was a tool limitation, not evidence of site downtime.
- GitHub repository is public and connected fetch succeeded. No temporary URLs or private credentials are in the copy.

## Reproduction scope
The article links the actual documented local procedure with prerequisites, expected result and failure. Its command was inspected in the documented example; it was not run here. Example source dates and expiry must be current when readers create their own records. Prefer the source demo's controlled fixture clock, where supplied, to blindly reusing historical timestamps; the delegation demo uses a fixed scenario time.
Sources show a mechanism and tests show asserted cases. Production adoption still needs integration-specific execution binding, key management, trusted facts and appropriate confinement. No research performance or security percentage is transferred to Genesis Mesh.


## Expanded revision — 2026-11-05

The user requested approximately 900 words, documentation links throughout and final Further reading. This revision reworks the prior reviewed mechanism and its essential limits; source-head and release checks on 2026-11-05 confirmed core a54b2d81f205c9b0203158f846f7ad44dc677063 and release v1.9.1 unchanged. The independent source reviewer also reconfirmed all six recorded source heads and latest releases unchanged. Relevant canonical guides were reopened. No SDK parity, live deployment, current revocation propagation or executed-test claim was added. Research remains motivation, not a Genesis Mesh guarantee. Public website and demo links identify available public entry points, not a tested deployment. A separate reviewer completed source-based review of the exact expanded article and LinkedIn text and the changed claim ledger; the author verified the staged hashes. No product example was executed. Covers and channel publication states are preserved.
