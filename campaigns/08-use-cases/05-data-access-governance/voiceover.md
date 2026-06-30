Use Case: Data Access Governance

Data governance frameworks describe policies: who can access what, under what conditions, for what purpose. They are well-developed on paper. The enforcement layer beneath them — the one that answers "was this access actually authorized at the moment it happened, by an authority that had the right to grant it?" — is usually thinner than the framework implies.

Access logs record what was accessed. Access control systems record what the policy said at the time. Neither records the full authorization state: who granted access, under what delegation, whether that delegation was still valid, and whether the stated purpose matched the actual access pattern. When an audit asks those questions after the fact, the answer is usually assembled from partial records, which is different from being proven.

The data governance use case in Genesis Mesh is not about data routing or data translation. It is about carrying the authorization context with the access decision.

A data access event is a trust decision. System A is granted access to data held by System B, for a specific purpose, under a specific policy, at a specific time. Genesis Mesh makes this decision explicit: a DataUsage disclosure record is issued — signed by the authority that authorized the access, timestamped, including the stated purpose and the policy terms. The record can be verified by any party that holds the issuing authority's public key.

This matters most in cross-organizational data sharing. Consider a GDPR-governed scenario: a data processor accesses patient records under a data processing agreement with a healthcare operator. Six months later, a regulator requests evidence that each access fell within the scope and purpose defined in the agreement. With conventional logging, the processor presents retained logs and hopes the auditor accepts the reconstruction. With DataUsage records, the processor presents signed artifacts — each containing the stated purpose, the policy reference, the issuer, and a timestamp — produced at the moment of access. The artifacts are self-contained and verifiable without auditing the processor's logging infrastructure.

With a DataUsage record, the audit artifact is produced at the moment of access, not after. It includes purpose, policy reference, issuer, timestamp, and signature. It can be presented to an auditor, retained for a compliance period, and verified offline without a live connection to the system that produced it.

The limit of what Genesis Mesh does here is important to state clearly. It makes authorization decisions auditable. It does not make data semantics auditable — it is not a data catalog, a lineage tracker, or a translation layer. The authorization context travels with the access event. The data itself is outside the scope of the protocol.

Authorization evidence is the governance artifact. Everything else is built on top of it.
