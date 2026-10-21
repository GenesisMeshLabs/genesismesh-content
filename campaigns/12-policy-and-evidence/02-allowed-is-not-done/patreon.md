# Allowed Is Not Done

**Policy and Evidence · Part 2 of 2**

*A decision says what was allowed. This post is about recording what was actually done.*

An auditor asks about one vendor's access key. Who allowed it to be created? Was it rotated when the policy said it would be? At offboarding, was the key actually revoked? The answers usually live in three places: a decision in an authorization system, an action in a controller's logs, and a change in a cloud provider's activity history. None links to the others, and each is kept by someone different.

A signed allow proves that the rotation was permitted. It says nothing about whether the rotation happened, when, or to which version of the key.

Genesis Mesh can put the decision and its consequence in one place: the evidence store, a history kept by the Network Authority, the service each operator runs to hold its keys and sign its trust decisions. Once the operator switches it on, the authority keeps every decision it signs, with the request it judged and how it reached its verdict. The controller, the program that actually changes the secret, then submits signed evidence of what it did, under its own key rather than the authority's.

The authority can say what was allowed. Only the executor that acted signs what it reports having done.

The authority does not take that report on faith. A record is refused, with a stable reason, if its signer is not a registered executor, a program the operator has authorized to act; if the decision it cites does not exist or was a deny; if the action falls outside the decision's window; or if it claims a capability the decision did not grant. Every acceptance and every refusal is audited.

What it accepts becomes one history per resource. Each record of an action on a secret points to the record before it, so the creation, every rotation and the final revocation form one chain, verifiable from one place. The store is meant to hold identifiers, versions and timestamps, never the secret itself, and it refuses records that obviously carry one.

The history only grows. The database refuses ordinary edits, and every entry carries the digest of the one before it, so changing an entry breaks the chain. Old entries leave only from the start of the history, behind a signed checkpoint the rest verifies from. But a chain proves order, not completeness, and whoever administers the database is not bound by its rules. That gap comes back later in the series.

For an auditor, the history leaves as a versioned export. Every line carries the signed record itself, and the whole export verifies offline with the public keys of the authority and the executors. A controller built on the TypeScript or Rust SDK asks, acts and records in one call.

Authorization and its consequence belong in the same record. Otherwise the audit is a reconstruction.

**Builds on our video** Why Every Trust Decision Needs a Signed Record: https://www.youtube.com/watch?v=gp5yqnNQdZI

**Go deeper:**

The evidence store: https://docs.genesismesh.org/examples/evidence-store.html

**Next:** A Front Door, Not an Authority

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
