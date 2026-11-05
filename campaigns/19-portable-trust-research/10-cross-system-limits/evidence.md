# Evidence ledger - idea 6: Can an agent keep its limits when it crosses systems?

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

### Claim 6-1
- Exact wording / scope: The issue_invocation_token function takes the supplied agreement or delegated scope and refuses requested capabilities outside that scope.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L108-L199
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py#L203-L339
- Verification and limits: Rendered wording; caller validates source basis and lifetime. Not an independent authentication of the source agreement.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 6-2
- Exact wording / scope: The receiver calls verify_invocation_token with trusted issuer keys, the requested capability, bearer identity and verification time.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py#L203-L339
- Verification and limits: Rendered wording; wrong bearer, expiry or missing capability fail. Caller authenticates identity, chooses trusted keys and binds actual execution.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 6-3
- Exact wording / scope: A token may include max_invocations, but the verifier counts caller-supplied use records.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py#L359-L387
- Verification and limits: Rendered wording. No global durable counter, concurrent coordination or record-set completeness guarantee.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 6-4
- Exact wording / scope: The API does not verify the entire linked use-record chain, so merely passing a collection of records should not be described as proof of globally complete consumption.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311
- Verification and limits: Bounded negative from inspected verifier; creation of linked records is not whole-chain verification.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 6-5
- Exact wording / scope: The supported peer_sovereign: constraint checks the bearer; it is not a general service URL or audience binding.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L207-L250
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py
- Verification and limits: Rendered wording; only known constraint implementations accepted.
- Decision: retained after author and independent source-based expanded-revision review.

### Claim 6-6
- Exact wording / scope: Expect acceptance for the intended bearer and capability, and refusal with a wrong bearer or ungranted capability.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/invocation-bound-tokens-demo.py
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py
- Verification and limits: Source demo uses controlled clock. Not executed; AIP research supplies motivation, not transport compatibility or SDK parity.
- Decision: retained after author and independent source-based expanded-revision review.

## Research and primary reader links
- Research source: https://arxiv.org/abs/2603.24775
- Canonical guide: https://docs.genesismesh.org/examples/invocation-bound-tokens.html (opened and substantive body inspected without sign-in).
- Pinned code: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py (file fetched at exact revision).
- Pinned tests: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py (test assertions inspected; not run).
- Related guides opened: https://docs.genesismesh.org/operations/independent-verification.html ; https://docs.genesismesh.org/operations/audit-verification.html ; https://docs.genesismesh.org/examples/process-level-mediation.html ; https://docs.genesismesh.org/examples/declarative-boundary-policy.html ; https://docs.genesismesh.org/examples/invocation-bound-tokens.html . Only relevant ones are linked in the article.
- Website https://genesismesh.org/ and public demo https://mesh.genesismesh.org/ were verified through the public browser UI; web-fetch root failure was a tool limitation, not evidence of site downtime.
- GitHub repository is public and connected fetch succeeded. No temporary URLs or private credentials are in the copy.

## Reproduction scope
The article links the actual documented local procedure with prerequisites, expected result and failure. Its command was inspected in the documented example; it was not run here. Example source dates and expiry must be current when readers create their own records. Prefer the source demo's controlled fixture clock, where supplied, to blindly reusing historical timestamps; the delegation demo uses a fixed scenario time.
Sources show a mechanism and tests show asserted cases. Production adoption still needs integration-specific execution binding, key management, trusted facts and appropriate confinement. No research performance or security percentage is transferred to Genesis Mesh.


## Expanded revision — 2026-11-05

The user requested approximately 900 words, documentation links throughout and final Further reading. This revision reworks the prior reviewed mechanism and its essential limits; source-head and release checks on 2026-11-05 confirmed core a54b2d81f205c9b0203158f846f7ad44dc677063 and release v1.9.1 unchanged. The independent source reviewer also reconfirmed all six recorded source heads and latest releases unchanged. Relevant canonical guides were reopened. No SDK parity, live deployment, current revocation propagation or executed-test claim was added. Research remains motivation, not a Genesis Mesh guarantee. Public website and demo links identify available public entry points, not a tested deployment. A separate reviewer completed source-based review of the exact expanded article and LinkedIn text and the changed claim ledger; the author verified the staged hashes. No product example was executed. Covers and channel publication states are preserved.
