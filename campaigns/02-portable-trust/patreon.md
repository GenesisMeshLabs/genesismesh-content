# Portable Trust Across Boundaries

https://www.youtube.com/watch?v=y3GBM5h-RdY

The second video in the series goes deeper on what "portable trust" actually means — and why it's a harder concept than it sounds.

**The objective behind this video**

"Zero trust" has become a standard in the industry. Verify every request, never assume. But zero trust frameworks are almost universally scoped to one organization's perimeter: your identity store, your policy engine, your infrastructure. They're very good at what they do inside that boundary. They say almost nothing about what happens when a request originates outside it.

We made this video because we kept running into the same conversation with engineers and security architects: "we use zero trust internally" — followed by a description of how cross-organizational requests fall back on API keys, shared secrets, or a federated identity provider they don't fully control. Those mechanisms work in narrow cases. None of them carry a trust decision from one organization to another in a way that's self-contained and offline-verifiable.

Portable trust is the concept that fills that gap. The three conditions — explicit, self-contained, and revocable — are what distinguish a protocol-level trust primitive from an authentication workaround. Getting those conditions right is what the entire Genesis Mesh design is built around. This video makes that case from first principles, before diving into how the implementation works.

Website: https://genesismesh.connectorzzz.com
GitHub: https://github.com/GenesisMeshLabs

