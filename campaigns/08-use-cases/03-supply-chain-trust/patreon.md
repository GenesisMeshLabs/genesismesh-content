# Securing Supply Chain Authorization

https://www.youtube.com/watch?v=H41w_3mMrcE

Supply chain attacks have made artifact signing mainstream. But signing an artifact and proving authorization to sign it are different things. This video is about the difference.

**The objective behind this video**

The software supply chain security conversation has advanced a lot in recent years ? SBOMs, artifact signing, hash verification, provenance attestations. All of that addresses a real problem: making sure what was built is what gets deployed, intact. We think there's a second problem that receives significantly less attention: proving that the person who signed the artifact was authorized to do so at that moment, under a delegation that was still valid, and whose terms can be independently verified.

Maintainer compromise attacks work precisely because they take place inside the trust relationship. The signing key is valid. The signature verifies. The artifact is correct. The authorization chain is broken ? and nothing in the standard tooling checks the authorization chain.

The objective of this video is to show how Genesis Mesh addresses this specific gap: signed, time-bounded attestation of a maintainer's release authority; release gates that check whether that attestation is current and non-revoked before promotion; and a revocation path that propagates the moment an account is compromised. It doesn't replace signature verification or SBOM tooling ? those answer "what is this artifact." Genesis Mesh answers "who was authorized to produce it, under what delegation, and is that authorization still valid." That's the question the existing tooling doesn't ask.

Website: https://genesismesh.connectorzzz.com
GitHub: https://github.com/GenesisMeshLabs
