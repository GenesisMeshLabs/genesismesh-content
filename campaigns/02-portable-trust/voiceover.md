Portable Trust

The phrase "zero trust" is well understood. Verify every request. Never assume. But zero trust frameworks are typically scoped to a single organization's perimeter. They describe how you handle traffic inside your boundary, authenticated against your identity store, authorized by your policy engine.

What happens when the request originates outside that boundary?

Most systems fall back on shared secrets, API keys, mutual TLS with a certificate chain they manage, or a federated identity protocol that still points back to a central provider. All of these work within a narrow scope. None of them solves the structural problem: trust decisions made on one side of a boundary need to be carried — not just referenced — to the other side.

Portable trust is the missing concept.

A portable trust decision is explicit — made at a specific time, by a specific authority, for a specific purpose, recorded in a verifiable artifact. It is self-contained — any party with the right public key can verify it without calling back to the authority that issued it. And it is revocable — the issuing authority can withdraw trust with an equally signed artifact, through the same channels as the original grant.

These three conditions together mean trust can travel across organizational lines without dragging the issuing authority's infrastructure into every verification. The receiver does not need a live connection to the issuer. The verifier does not need to trust the same central registry the issuer trusts.

Genesis Mesh implements portable trust as a protocol. A Network Authority issues signed attestations, agreements, and evidence records using Ed25519 keys. The artifacts are canonical JSON — deterministic, verifiable offline, and independent of any particular runtime. SDKs in TypeScript, Go, and .NET implement the same Trust API HTTP surface and produce identical artifacts.

The organizing principle matters before the implementation does. If your architecture assumes trust is verified in-band, at request time, against a central source of truth, you have already constrained what cross-boundary cooperation looks like. Start instead with the premise that trust moves with the data — signed, bounded, and revocable — and the architecture that follows is fundamentally different.

That is the shift portable trust makes possible.
