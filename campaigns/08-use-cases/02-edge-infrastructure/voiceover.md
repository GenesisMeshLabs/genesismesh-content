Edge infrastructure does not always have a reliable connection back to a central authority.

A branch gateway may need to verify requests while offline. It may hold a cached attestation, signed by its Network Authority, proving its identity and capabilities.

If the gateway is later compromised, the operator issues a signed revocation. Online systems can enforce it on their next check. Offline systems catch up when they reconnect.

Genesis Mesh does not pretend revocation is instant everywhere. It makes revocation explicit, signed, and auditable.

Distributed infrastructure needs identity that travels with it.
