# Offline trust and revocation: what a disconnected system can know

A controller loses its network connection at 10:00. At 10:05, its operator revokes a permission. At 10:06, the controller receives a request that would have been allowed before the outage.

The signature on the permission still verifies. The controller has no new message telling it that authority has changed.

That gap is the starting point for offline trust. A system needs to make its limits explicit before the connection disappears.

## Separate authenticity from freshness

A signature helps establish who issued a record and whether its signed contents changed. Deciding whether to accept that record also requires policy: which issuer is recognized, which action is covered, when the permission expires, and how recent the available revocation information must be.

The disconnected controller can check information it already holds. It cannot discover a revocation that has never reached it. Short validity periods and small use budgets can reduce exposure, but they do not create a communication channel.

[NostrAgent](https://arxiv.org/abs/2609.22944) explores decentralized identity, delegation and offline verification from signed events. Its prototype is useful research context for this distinction. Offline verification should not be read as a promise that every verifier knows the latest authority state.

## What Genesis Mesh documents today

Genesis Mesh approaches this through portable trust for sovereign systems. Its [pre-issued grants](https://github.com/GenesisMeshLabs/genesismesh/blob/main/docs/operations/grants.md) let a Network Authority authorize a bounded class of changes before a controller disconnects. The grant binds a bearer key, capabilities, validity, a use budget and a parameter envelope. Signed time tokens and chained use records support later verification.

There are important operating limits. Grants and the evidence features they require are off by default. Grant routes are beta. A holder learns of revocation when it reads a fresh feed; the authority can refuse or quarantine a submitted use after the external action has already occurred.

The runbook also describes break-glass fallback when the authority cannot be reached. In the TypeScript and Rust SDKs, an expired or exhausted grant does not necessarily stop an urgent change: it may run and be judged later. The edge agent has stricter rules for some server responses. An application requiring a hard stop must verify its actual execution path rather than assuming expiry provides one.

## A useful test before deployment

Consider a simulated controller with a small grant. Disconnect it, revoke the grant at the authority, attempt a change, then reconnect. Capture four separate events: the action requested, the local decision, the external outcome and the authority's later treatment of the evidence.

This is a proposed experiment, not a result reported here. Include an expired grant and a break-glass case. Otherwise the test may show only the easy path.

The practical question is specific: which actions can your system take with old trust information, for how long, and with what consequences when the records return?
