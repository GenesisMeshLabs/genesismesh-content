Recognition and Revocation

Trust is not a binary state that you set once and forget. It is a lifecycle. Systems recognize each other, cooperate under that recognition, and at some point circumstances change — a partner is compromised, a contract expires, a key is rotated by the wrong party. At that point, trust needs to end. Not gradually. Not eventually. Now, with proof.

Most systems handle the granting side of trust reasonably well. Federation protocols, certificate authorities, and API keys all have mechanisms for saying "this party is authorized." What they handle poorly — or not at all — is the withdrawal side.

Consider what happens when a compromised third party needs to be cut off. If trust was implicit (shared network, API key in config), you change the key and hope nothing downstream cached it. If trust was via a certificate, you issue a CRL and hope the relying parties check it. If trust was via a federated identity token, you revoke the session, but any already-issued tokens remain valid until they expire. In each case, revocation is an afterthought — a mechanism bolted on after the fact, with gaps between the withdrawal decision and its enforcement.

The structural problem is that most trust systems are designed to say yes, not to say no.

Recognition and revocation in Genesis Mesh are symmetric by design. Both are explicit, signed operations. A Network Authority issues a recognition treaty by signing an artifact that declares its terms: which sovereign it recognizes, what capabilities that recognition extends, and the validity period. Revocation is a signed withdrawal artifact — same format, same key, same distribution path. No revocation is implicit. No trust ends because a timer expired. A session expiry tells a system to stop accepting tokens. A revocation artifact tells the system why trust ended, when, under whose key — in a form that can be inspected and verified years later.

This matters for auditability as much as for enforcement. When something goes wrong, you need to know not just that trust was revoked, but when, by whom, under which key, and whether downstream systems received the revocation before or after an anomalous event occurred. Signed revocation artifacts provide exactly that record.

The ability to cut trust off with proof is not a security feature. It is a prerequisite for operating systems across organizational boundaries where you do not control the other side.

Recognition and revocation are the lifecycle. The protocol enforces both.
