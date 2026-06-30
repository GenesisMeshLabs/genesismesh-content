Protocol Interoperability

A trust layer that only works from one language, one runtime, or one vendor's stack is not a trust layer. It is a library with a marketing story around it.

Real interoperability means that two systems built in entirely different languages, by different teams, operating on different infrastructure, can produce and verify the same trust artifacts. Not compatible artifacts. Not semantically similar artifacts. The same artifact, byte-for-byte verifiable against the same public key.

This is a harder constraint than it sounds.

Most "interoperability" in software systems means compatible APIs. You call the same HTTP endpoints. You parse the same JSON schema. But if the signing algorithm, key encoding, or canonical serialization differs between implementations, two systems that "speak the same protocol" will produce signatures that the other cannot verify. They are not interoperable at the trust layer — only at the communication layer.

Consider a concrete case: a Go service produces a signed attestation in a cloud environment. Six months later, a compliance team needs to verify that attestation using a .NET tool built by a different team in a completely different codebase. They hold the issuer's public key. They have no access to the Go service, its runtime, or its database. The verification either passes or it does not — the signature is over a canonical byte sequence that any compliant implementation can reproduce. That is interoperability at the trust layer, not the communication layer.

Genesis Mesh defines interoperability at the cryptographic layer. The Trust API specifies not just the HTTP surface but the exact signing algorithm (Ed25519), the exact canonical JSON serialization (sorted keys, no HTML escaping, no trailing whitespace), and the exact header set that must be present on every signed admin request. Any implementation that follows this specification will produce artifacts any other compliant implementation can verify.

Current SDK implementations include TypeScript (genesis-mesh-sdk on npm), Go (sdk-go), and .NET (genesismesh-sdk-dotnet on NuGet). Each covers the same seven sub-clients — Agreement, Attestation, Boundary, Consensus, DataUsage, Disclosure, and Evidence — against the same Network Authority HTTP API. The conformance suite defines reference vectors — canonical inputs and expected outputs across signatures, treaties, attestations, revocation, evidence, and consensus — that any implementation must reproduce. The Python reference implementation validates against them. SDK implementations are each verified through their own test suites against the same Trust API surface.

This matters for adoption. An organization running one stack and a partner running another should be able to exchange signed trust artifacts without either party accommodating the other's runtime. They speak the protocol. The runtime is irrelevant.

It also matters for verification. When you need to verify a trust artifact out-of-band — in a compliance review, in a forensic analysis, in a different language than the one that produced it — you need to know that the artifact is verifiable by any compliant implementation, not just the one that issued it.

Protocol interoperability is what makes portable trust actually portable.
