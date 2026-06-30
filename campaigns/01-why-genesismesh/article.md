# Why Genesis Mesh?

Systems today connect well. APIs talk to APIs. Services discover each other. Traffic flows across organizational lines. The connectivity problem is largely solved.

The trust problem is not.

When a request crosses an organizational boundary, connectivity carries it across. Nothing carries the authorization state with it. Each system must re-verify, re-interpret, or simply assume. The result is implicit trust — trust that exists in practice because it has to, but that exists in no verifiable, inspectable form.

This gap has consequences. A compromised supplier keeps making authorized requests because no mechanism carries the revocation downstream. A long-running automation inherits permissions that were never reviewed after the original context expired. An audit finds that a decision was made, but the evidence of why it was authorized does not exist.

The instinct is to add a central authority: a shared identity provider, a registry, a broker that all systems consult. But centralization shifts the problem. Now you have a single point of failure, a single point of capture, and a single owner for decisions that belong to independent organizations. You have also made cooperation conditional on every participant trusting that central system's operator.

Genesis Mesh starts from a different premise: trust should be carried by the protocol, not assumed by the connectivity layer.

That means trust decisions are explicit. A sovereign system issues signed evidence when it authorizes or recognizes another. The evidence is self-contained — it includes the decision, the keys that authorized it, and a timestamp. It does not require a live call to a central registry to verify. And it can be revoked with a signed withdrawal that propagates across boundaries.

This is portable trust. Not a marketplace. Not a reputation score. Not a shared registry. A protocol layer that lets independent operators make trust decisions, carry them across boundaries in signed form, and revoke them with the same level of proof.

Genesis Mesh is the implementation: a Network Authority per sovereign, a defined HTTP protocol surface, SDKs in TypeScript, Go, and .NET, and a conformance suite that defines the behavior any implementation must reproduce. The "per sovereign" part is not incidental — each operator runs its own authority, retains its own keys, and makes its own trust decisions. That is what makes the system genuinely sovereign rather than federated under a common owner.

The protocol is what makes portable trust possible. But the recognition network that forms on top of it is what makes it durable. Software can be copied. The accumulated graph of which sovereigns recognize each other — which attestations have been honored, which revocations have propagated, which trust relationships have been formed and held over time — cannot. The value of the network grows with the number of real recognition edges, not with the number of deployments.

If your systems cross organizational boundaries, portable trust is not a feature. It is the missing layer.
