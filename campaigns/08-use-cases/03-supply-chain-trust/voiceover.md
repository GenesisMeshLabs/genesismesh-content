Use Case: Supply-Chain Trust

Software supply chain security has become serious infrastructure work. But most of the tooling addresses the artifact layer — what was built, what it contains, whether it matches a known hash. The trust layer beneath the artifact layer receives less attention: who authorized this release, under what delegation, and can that authorization be withdrawn?

These are not the same question.

A signed artifact proves the artifact was not tampered with after signing. It does not prove the person who signed it was authorized to do so at that moment. Maintainer compromise attacks work precisely because the victim's signing key was trusted — the signature was valid, but the trust was misplaced. The artifact is correct. The authorization chain is broken.

Genesis Mesh addresses the authorization chain.

A maintainer's trust relationship to a project can be attested: signed evidence that Maintainer A holds signing authority for Project B, issued by the operator that controls the project's namespace. That attestation has a validity period. It can be revoked — with a signed withdrawal — the moment the maintainer account is compromised, the maintainer leaves the project, or the delegation terms expire.

Release gates are a natural consequence. Before a release artifact is promoted to a distribution channel, a boundary decision is evaluated: does the signing party hold a current, non-revoked attestation of release authority for this project? The boundary decision is itself a signed record — it can be audited after the fact to show that the gate ran, that the attestation was valid at evaluation time, and what the outcome was.

The revocation path is where the model earns its value. When a maintainer account is compromised, the response is typically: rotate the key, re-sign recent artifacts, notify downstream consumers. With a signed revocation, there is an additional step with a harder guarantee: issue a revocation artifact for the compromised delegation. Any system in the publishing path that checks Genesis Mesh attestations — a package registry, a CI release gate, a package-manager policy — will reject the compromised key's signatures from that point forward. That enforcement requires those integration points to exist. The protocol provides the trust mechanics and the revocation artifact; the supply-chain protection becomes complete when the publishing path is wired to check them.

This does not replace signature verification, SBOM tooling, or vulnerability scanning. Those address what the artifact is — its contents, its dependencies, its integrity. Genesis Mesh addresses who was authorized to produce it, under what delegation, and whether that authorization is still valid. The two layers are complementary.

Maintainer trust is not a binary. It is delegated, bounded, and withdrawable. Treat it as such.
