# Revocation is a privacy problem too

An organization revokes a departing contractor's credential. Its partner needs the update to stop accepting access, while an observer may learn something from the timing and identifiers. This illustrative case has both an enforcement requirement and a privacy question.

[CRSet](https://arxiv.org/abs/2501.17089) studies non-interactive revocation with issuer-activity privacy; that research mechanism is not a Genesis Mesh feature claimed here.

## A signature does not conceal status

Genesis Mesh's Network Authority is the operator's service for issuing and revoking membership credentials. The [revocation runbook](https://docs.genesismesh.org/operations/revocation.html) describes a privileged operator revoking a certificate, publication of a signed certificate revocation list, and refusal of the revoked certificate's heartbeat and renewal.

The [CRL model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) exposes issuer, sequence, issue time, next-update time and revoked entries. Each entry contains certificate ID, revocation time, reason and issuer. Signing authenticates that material; it does not hide it. An opaque identifier may still be linkable to other records.

Sequence changes also need careful interpretation. The [authority tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) refresh an expiring list with a higher sequence but unchanged revoked entries. A sequence increment is not necessarily another departure or compromise.

A receiving peer checks the revocation state it holds. It cannot enforce an update it has not received. This flow establishes neither private status queries nor issuer-activity hiding; caching alone does not erase visible metadata.

## Check it yourself

Use synthetic identities in a disposable [development installation](https://docs.genesismesh.org/installation.html):

```text
python -m pytest genesis_mesh/tests/test_na_crl.py -v
```

The fixtures enroll and revoke a node: its certificate should appear in the list, and heartbeat and renewal should return refusal. A separate test refreshes the list without adding revocations. Compare the before-and-after fields. This source-based test procedure was not executed in this review.

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/operations/revocation.html) | [Public console](https://mesh.genesismesh.org/) | [Source](https://github.com/GenesisMeshLabs/genesismesh)
