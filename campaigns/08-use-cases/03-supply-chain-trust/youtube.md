# YouTube Metadata - Supply Chain Trust: Beyond Artifact Signing

**Title:** Supply Chain Trust: Beyond Artifact Signing

**Video ID:** `H41w_3mMrcE`
**Video URL:** https://www.youtube.com/watch?v=H41w_3mMrcE
**Thumbnail:** `../../../videos/thumbnails/use-cases-supply-chain-trust.png`
**Thumbnail text:** SIGNING IS NOT ENOUGH
**Render:** `../../../videos/renders/use-cases-supply-chain-trust-revid-stock.mp4`

**Description:**
Most supply-chain security tooling checks what was built and whether it matches a known hash. It rarely checks who was authorized to build it, and whether that authorization could still be withdrawn. A signed artifact proves it wasn't tampered with after signing — it doesn't prove the signer was authorized at that moment. Maintainer-compromise attacks exploit exactly that gap.

Genesis Mesh attests a maintainer's signing authority for a project as signed, time-bounded evidence that can be checked at release gates and revoked the moment an account is compromised. Any system in the publishing path that checks the attestation — a registry, a CI gate, a package-manager policy — rejects the compromised key's signatures from that point forward. It doesn't replace SBOM tooling or signature verification; it answers the question they don't: who was authorized to produce this, and is that authorization still valid?

Website: https://genesismesh.connectorzzz.com
GitHub: https://github.com/GenesisMeshLabs

**Tags:** supply chain security, software supply chain, Genesis Mesh, maintainer compromise, release gates, SBOM, signed attestation, Ed25519, Zero Trust, open source security, trust protocol

**Category:** Science & Technology
