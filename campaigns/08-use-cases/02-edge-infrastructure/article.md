# Use Case: Edge Infrastructure

Distributed infrastructure does not trust uniformly. Consider a branch office gateway operating over an unreliable link. When the link is up, the gateway enrolls with its Network Authority and retrieves a signed attestation of its identity and capabilities. When the link is down, it continues operating, verifying incoming requests against the cached attestation without a live call upstream. If the gateway is later compromised, the operator issues a signed revocation; systems that poll for revocation updates will detect it and enforce it on their next check. The gateway itself, if offline, will continue accepting requests until it reconnects and retrieves updated state.

This is the trust model edge infrastructure needs: portable identity with offline verifiability and explicit, signed revocation — not instant enforcement everywhere, but a clear, auditable record of when trust ended and why.

The standard answers do not scale well to this problem.

Mutual TLS proves the certificate is valid. It does not prove the node has not been compromised since enrollment. API keys prove the caller has a shared secret. They do not prove the caller is the correct node, or that the node's configuration has not drifted. Certificate authorities require revocation infrastructure that edge nodes cannot reliably consult. Private key rotation across thousands of edge nodes is operationally painful and frequently skipped.

What edge infrastructure needs is portable identity with revocable attestation.

Each Genesis Mesh node is enrolled with a cryptographic identity — an Ed25519 key pair tied to a Network Authority that operates the sovereign. The node can attest its current state: which software version it runs, which capabilities are active, which configuration it holds. That attestation is a signed artifact. Any downstream system that holds the NA's public key can verify the attestation offline, without a live connection to the issuing authority.

Revocation follows the same pattern. If a node is compromised, the operator issues a signed revocation artifact. Systems that poll for updates detect it and enforce it; systems operating offline continue trusting the cached attestation until they reconnect. The revocation record itself is permanent — it establishes when trust ended and under whose key, regardless of when downstream systems process it.

This model extends naturally across organizational boundaries. An edge node operated by one organization can be recognized by another's Network Authority, enabling cross-organization cooperation at the edge without centralizing the authorization decision in either party's backend.

The key property for edge deployments is offline verifiability. A node at the edge may not have a reliable connection to its own NA, let alone a third party's. Signed artifacts that verify against a known public key without a live call are what make trust portable to the edge in a meaningful sense.

Distributed infrastructure needs identity that travels with it.
