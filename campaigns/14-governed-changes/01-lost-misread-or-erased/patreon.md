# Lost, Misread or Erased

**Governed Changes · Part 1 of 5**

*Three quiet ways evidence fails: it gets lost, it gets read two ways, or it disappears.*

At two in the morning a controller rotates a database credential. The rotation succeeds. Then it tries to hand the signed record of what it did to its Network Authority, the service each operator runs to hold its keys and sign its trust decisions, and the authority is mid-restart. The submission fails. The credential has changed, and the proof that it changed under a decision lives only in the memory of a process that is about to exit.

Evidence is only useful if it arrives, if it means one thing to everyone who reads it, and if it stays where it was put.

Each of those can fail quietly.

The first failure is loss. A controller built on the TypeScript or Rust SDK can keep an outbox: durable storage the operator supplies, where the signed record is written as soon as the action has run and kept until the authority admits it. When the authority is back, the controller flushes the outbox, oldest first for each resource. A record the authority refuses for good stays in the outbox as a dead letter with its refusal code, and the authority can keep it in quarantine as well.

The second failure is ambiguity: one record that two verifiers read in two different ways. Every Genesis Mesh verifier refuses a signed field it does not know and the kinds of input implementations were found to read differently, and accepts a record only in its canonical form. How those differences were found is a story for later in this series.

The third failure is removal. The evidence store, where the authority keeps its decisions and what was done with them, is a hash chain: each entry carries the digest of the one before it, so an edited entry breaks the chain. But a chain proves order, not completeness. Whoever can write the database can delete an entry and recompute every link after it. So the authority signs the head of its store, hourly by default and whenever asked. That signature is an anchor, and one anchor covers every entry before it. An auditor, using a read-only key the operator issues, copies the anchors to storage the operator cannot change. From then on, an export that removed, rewrote or truncated an anchored range no longer matches them.

Removal stays undetectable until an anchor covering the entry has been copied out. The copy schedule sets that window, and the auditor can ask for a fresh anchor each time they copy. A change that was never recorded at all is a different problem, and the next article takes it up.

The controller from two in the morning can exit now. Its record is in the outbox, waiting.

Evidence that can vanish without anyone noticing was never evidence.

**Builds on our video** Why Every Trust Decision Needs a Signed Record: https://www.youtube.com/watch?v=gp5yqnNQdZI

**Go deeper:**

Evidence anchors: https://docs.genesismesh.org/operations/evidence-anchors.html

**Next:** Changes That Happen Anyway

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
