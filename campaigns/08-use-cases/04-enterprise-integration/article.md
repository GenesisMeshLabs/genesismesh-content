# Use Case: Enterprise Integration

Enterprise integration across organizational boundaries usually means one of two things: one party adopts the other's identity system, or both parties adopt a shared third-party broker. Either way, one participant's local authority is subordinated to another's infrastructure.

Consider two mid-sized enterprises integrating for a joint service offering. Neither is willing to make the other an authority over its own identity system. Neither wants to depend on a third-party broker they do not control. The practical problem in this situation is that standard integration paths require exactly that subordination — one party's access control, credential lifecycle, and revocation decisions become entangled with the other's. If the relationship changes, unwinding the commercial terms is straightforward; unwinding the shared trust infrastructure is not.

The alternative — and the integration model the Genesis Mesh protocol is designed around — is integration without authority transfer.

Two enterprises can cooperate through explicit, bilateral recognition. Enterprise A's Network Authority issues a signed recognition treaty that says: "We recognize Enterprise B's Network Authority as a valid source of trust for the following capabilities, under these terms, for this validity period." Enterprise B does the same in the other direction. Each party retains full control of its own keys, its own enrollment, its own revocation decisions. Neither party's operations become dependent on the other's infrastructure being available.

Within that recognition relationship, cross-boundary requests carry signed evidence. When Enterprise B's system makes a request that requires authorization from Enterprise A's side, it presents an attestation — signed by B's NA, verifiable by A against the recognition treaty. If B's credentials are revoked, A's systems detect it when they next verify the attestation. B's own systems are unaffected.

This model fits the political reality of enterprise partnerships better than centralized federation does. Contracts between enterprises define terms, scope, and exit conditions. The recognition treaty in Genesis Mesh is the technical analog: explicit terms, a defined scope, a signed expiry, and a revocation mechanism that any party can exercise unilaterally.

The integration does not require either enterprise to treat the other as an authority over their own systems. It requires them to agree on what they recognize, express that agreement in a signed artifact, and operate within those terms until one party withdraws.

The value of this model grows as more sovereign operators join the network. Two enterprises whose operators are part of the same recognition graph can form bilateral recognition without Genesis Core or any other central party brokering the relationship. That is the difference between a product and a protocol: the trust infrastructure becomes more useful as independent operators form real recognition edges with each other, not because any central registry grows.

Local authority stays local. Cross-boundary cooperation stays explicit.
