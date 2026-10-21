# New Key, Same Past

**Governed Changes · Part 5 of 5**

Previously: an audit pack that someone outside can verify offline, without trusting the operator.

Every record a sovereign signs is meant to verify for years. The key that signed it will not last that long. A regulator sets a deadline for moving signing keys onto certified hardware, a key-management service is retired, people who had access move on. A verifier that knows exactly one key for the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, leaves only bad options: old signatures stop vouching, or the operator starts over as a new sovereign. The project's own security review listed this as the one high-severity risk it accepted and left open.

Changing a key should not mean changing who you are.

Key succession is the answer. Each sovereign starts from a founding record, signed by a root key meant to live offline, in the hands of the people accountable for the sovereign, and to be used for almost nothing. One of those few uses is a succession: a record naming the authority's next key and when it takes effect. Three keys sign it. The root key, on an offline machine, says the change is the sovereign's. The new key proves it exists and is held. The outgoing key shows the hand-over is continuous. Together the successions form a key history that anyone with the root's public key can check.

A verifier given that history asks one question of a signature: was this the authority's key at the record's own time? A decision signed years ago under the first key verifies as it always did. Treaties and attestations issued under the old key keep vouching. Agreements the authority signed are the exception, and must be offered again under the new key.

The obvious attack is to keep an old key useful: whoever still holds it signs something new and dates it inside the old key's window. Several rules narrow that. A succession cannot be backdated; it must be recorded before it takes effect. The outgoing key is accepted for five minutes past the hand-over, and time in the evidence store may not run backward by more than five minutes. A decision the outgoing key signs cannot stay valid more than a few minutes beyond that.

In the evidence store a window of a few minutes remains, bounded by the anchors made afterward. Records checked on their own, such as attestations and treaties, rely on the issue time they carry, so whoever keeps the old key can still sign one dated inside its old window.

Succession is a planned change. A lost or compromised authority key cannot sign its own succession, and the root key cannot be replaced at all. Losing either means starting over as a new sovereign identity, which partners must recognize afresh.

Keys change. What they signed must stay checkable.

**Go deeper:**

Key succession: https://docs.genesismesh.org/operations/key-succession.html

**Next:** Permission Before the Link Goes Down

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
