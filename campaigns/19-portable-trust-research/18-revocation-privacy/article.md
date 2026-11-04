# Revocation is a privacy problem too

An organization revokes credentials when devices are retired, people leave or keys are compromised. A partner needs that information to stop accepting access. An observer may also learn something from the identifiers, reasons and timing of the updates.

In this illustrative case, the security team wants prompt revocation without publishing an unnecessary picture of internal operations. Those are two requirements, and solving one does not automatically solve the other.

[CRSet](https://arxiv.org/abs/2501.17089) studies non-interactive credential revocation with protection for issuer activity. Its published design lets relying parties obtain encoded status material and check it locally. It is a research mechanism with its own assumptions and implementation, not a Genesis Mesh feature claimed here.

## See what the revocation record reveals

Genesis Mesh's Network Authority is the operator's service that issues and revokes membership credentials. Its [revocation runbook](https://docs.genesismesh.org/operations/revocation.html) describes a privileged operator revoking a certificate, the authority publishing an updated signed certificate revocation list, and the authority refusing that certificate's heartbeat and renewal.

The [CRL model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) contains an issuer, sequence, issue time, next-update time and revoked entries. Each entry includes a certificate identifier, revocation time, reason and issuer. The signature lets a consumer check who signed that status material; it does not conceal those fields.

A privacy review should therefore inspect the material recipients actually receive, the places it is retained and the other records with which it can be combined. Whether a certificate identifier identifies a person depends on the surrounding system. It should not be treated as anonymous merely because it is an opaque string.

There is a subtlety when interpreting activity: a new sequence does not necessarily mean another credential was revoked. The [authority tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) cover refreshing an expiring CRL with a higher sequence and the same revoked entries. Counting sequence changes as staff departures would be an unsupported inference.

## Local checks still have an age

For a peer connection, the receiver checks the certificate against the revocation state it holds. The [peer identity implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py) rejects a certificate found in that state. It cannot use an update it has never received.

Other records have their own propagation paths. A partner's membership-attestation revocation reaches a sovereign when its feed is imported. A grant revocation reaches an offline holder at its next sync. The runbook distinguishes these paths; a certificate CRL is not a universal revocation channel.

The design question is consequently broader than "online or offline?" It includes which status data is fetched, how old it may be, what the consumer does when refresh fails and what the fetch or published data reveals. Caching may reduce individual requests, but it does not erase visible metadata or create immediate knowledge of a new revocation.

No issuer-activity hiding, private status query or CRSet integration is established by the Genesis Mesh CRL flow described here. Adding such a mechanism would require a separate design and verification effort, including how it interacts with freshness and local authorization.

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html) and inspect the CRL route tests:

```text
python -m pytest genesis_mesh/tests/test_na_crl.py -v
```

The fixtures enroll a node, revoke its certificate and expect the published list to contain that certificate. Heartbeat and renewal are then refused. Another test refreshes an expiring list without changing its revoked entries. This source-based test procedure was not executed in this review.

For an operational review, compare the before-and-after JSON and note exactly which fields reveal changes. Do that in a test authority with synthetic identities, then decide which recipients need that information. The useful privacy question is what each recipient can infer from the status material your enforcement depends on.

[Website](https://genesismesh.org/)  |  [Documentation](https://docs.genesismesh.org/operations/revocation.html)  |  [Public console](https://mesh.genesismesh.org/)  |  [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)
