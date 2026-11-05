# Revocation is a privacy problem too

A contractor leaves a project, and the operator revokes its access certificate. That is the right security action. But suppose an outside observer watches the organization's revocation data over time. Even without a person's name, changing identifiers, reasons and timestamps may reveal patterns of activity. This illustrative case asks two questions: will the revoked credential be refused, and what does publishing that refusal reveal?

[CRSet research](https://arxiv.org/abs/2501.17089) studies private, non-interactive credential revocation, including the risk that revocation activity exposes information about an issuer. Genesis Mesh does not claim to implement CRSet. Its signed certificate revocation list provides a concrete way to examine the difference between authentic revocation information and private revocation information.

## Follow one certificate withdrawal

A Genesis Mesh Network Authority is the operator's service for membership credentials and trust material. The [revocation runbook](https://docs.genesismesh.org/operations/revocation.html) describes an operator-authenticated `POST /admin/revoke` request. It requires a privileged operator key; possession of the certificate being revoked is not administrative authority to change the domain's revocation state.

The operator identifies the certificate and gives a reason. The authority marks the certificate revoked, produces a new certificate revocation list, increments its sequence and signs it. The active list is available through `GET /crl`. The [route implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/crl.py) serializes the active signed CRL for readers.

The authority then refuses heartbeat and renewal requests using the revoked certificate. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) exercise both refusal paths and check that the certificate identifier appears in the CRL. This is an inspectable local consequence of the operator's decision, not merely a note in an incident document.

Other participants need the relevant state before they can enforce that withdrawal. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes peer certificate checks against known revocation state. A participant using an older copy cannot learn a new withdrawal from a signature alone. Authenticity and freshness are different properties of the information it has.

## Inspect the public fields

The [CRL model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) exposes the list identifier, sequence, issue time, next-update time and issuer. Each revoked-certificate entry contains a certificate identifier, revocation time, reason and issuer. The authority's signature lets a consumer check the signed content. It does not encrypt those fields.

For the departing contractor, the certificate identifier need not contain a human-readable name to be linkable. A recipient may already have seen that identifier during a previous interaction. Matching the later CRL entry to that earlier observation can reveal that the same credential was withdrawn. This is an inference from visible metadata, not a claim that every observer can identify every holder.

The reason field can add context. The [runbook](https://docs.genesismesh.org/operations/revocation.html) distinguishes reasons such as key compromise and cessation of operation. Operators should select an accurate reason because these choices have operational meaning; the privacy question is what recipients can infer from the reason and its timing. Replacing a meaningful reason with an inaccurate one is not a sound privacy mechanism.

Counting sequence changes also needs care. The [refresh test](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) shows a quiet authority republishing an expiring CRL with a higher sequence and unchanged revocation entries. A new sequence therefore does not necessarily mean another certificate was revoked. Comparing the actual entries supports a more precise observation than treating every refresh as new organizational activity.

## Local checking is not automatically private checking

Downloading a signed list can support local verification of the information already obtained. It does not erase the contents of that list, prevent recipients from retaining earlier copies or hide information that an observer can correlate with another source. The [CRL representation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) remains explicit about the revoked entries.

That makes the operator's privacy review different from the signature review. A valid signature answers who signed these bytes and whether they were altered. It does not answer whether the bytes reveal more than the recipient needs. Likewise, an accurate timestamp can be useful for investigation while also contributing to an activity pattern.

The receiving service still owns its admission and resource decisions. It should verify the relevant trust material, apply the state it knows and avoid presenting an old copy as evidence of fresh permission. A disconnected verifier cannot promise immediate knowledge of a new revocation. These operational limits remain even if the certificate identifier looks opaque.

CRSet addresses a separate design objective around issuer activity. Its research results should prompt explicit requirements, not an assumption that a signed Genesis Mesh CRL has the same privacy properties. If a deployment requires private non-revocation proofs or concealed revocation activity, that requirement remains unmet by the inspected CRL mechanism.

For the contractor's operator, a practical review would keep the authorized withdrawal, the resulting signed list and the observed refusal together. It would also inventory who can retrieve or retain that list. This separates evidence that access was withdrawn from the broader privacy question of what outsiders learn. Both deserve review, and neither should be inferred from the other.

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html) with synthetic identities. Read and run the source-based CRL checks:

```text
python -m pytest genesis_mesh/tests/test_na_crl.py -v
```

Inspect the CRL before and after the fixture revokes a certificate. Expected results include the new entry and refused heartbeat and renewal. Then inspect the quiet-refresh test: its sequence increases while the entries remain equal. Compare what a verifier needs with every field a recipient can see. These tests were inspected, not executed in this review.

## Further reading

- [Certificate revocation runbook](https://docs.genesismesh.org/operations/revocation.html)
- [Membership and revocation security model](https://docs.genesismesh.org/concepts/security-model.html)
- [CRSet privacy research](https://arxiv.org/abs/2501.17089)

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/) | [Public demo](https://mesh.genesismesh.org/) | [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
