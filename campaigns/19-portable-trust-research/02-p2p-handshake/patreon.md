# P2P transport is only half the handshake

**Portable Trust · Part 2 of 6**

*An authenticated connection gives a request a source. The receiver still needs to decide what that source may do.*

Consider an illustrative request: two machines find each other, establish an encrypted connection and exchange identity proofs. One then asks the other to export a customer dataset. The connection works. The export needs a separate decision.

This is a practical distinction in Genesis Mesh, because the transport code, membership checks and application trust boundary answer different questions.

## What the handshake actually checks

The repository contains a [Noise XX handshake over WebSocket](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/transport/noise_handshake.py). The implementation exchanges certificates during the handshake and derives its X25519 transport key from the node's Ed25519 identity. Encryption alone is not the membership check.

The [peer-identity validator](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/node/peer_identity.py) checks the certificate's network name, validity window, revocation against the available local CRL, and the authority signing key. It also binds the certificate identity to the static key used in the Noise session. That binding matters: presenting somebody else's valid certificate should not establish that the current peer owns its identity.

There is a scope limit here. This peer check requires the same network name. The existence of cross-sovereign recognition elsewhere in the project does not make the handshake an arbitrary cross-network federation mechanism. And the [development strategy](https://docs.genesismesh.org/development/strategy.html) identifies the mesh-node transport runtime as dormant. These are concrete implementation paths, not a claim that a production P2P network is currently operating through them.

## Where the receiving application decides

For an application accepting a foreign member, the [trust gateway](https://docs.genesismesh.org/concepts/rust-gateway.html) is a separate boundary. It checks trust artifacts against pinned authority keys, accepted roles, freshness rules and signed revocation state. It does not become another Network Authority, the operator's service that holds authority keys and signs trust records, or acquire that service's signing key.

An HTTP 200 from `/verify` means the verification request was handled. The caller must inspect the returned `trusted` result. It must also bind the verified identity to the authenticated application session; verifying a supplied record does not establish that the caller owns the key in it.

Even a positive trust result does not grant every application operation. The component that can export the dataset must enforce the applicable local authorization decision before performing that export. The [security model](https://docs.genesismesh.org/concepts/security-model.html) documents boundary-policy enforcement and its configuration limits. Leaving optional enforcement disabled must not be described as a policy-protected route.

## Check the decision, not just the signature

The [boundary-decision verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/trust/context/decisions.py) can return `accepted=true` with `authorized=false`: the record is a valid signed deny. Treating every authentic record as permission would erase the distinction the verifier preserves. The repository's [attestation-boundary tests](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/tests/test_attestation_boundary.py) and [boundary-policy tests](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/tests/test_boundary_policy.py) are concrete places to inspect those boundaries. Their presence is not a claim that this article reran the suite or validated a particular deployment.

## Why the research is relevant

[DIAP](https://arxiv.org/abs/2511.11619) brings decentralized identity proofs together with a hybrid peer-to-peer stack. It is useful context for separating discovery, authentication and the exchange that follows. Genesis Mesh is not presented here as a DIAP adapter, and the dataset example is not a vulnerability claim about that paper.

For an integration test, keep the authenticated peer fixed and change the action: permit a status read, refuse a dataset export. Record which membership check ran, which local rule made the authorization decision and which component stopped the export. Then change the accepted trust state and repeat after the receiver has refreshed it. A receiver using an old CRL cannot act on a revocation it has never learned.

## Check it yourself

Use the linked source and its documented setup. Start with the peer-identity validator and follow the certificate-to-static-key comparison. Then inspect the attestation-boundary and boundary-policy tests linked above: distinguish a rejected record from a verified deny. To reproduce the API behavior, use the gateway guide's documented configuration with pinned authority keys, an authenticated caller and accepted roles; inspect `trusted`, not HTTP status alone. Include an untrusted or revoked attestation and confirm the consuming application refuses the action.

This is a documented procedure and source-inspection checklist, not executed in this review. Set up the dependencies and fixtures exactly as the linked repository describes; do not use a production export as the test action.

**Builds on our video** [Genesis Mesh Trust API and SDKs Overview](https://www.youtube.com/watch?v=E2UQRM7c3Vo)

**Go deeper:**

[trust gateway](https://docs.genesismesh.org/concepts/rust-gateway.html)

**Next:** Federation without surrendering local control

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
