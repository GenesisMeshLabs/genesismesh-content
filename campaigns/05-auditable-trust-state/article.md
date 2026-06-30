# Auditable Trust State

After an incident, the question is never just "what happened?" It is "why was that allowed to happen?" That second question requires evidence of the authorization state at the time the event occurred — who trusted whom, what that trust permitted, whether it was still valid, and whether anyone could have known it was about to be abused.

Most systems cannot answer that question with proof. They can answer it with logs, if the logs were retained and correlated correctly. They can answer it with inference, if the access control policy was consistent and documented. But direct, cryptographically verifiable evidence of the trust state at a specific point in time — that is rarely available because it was rarely produced.

Auditable trust state means that every trust decision leaves a signed artifact. Not a log line. Not an access control evaluation recorded in a SIEM. An explicit, self-contained record that includes the decision, the authority that made it, the keys used to authorize it, the timestamp, and the signature.

This matters in three situations.

The first is post-incident review. Consider: a compromised partner account makes unauthorized API calls over several hours before the anomaly is detected. The incident report needs to answer whether each call was authorized at the moment it was made — and whether the partner's attestation was still valid, or whether a revocation had already been issued before the calls started. A reconstructed log trail shows the calls happened. A signed trust evidence record shows the authorization state at the moment each one did. A signed evidence record from the moment of authorization cannot be retroactively altered. The signature is either valid or it is not. The key that signed it is either in the trust set or it is not. Forensic reconstruction does not depend on whether someone configured log retention correctly.

The second is compliance. Regulators and auditors want to see that access decisions were intentional, authorized, and reviewable. A signed artifact satisfies this in a way that a reconstructed log trail does not.

The third is operational confidence. When a system is operating across sovereign boundaries, the operators of each sovereign need to know what trust relationships are currently active. Not estimated. Not inferred from traffic patterns. Explicitly stated in verifiable form.

Genesis Mesh produces trust evidence records for every significant authorization decision: agreements between sovereigns, attestations of node state, boundary decisions, consensus outcomes, and data usage disclosures. Each is signed with the operator's Ed25519 key. Each is verifiable by any party that holds the corresponding public key, without a live connection to the issuing authority.

The audit trail is not a report generated after the fact. It is the protocol output.
