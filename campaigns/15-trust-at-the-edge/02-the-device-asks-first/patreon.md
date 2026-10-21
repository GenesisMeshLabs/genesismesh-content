# The Device Asks First

**Trust at the Edge · Part 2 of 2**

*A small program on the device that asks first, acts within limits and can be cut off in one step.*

Previously: grants that let a device act within limits set in advance while it is cut off.

A water operator runs a few hundred pumping stations. Each has a small Linux board that drives the pumps and an unreliable link to headquarters. Pre-issued grants let a station act within limits while cut off, but two problems remained. Every service that wanted a grant had to embed an SDK. And asking the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, for a live decision meant putting an operator key on the board, one that could ask for far more than a pumping station should.

The answer is a small program called genesis-mesh-edge. It is an agent in the sense a monitoring agent is one: it runs on the device as one of the operator's nodes. It holds no policy. It advises, and the local services act on its answer.

It enrolls with a one-time invite and generates two keys on the device: a node key that identifies it, and an executor key that signs its records. Both are files protected by permissions, and no operator key lives there. The authority registers the executor key for this station's own resources, which no other edge node can claim.

Local services hold no keys. They ask the agent one question, over a local channel only callers the operator approved can use: may I do this, with these parameters, to this resource? While connected, the agent asks the authority for a decision scoped to this station alone. When the authority cannot be reached, it checks its grants, which it stops using if it has not refreshed its view of revocations within the operator's limit. Only when no grant can be used, and the service gives a justification, does the agent decide on its own, under break-glass: the change goes ahead, the record says why, and the authority judges it later.

An answer from the authority is final.

Unlike the TypeScript and Rust SDKs, the agent treats an overloaded authority as present: grants may cover the gap, break-glass may not. A request that a held grant names but does not cover is refused, justification or not.

Every record waits in a durable outbox on the board and uploads in order when the link returns.

When a station is stolen, the operator revokes the node. One step at the authority ends its certificates, retires its executor key and revokes every grant it held; anything later under that key is refused. The station itself learns at its next sync. Revocation ends what the authority will accept. It cannot reach a board kept offline, or stop someone who controls it, which is why grants are short and budgets small.

The agent is still in beta, and its rule is simple: a device should never hold more authority than the operator can take back in one step.

**Go deeper:**

The edge agent: https://docs.genesismesh.org/operations/edge-agent.html

**Next:** Five Languages, One Verdict

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
