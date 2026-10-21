# A Contract That Holds

**Running It for Real · Part 4 of 5**

*What a stability promise has to cover when the things it protects are signed records meant to last for years.*

The project's stability page once promised commands that no longer existed. The page was written by hand, and the code moved on.

An independent operator pays for that kind of drift. Picture one with years of signed decisions in an archive, recognition treaties with two other sovereigns and controllers in two languages. An upgrade renames a response field, and a controller breaks. Or a signed record gains a field an older verifier quietly ignores, so the record means something the verifier cannot see. Every trust artifact the operator holds is only as durable as the software that reads it.

A promise written by hand decays. A promise a test checks on every change does not.

So Genesis Mesh classifies every public surface as stable, beta or internal: each route of the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, and each command, public function, signed artifact and error code. The classification lives in one contract file. Tests compare it with what the code exposes and fail on any drift, so changing a stable surface is deliberate.

The promise covers what is classified stable, for the whole major version, and it reaches the signed bytes. The canonical form that signatures cover stays fixed, and no stable route, signed field or error code is removed. A new signed field is optional and left out when absent, so older records still verify. A verifier refuses a signed field it does not know, so a newer record fails closed on an older verifier rather than losing part of its meaning. Security fixes are the stated exception.

Upgrades are rehearsed against real data. Each supported past release fills a database through its own API, which is then upgraded, verified record by record, restored from backup and migrated to PostgreSQL. Records signed by those releases keep verifying on every later one. Migrations only move forward, so rollback means restoring the backup taken before the upgrade. The maintainers' own security review lists, with reasons, the risks it left open.

A contract is also about leaving. The exit and fork note sets out what an operator owns and takes with it: its keys, its database, its endpoint and its trust decisions. Runtime code has no built-in endpoint, key or identity belonging to the project, and a test fails if one ever appears. Another sovereign recognizes you because it issued a treaty naming your keys; the project vouches for no one. The code is open and the protocol is public. A fork that passes the conformance vectors signs and reads records the same way, the precondition for working with sovereigns that never changed a line.

A promise to independent operators is worth what its tests enforce, and what it lets them take when they leave.

**Go deeper:**

The public contract: https://docs.genesismesh.org/reference/public-contract.html
Exit and fork: https://docs.genesismesh.org/operators/exit-and-fork.html

**Next:** Verify What You Run

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
