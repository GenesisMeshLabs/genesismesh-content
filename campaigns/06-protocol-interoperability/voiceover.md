A trust layer that only works in one language or one runtime is not a trust layer. It is a library with a marketing story around it.

Real interoperability means different implementations can produce and verify the same trust artifacts. Not similar artifacts. The same canonical bytes, signed and verified against the same public key.

Genesis Mesh defines interoperability at the cryptographic layer: Ed25519 signing, canonical JSON serialization, and the exact header set for signed admin requests.

A Go service can produce an attestation today, and a .NET tool can verify it later without access to the original service, runtime, or database.

That is what makes portable trust actually portable.
