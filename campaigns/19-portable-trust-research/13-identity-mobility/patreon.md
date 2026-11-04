# Identity should survive a network move

An inventory agent moves from a developer's laptop to an edge machine, then into a cloud service. Its address changes each time. Should every move create a new trust relationship?

In this illustrative scenario, the operator wants continuity without confusing "the same name" with "the same authorized actor." The destination still needs to know which keys stand behind the identity, whether their credentials remain valid, and what this particular request may do.

The proposed [Agent Identity URI Scheme](https://arxiv.org/abs/2601.14567) studies topology-independent names and capability discovery. It is useful research context for separating identity from location. Genesis Mesh does not claim to implement that paper's `agent://` scheme or its discovery system.

## Keep the anchor separate from the address

Genesis Mesh makes this distinction explicitly at the trust-domain level. A sovereign is an independently administered trust domain. Its Network Authority is the operator's service for issuing membership credentials and publishing trust material.

The [sovereign identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) gives the domain a stable `sovereign_id`. Its `endpoint` is a reachability hint, not permission to trust whatever answers there. A consumer checks the identity's trust fields against the root-signed genesis block and starts from a root key it already has a reason to trust.

There is an easily missed detail: `GET /sovereign.json` returns an unsigned identity document. Its descriptive fields are not an alternative signature. The [actual public route](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) publishes the domain information; the signed genesis material provides the cryptographic anchor. An endpoint change and a root-key replacement are very different events.

## A node needs current credentials too

A node's identity is a separate layer. In the reference peer runtime, a node announces its endpoint alongside a join certificate and signs its announcement with the node key. The receiver checks the certificate, its network and validity, known revocation state, and the announcement signature. Roles come from the certificate rather than the sender's preferred description. A connection also binds the certificate key to the Noise handshake key. These are [implemented checks](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py), not a request for another model to decide whether the sender sounds familiar.

Certificate renewal illustrates why continuity needs fresh evidence. The [renewal tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_peer_identity_renewal.py) keep the node public key unchanged while replacing its certificate. A peer holding the superseded certificate and the updated revocation list treats it as revoked; receiving the renewed certificate in a valid announcement restores recognition. The old certificate is still refused on its own.

This does not provide automatic workload migration. The operator remains responsible for moving or reprovisioning keys securely, removing old access paths and preventing unintended duplicate holders. The peer runtime is maintained for fixes, with [no new features planned for those internal packages](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html). Its checks demonstrate a specific implementation, not a universal migration API.

## Check it yourself

Use a disposable development checkout with the [documented Python and development dependencies](https://docs.genesismesh.org/installation.html). Run:

```text
python -m pytest genesis_mesh/tests/test_peer_identity_renewal.py -v
```

The source tests exercise unchanged node keys, a revoked predecessor certificate and recovery after a valid renewed announcement. Expect the stale-certificate case to be refused and the renewed announcement to restore the certified role. This is a source-based test procedure, not executed in this review.

For a domain-level check, inspect `/sovereign.json` and `/genesis` on an authority you operate. Compare their identity fields and verify the genesis signature using your trusted root. A new address must not silently become a new trust anchor.

Stable identity makes history easier to follow. Permission still belongs at the receiving system's boundary. Start a migration review by listing separately what changes: address, process, node key, certificate, trust root and authorization.

[Website](https://genesismesh.org/)  |  [Documentation](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html)  |  [Public console](https://mesh.genesismesh.org/)  |  [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)
