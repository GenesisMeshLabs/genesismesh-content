# Staying Up Without Giving Up the Keys

On an ordinary Tuesday afternoon, the disk fails under the one host that signs an organization's trust decisions. Requests for decisions go unanswered. A compromised device needs revoking, and nothing is there to sign the revocation. Everything that relies on the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, is waiting on one machine.

A sovereign system that cannot stay up comes under pressure to stop being sovereign.

The easy fix is to hand the authority to someone who runs it at scale, and with it the keys, the database and the trust decisions. Genesis Mesh takes the other path: the operator can run its own authority as several instances, on infrastructure it controls.

That is optional. The default stays one host, one SQLite file and one key. An operator who needs more runs two or more instances behind a load balancer, sharing one PostgreSQL database. The instances keep no state of their own, so any of them can answer, and a failed one drops out of rotation. The database becomes the part that must not fail, so it has to be highly available in its own right, such as a zone-redundant server; while it fails over, the authority waits with it. All of this lives within a single region.

The hard part is that some things must happen exactly once. A request nonce is accepted once, or a replay gets through. Each revocation list carries a sequence number that must never be issued twice. Each evidence record holds one place in its chain. Checks in application code cannot promise that, because two workers, on one host or on several, can pass the same check at the same moment: two concurrent revocations could compute the same sequence number, and one could overwrite the other. So the database enforces every one of these rules, and they hold for any number of instances.

There is still one identity. Every instance reads the same signing key into memory from a key vault or the platform's secret store, and high-availability mode refuses the plain key-file provider, so key files are not copied from host to host and the authority never writes the key to disk. An instance that cannot reach its database or its key reports not ready and makes no decisions; it never falls back to local state.

The claim is tested. Under load, one of two authority processes is killed while decisions, evidence and revocations keep flowing through the other. Every acknowledged record survives exactly once, and attestations revoked during the failure stay revoked. A recovery drill dumps a populated database, restores it into a new one and has a fresh instance verify every treaty, revocation, policy, decision and evidence record.

What an authority acknowledged, it keeps. That is what availability means for trust.
