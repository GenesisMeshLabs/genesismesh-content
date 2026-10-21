# An Audit That Doesn't Trust the Audited

Eighteen months after a breach, an insurer asks the operator two questions about the quarter it happened in: was every change to the affected credentials made under the operator's own rules, and is anything missing from the record? The evidence exists, signed and judged. But the usual way to show it is to ask the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, for an export, and to check it with a verifier from the same package that runs the authority.

The audit trusts the audited.

Portable trust has always meant that a signed decision can be checked by someone who does not take the signer's word for it. An audit pack carries that to the auditor. For any range between two anchors, the signed store heads from the first article in this group, the pack holds the records and everything they rest on: the decisions they cite, the policies in force, the keys that signed them. A manifest lists every file with its digest, and the authority signs it. A report lists every change, how it was governed and what was decided, including every use of break-glass.

The insurer's auditor verifies the pack offline from what they hold themselves: the public half of the sovereign's root key, the offline key the authority was founded on, and the anchors they have been copying out. Keys inside the pack prove nothing alone. Each record is judged as of its own time, so a decision that expired years ago still verifies for the moment it was made. Held anchors show that nothing was removed after each one was copied; without them, a pack proves only that what is present is intact.

The most important check uses a log the operator never controlled. The auditor converts a log the operator cannot alter, such as the cloud provider's own audit trail, into a simple list of changes, and every change in the period must match a record. A change that was never recorded, or was erased before an anchor covering it was copied out, shows up as an unmatched line.

That leaves the verifier itself. Genesis Mesh ships a second one, a standalone program ported by hand to Rust from the main implementation and held to a corpus of valid and tampered cases that implementation produces. A porting mistake in either shows up as a disagreement, though a design error the two share would not. It needs no private key and no network, and it builds reproducibly, so the auditor can rebuild it from source and compare the digest before trusting its verdicts.

An audit that only works if you trust the operator is a description. An audit you can run without that trust is evidence.
