# Evidence ledger - idea 2: How do you revoke one delegation without breaking everything?

Review date: 2026-11-04. Intended publication date: not assigned. Authoring reviewer: Codex campaign author.
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

Exact wording below follows the shortened article revision. Source inspection and test-execution status are unchanged.

### Claim 2-1
- Exact wording / scope: Each hop identifies its parent and binds its terms.
- Affected assets: article.md, identical patreon.md and the narrower linkedin.md.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L723-L746
- Verification and limits: Beta chain verification; does not establish live root validity or multi-parent path preservation.
- Decision: retained with the stated scope after author shortening review; independent revision review follows.

### Claim 2-2
- Exact wording / scope: The verifier checks linkage, capability containment, validity limits and signatures.
- Affected assets: article.md, identical patreon.md and the narrower linkedin.md.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603
- Verification and limits: Source and tests inspected, not run; receiving system remains responsible for current execution policy.
- Decision: retained with the stated scope after author shortening review; independent revision review follows.

### Claim 2-3
- Exact wording / scope: The controlled-time example verifies a two-hop chain and refuses a capability outside its parent's scope.
- Affected assets: article.md, identical patreon.md and the narrower linkedin.md.
- Implementation: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/delegation-chain-demo.py
- Test source: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603
- Verification and limits: Documented example uses a fixed scenario clock. Not executed in this review.
- Decision: retained with the stated scope after author shortening review; independent revision review follows.

## Research and primary reader links
- Research source: https://arxiv.org/abs/2608.30091
- Canonical guide: https://docs.genesismesh.org/examples/delegation-chain.html (opened and substantive body inspected without sign-in).
- Pinned code: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py (file fetched at exact revision).
- Pinned tests: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py (test assertions inspected; not run).
- Related guides opened: https://docs.genesismesh.org/operations/independent-verification.html ; https://docs.genesismesh.org/operations/audit-verification.html ; https://docs.genesismesh.org/examples/process-level-mediation.html ; https://docs.genesismesh.org/examples/declarative-boundary-policy.html ; https://docs.genesismesh.org/examples/invocation-bound-tokens.html . Only relevant ones are linked in the article.
- Website https://genesismesh.org/ and public demo https://mesh.genesismesh.org/ were verified through the public browser UI; web-fetch root failure was a tool limitation, not evidence of site downtime.
- GitHub repository is public and connected fetch succeeded. No temporary URLs or private credentials are in the copy.

## Reproduction scope
The article links the actual documented local procedure with prerequisites, expected result and failure. Its command was inspected in the documented example; it was not run here. Example source dates and expiry must be current when readers create their own records. Prefer the source demo's controlled fixture clock, where supplied, to blindly reusing historical timestamps; the delegation demo uses a fixed scenario time.
Sources show a mechanism and tests show asserted cases. Production adoption still needs integration-specific execution binding, key management, trusted facts and appropriate confinement. No research performance or security percentage is transferred to Genesis Mesh.

## Concise revision

Shortened 2026-11-04 at the user's request. One scenario and one mechanism retained, with essential refusals and limitations. The same pinned evidence supports this revision; no new feature, deployment or test-run claim was added. Independent concise-revision review is pending. Superseded prose was removed, not silently treated as reviewed. No publication or schedule field changed.
