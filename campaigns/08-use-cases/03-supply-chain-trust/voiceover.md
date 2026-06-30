Software supply-chain security usually focuses on the artifact: what was built, what it contains, and whether it was tampered with.

But there is another question beneath that: who was authorized to produce this release, under what delegation, and can that authorization be withdrawn?

A valid signature does not prove the signer was still authorized. Maintainer compromise works because trusted keys can be misused.

Genesis Mesh adds the authorization layer. Maintainer authority can be attested, bounded, checked at release gates, and revoked with a signed withdrawal.

It does not replace SBOMs, signature verification, or vulnerability scanning. It complements them by making authorization explicit and withdrawable.
