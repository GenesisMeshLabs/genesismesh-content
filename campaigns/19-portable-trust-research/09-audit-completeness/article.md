# A signed audit log does not tell the whole story

An auditor receives ten validly signed credential-rotation records. Was the history altered? Did another rotation happen without being reported? Those are different questions.

Genesis Mesh's [audit-verification workflow](https://docs.genesismesh.org/operations/audit-verification.html) addresses them with different evidence. Its Network Authority, the operator's local trust and policy service, can export an audit pack when `EVIDENCE_STORE=on`; the store is off by default.

The auditor needs a root public key obtained independently and signed store anchors copied to storage the authority's operators cannot rewrite. The [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L334-L535) checks the manifest, files, key history and anchored record range. Without held anchors, the conclusion is narrower: integrity of the supplied material, not assurance that nothing was removed.

In our illustrative rotation audit, an anchor can expose an incompatible rewrite of covered history. It cannot reveal a rotation that never reached the store.

For that, the auditor supplies an outside change log through `--changes`, such as cloud activity records. A change absent from the evidence store can produce `change_unmatched`. The [completeness implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L1068-L1160) and [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L279-L325) cover that comparison.

Its strength depends on the outside source's coverage, identifiers and timing. If both sources miss an event, reconciliation cannot recover it. A signed payload also does not prove its real-world claims are true. The auditor, not the system producing the pack, must control the independent comparison evidence.

## Check it yourself

Follow the [audit-pack walkthrough](https://docs.genesismesh.org/operations/audit-verification-walkthrough.html) with a local authority, enabled evidence store, independently obtained root key, held anchors and installed verifier tools.

Verify the original pack, supply an external change missing from it, then alter a byte in a copy. Expect the original to verify, the unmatched change to produce `change_unmatched`, and the edited file to produce `manifest_digest_mismatch`. This documented example was not executed in this review.

The walkthrough also compares the Rust verifier: a same-project port, not independent proof that the shared specification is correct. [Verifier limits](https://docs.genesismesh.org/operations/independent-verification.html)


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
