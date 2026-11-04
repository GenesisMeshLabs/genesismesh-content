# A signed audit log does not tell the whole story

An auditor receives ten signed records of changes to a production system. Every signature verifies. Is the history complete?

There are at least two different questions. Did someone alter or remove a record that was previously committed to the history? And did a real change happen without anyone reporting it at all?

A signature on each remaining record cannot answer both questions by itself. The illustrative problem is not a weak signature. It is a missing comparison point.

## Hold evidence outside the system being audited

Genesis Mesh's Network Authority, the operator's service for local trust and policy, can keep an evidence store when `EVIDENCE_STORE=on`. It is off by default. The authority can export an audit pack containing records and their supporting material.

An auditor starts with a root public key obtained independently, then keeps signed store anchors on storage the authority's operators cannot rewrite. The [audit-pack verification guide](https://docs.genesismesh.org/operations/audit-verification.html) explains how those anchors constrain the history being presented. A key bundled inside the pack is not, on its own, a reason to trust the pack.

The [verification implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L334-L535) checks the manifest, files, key history, anchored range and linked records. Without independently held anchors, it reports a narrower result: integrity of the material supplied, not proof that nothing was removed. That distinction should survive into the audit report instead of disappearing behind a green check mark.

In an illustrative credential-rotation audit, a controller submits its execution record after changing a credential. An anchor held by the auditor makes a later incompatible presentation detectable within the covered history. The anchor still cannot describe a rotation that never reached the store.

## Compare the history with another observation

For that second case, the verifier accepts a separate change log through `--changes`. It compares the pack with events collected outside Genesis Mesh, such as a cloud activity log.

The documented walkthrough includes a resource change absent from the evidence store. Verification reports `change_unmatched`. The [completeness implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L1068-L1160) performs that reconciliation; [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L279-L325) covers unmatched external changes. The sources were inspected, not executed in this review.

The extra log introduces its own assumptions. It must cover the relevant resources and period, identify events consistently, and remain available. If both the controller and the outside observer miss a change, comparing their records does not conjure it into existence. If clocks or resource identifiers disagree, investigate the mismatch rather than treating it automatically as proof of misconduct.

These are operational responsibilities: who exports anchors, where they are held, which independent log supplies the comparison, and who resolves gaps.

## A second verifier adds another check

Genesis Mesh also provides `genesis-mesh-verify`, a Rust port of the Python verification logic. It can check a pack offline using public verification material.

That gives an auditor a second implementation to compare. It is not a clean-room implementation by an unrelated organization. Agreement can reveal neither a mistake copied by both implementations nor a shared misunderstanding of the specification. The [independent-verification guide](https://docs.genesismesh.org/operations/independent-verification.html) states this limitation directly.

A valid audit pack therefore supports a bounded statement about the supplied evidence and the anchors or observations used to check it. It does not prove that every real-world statement in a signed payload is true.

## Check it yourself

Follow the [audit-pack walkthrough](https://docs.genesismesh.org/operations/audit-verification-walkthrough.html). You need a local Network Authority with the evidence store enabled, its independently obtained root key, held anchors and the verifier tools. The procedure verifies the original pack, adds an external change absent from it, and changes a byte in a copy.

Expect the intact pack to verify, the outside change to produce `change_unmatched`, and the edited file to produce `manifest_digest_mismatch`. This is a documented example, not executed in this review.

For your own system, choose the outside comparison source before you need the audit. "All signatures passed" is useful evidence. "We checked what might be missing" requires more.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
