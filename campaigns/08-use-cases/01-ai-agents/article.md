# Use Case: AI Agents

Multi-agent systems have a trust problem that orchestration frameworks do not solve.

When one agent delegates a task to another, or when an orchestrator dispatches work to a specialized subagent, the framework knows the routing. It does not know whether the acting agent holds legitimate authority, under whose key it was enrolled, or whether that enrollment has been revoked. If the answer to those questions is "the framework tracks this internally," you have implicit trust inside a runtime boundary — not portable trust across organizational ones.

This is the distinction Genesis Mesh targets: not intra-runtime coordination, but cross-boundary trust.

A concrete example: a user's agent, operating under Sovereign A's authority, needs to call a specialized data service run by Sovereign B. Sovereign B has no prior relationship with the user's agent. For the call to be authorized, Sovereign A must have issued a signed attestation of the agent's identity and capability set, and Sovereign B must hold a recognition treaty with Sovereign A that covers this class of request. Without those two signed artifacts, the request is not authorized — regardless of how sophisticated the orchestration layer above it is.

An AI agent that operates within a single organization's runtime does not need Genesis Mesh. The orchestration framework, the IAM system, and the internal network boundary handle the trust surface adequately. But when agents cross organizational lines — when a user's agent interacts with a partner's service, when an automation delegates to an external capability, when an autonomous system needs to prove its authorization to a system it has no prior relationship with — the trust layer beneath the routing layer matters.

Genesis Mesh provides that layer. A Network Authority enrolls agents as nodes: each node has an Ed25519 key pair, each has a defined capability set, each can be attested and recognized by a second sovereign. When an agent from Sovereign A makes an authorized request to Sovereign B, the trust path is explicit — a signed recognition treaty from A to B, a signed attestation of the agent's current state, and a signed evidence record of the decision.

None of this requires Genesis Mesh to know what the agents are doing. It is not a task router. It is not an agent framework. It is the layer that answers the authorization question before the routing question is even posed.

Agents are an overlay. They consume the trust primitives that Genesis Mesh exposes — enrollment, attestation, recognition, revocation, evidence — and those primitives are available to any runtime that can make an HTTP request.

The trust layer should outlast any particular agent framework. Build it independently of the orchestration layer, and it will.
