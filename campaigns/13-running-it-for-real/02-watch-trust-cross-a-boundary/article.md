# Watch Trust Cross a Boundary

An architect has read the articles. Sovereign authorities, signed recognition, revocation that travels. She has one reply: show me. Not a diagram. Not a recorded demo. Two authorities that do not share keys, recognizing each other, live, with something she can try to break.

Describing portable trust is not the same as showing it.

At [mesh.genesismesh.org](https://mesh.genesismesh.org), a gateway sits in front of a live Network Authority, the service each operator runs to hold its keys and sign its trust decisions. Beside it stands a second, independently signed sovereign: the public reference at na.genesismesh.org, published read-only on a different machine with its own keys. Its web server never loads a private key; a separate maintenance job on that machine, under its own user, signs its records.

Each authority recognizes the other through a treaty, a signed, scoped and expiring agreement in which one sovereign accepts another's members for named roles. Neither signs for the other. Revocation crosses in one direction: the live authority imports the reference's signed revocation feed, the list of what the reference has withdrawn.

No account is needed. The console hands the operator's demo credential to anyone, so its safety cannot depend on secrecy. It depends on policy: the gateway refuses to start if that credential could do more than read and verify, or exceed a low quota. A visitor cannot issue, revoke, sign or publish anything.

What a visitor can do is check. The guided tour starts with the live mesh. It verifies a treaty from the reference against its pinned key, then a copy with one changed value, which fails with the exact reason. It shows one sovereign's member accepted across the treaty by the other, and a revoked member refused, its revocation in the signed feed. A scheduled job issues and revokes demo memberships, so the data stays current.

Then comes evidence. A demo secret rotates every ten minutes under a governed process, and the browser verifies its chain of records, matching the Python reference on shared test vectors. That check runs in your browser, with code and keys the same site serves. For an independent check, download the reference's signed evidence bundle and verify it offline against a key obtained elsewhere.

This proves less than it might seem. We operate both authorities. They share no keys and no database, but one team's demonstration is not proof that a separate operator can do the same; that proof belongs to an operator with its own keys, infrastructure and policy. What the demo does prove is that the mechanics are real: signed recognition both ways, revocation crossing the boundary, evidence anyone can check.

Try it at [mesh.genesismesh.org](https://mesh.genesismesh.org): open the guided tour, verify the treaty, and watch the tampered copy fail.

Trust that claims to be verifiable should not need an account to verify it.
