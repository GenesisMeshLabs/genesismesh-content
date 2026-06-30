Trust API and SDKs

A protocol that requires developers to implement Ed25519 signing, canonical JSON serialization, and a custom header set from scratch before they can make their first trust decision will not be adopted. Good primitives need usable surfaces.

Consider what "from scratch" actually means here. Before issuing the first signed agreement, a developer without an SDK must: serialize the request body to canonical JSON (sorted keys, no HTML escaping), construct four specific HTTP headers including a timestamp and a base64-encoded signature, pipe the exact byte sequence through Ed25519, and encode the result correctly. None of this is conceptually difficult, but all of it is exact. One byte wrong in the canonical body and the signature will not verify — silently. The server returns an authorization error with no indication of where the encoding diverged.

The SDKs exist so that problem does not belong to the caller.

The Genesis Mesh Trust API is the HTTP surface that makes the protocol reachable from real software. Every significant operation is an HTTP endpoint — issuing an agreement, building trust evidence, submitting an attestation, recording a boundary decision, querying consensus state, logging a data usage disclosure. The API is stable, versioned, and documented. You can call it from anything that speaks HTTP.

Current SDK implementations cover the major backend ecosystems:

TypeScript (genesis-mesh-sdk on npm) — for Node.js services, serverless functions, and edge compute environments.

Go (sdk-go) — for infrastructure tooling, CLI applications, and services where allocation control matters.

.NET (genesismesh-sdk-dotnet on NuGet) — for enterprise systems, Windows-first environments, and teams already running the .NET ecosystem.

Each SDK provides seven sub-clients, one per domain: Agreement, Attestation, Boundary, Consensus, DataUsage, Disclosure, and Evidence. All handle request signing automatically — the caller passes a key ID and base64-encoded private key once at client construction; every subsequent admin request is signed without additional setup.

The abstraction is intentional. The SDK encapsulates the correctness requirements so callers do not need to reproduce them.

The conformance suite defines reference vectors that SDK implementations can validate against. Each SDK is verified through its own test suite against the same Trust API surface.

For a developer integrating Genesis Mesh into an existing system, the path is: add the package, construct a client with credentials, call the sub-client method that matches the operation. The trust primitives — signing, canonical serialization, verification, revocation — are already correct.

The harder work is understanding which primitives to use and when. That is the protocol layer. The SDKs make sure the implementation is not the obstacle.
