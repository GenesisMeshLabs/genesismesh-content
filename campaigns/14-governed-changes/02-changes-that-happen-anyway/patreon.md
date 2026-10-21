# Changes That Happen Anyway

**Governed Changes · Part 2 of 5**

Previously: evidence that survives an outage, means one thing everywhere and cannot vanish unnoticed.

At the end of a night shift, an on-call engineer hands over the incident notes. One thing is missing: the engineer replaced a leaked API key by hand in the cloud console. Elsewhere, a controller that cannot reach its Network Authority, the service each operator runs to hold its keys and sign its trust decisions, still has a certificate to renew before it expires. Neither change asks the authority first. In most systems neither leaves a trace where trust decisions are kept, and nobody can say whether either was allowed.

A record of the governed path describes the well-behaved part of a system and says nothing about the rest.

The rest is often where the incident was.

Once the operator switches it on, Genesis Mesh records changes it did not govern. An observer, a small program the operator writes and runs, watches where changes show up, such as a cloud activity log. For each change it finds, it signs an observation: which resource, what was done, when, and who the source says did it. An observation proves what the observer saw. The actor is whatever the source reported, not an authenticated identity.

If the change matches a governed action already on record, that action's decision governs it, though the observer's own facts are still judged. Otherwise the authority judges the change: one signed verdict, allow, deny or indeterminate. The important choice is the clock. A change is judged as of when it happened, under the policies active then, reconstructed from the signed record of when each policy was switched on. Today's stricter policy does not condemn yesterday's legitimate change. The observer reports that time itself, within a bounded backlog, and a judgment today's policy would answer differently is flagged for a person.

A judgment cannot pass for permission. It is a record of its own kind, which no verifier reads as an authorization and no governed action can cite.

Then there is the outage. A controller built on the TypeScript or Rust SDK asks for a decision, and the request times out, fails on the network, or gets a server error or a rate limit. Its caller can break the glass: give a justification, let the action run, and have the controller sign a break-glass record that waits in the outbox until the authority can judge it. The record is the controller's own word that the authority was out of reach. No policy can stop the glass breaking, but one can make the later verdict deny for that capability. The edge agent, later in this series, is stricter: an authority that answers with an error has been reached.

Break-glass covers an authority that cannot be reached. It never covers an authority that answered no.

A change does not have to be governed to be accountable.

**Go deeper:**

Out-of-band changes: https://docs.genesismesh.org/operations/out-of-band-changes.html

**Next:** Rotate Forward, Never Back

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
