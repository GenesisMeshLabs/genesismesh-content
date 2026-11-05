# A signed audit log does not tell the whole story

An auditor receives ten signed records of credential changes. Every signature verifies. The platform team says the history is complete. Can the auditor accept that statement?

In this illustrative audit, two different gaps matter. Someone might remove a record that previously belonged to the history. Or a real credential rotation might never reach the evidence store. A signature on each remaining record cannot, by itself, distinguish either situation from a complete history.

The missing ingredient is a comparison point outside the material being presented.

## Establish what the pack is anchored to

Genesis Mesh's Network Authority, the operator's service for local trust and policy, can retain evidence when `EVIDENCE_STORE=on`. The evidence store is off by default. An enabled authority can export an audit pack containing records and supporting material for verification away from the running service.

The auditor first needs the authority's root public key from an independent channel. Accepting a key merely because it arrived inside the same pack would let the pack define its own trust. The [audit verification guide](https://docs.genesismesh.org/operations/audit-verification.html) explains the expected verification inputs.

The auditor also keeps signed store anchors on storage the authority's operators cannot rewrite. These are external commitments against which a later presented history can be checked. Their value depends on when they were obtained, what range they cover and whether the audited operator can replace the auditor's copies.

In our credential scenario, a controller submits evidence after a rotation. An auditor-held anchor covering that history constrains a later account of those recorded events. It still cannot describe a rotation that never reached the store.

The [pack verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L334-L535) checks the manifest, files, key history, anchored range and linked records. Without independently held anchors, its result is narrower: integrity of the supplied material, not proof that earlier material was never removed. That qualification belongs in the audit finding, even if every available signature passes.

## Compare against independently observed changes

To look for the second kind of gap, the verifier accepts an external change log through `--changes`. An auditor can compare the evidence pack with observations collected outside Genesis Mesh, such as a cloud activity log.

The [audit walkthrough](https://docs.genesismesh.org/operations/audit-verification-walkthrough.html) includes a change that has no corresponding record in the evidence store. Verification reports `change_unmatched`. The [completeness implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/workflows/audit_pack.py#L1068-L1160) and [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_audit_pack.py#L279-L325) show the matching behavior and asserted refusal case; they were inspected, not executed for this article.

For the credential audit, that means collecting the provider's observed rotations for the same resources and period. The external list provides a reason to ask why a rotation has no corresponding evidence, rather than trusting only the controller's account of its own work.

The comparison has limits. If both sources miss a rotation, reconciliation does not discover it. If resource identifiers or timestamps disagree, a mismatch needs investigation. It is not automatically proof of misconduct, and an empty mismatch list is not a universal completeness guarantee.

## Assign responsibility for the missing evidence

An audit procedure should name who obtains anchors, who controls their storage, which source records actual resource changes and who investigates unmatched events. These are parts of the evidence boundary, not administrative details added after cryptographic verification.

Consider two operational failures. If anchors stay only on the authority's host, the auditor has not retained an independent comparison point. If the cloud export excludes one production account, the completeness check cannot establish coverage for changes in that account.

The verifier cannot repair those collection choices. It can report what follows from the supplied inputs. The operator and auditor remain responsible for describing their scope accurately.

The distinction also applies to the records themselves. A valid signature shows that the record verifies under the trusted key and relevant rules. It does not prove that every assertion inside the payload describes reality. Independent observations and the executor's own evidence still matter when assessing what actually changed.

## Use the second verifier with its stated limits

Genesis Mesh provides `genesis-mesh-verify`, a Rust port of its Python verification logic, for offline checks with public verification material. An auditor can compare implementations without giving the verification process a signing key or contacting the production authority.

The [verifier guide](https://docs.genesismesh.org/operations/independent-verification.html) is explicit about the relationship: this is a port by the same project, not a clean-room implementation from an unrelated organization. A disagreement can reveal an implementation problem; agreement cannot rule out a mistake shared by both implementations or their reading of the specification.

That makes the second verifier useful evidence with a defined scope. It does not replace independent anchor custody or the external observations needed to investigate missing changes.

## Check it yourself

Follow the [audit-pack walkthrough](https://docs.genesismesh.org/operations/audit-verification-walkthrough.html). You need a local Network Authority with the evidence store enabled, its independently obtained root key, held anchors and both documented verifier tools.

The procedure verifies an original pack, supplies an external change absent from it, and changes a byte in a copy. Expect the intact pack to verify, the unmatched change to produce `change_unmatched`, and the edited file to produce `manifest_digest_mismatch`.

This documented example was not executed in this review. For your own audit, record the anchor coverage and external-log coverage alongside the verdict so another reader can see exactly what was checked.

## Further reading

- [Audit verification](https://docs.genesismesh.org/operations/audit-verification.html): inputs, checks and bounded results.
- [Audit-pack walkthrough](https://docs.genesismesh.org/operations/audit-verification-walkthrough.html): an intact pack and two failure cases.
- [The Rust verifier](https://docs.genesismesh.org/operations/independent-verification.html): a second implementation and its limitations.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
