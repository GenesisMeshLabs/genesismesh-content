# November 5 editorial revision: P2P transport is only half the handshake

The user requested articles around 900 words, canonical documentation links throughout, and a final Further reading section. This reviewed revision was subsequently saved to the existing Patreon post and verified as recorded below. Source-based review only: no product tests, demonstrations or live actions were executed.

## Current verification and changed claims

Core main and latest release remain a54b2d81f205c9b0203158f846f7ad44dc677063 / v1.9.1; gateway main remains 2e6486ee6a6481adca1be3b9dae70a4ef32036f9 / v1.9.1. The source-release refresh found no new source changes. Current peer_identity.py and trust/context/decisions.py were directly read: the former checks network, validity, local CRL, current key vouching and certificate/Noise binding; the latter distinguishes authentic denials from permission and conditionally checks expected policies/attestation.

The revised gateway paragraph accurately names join-certificate verification, replacing the broader 'foreign member' phrasing. The current canonical gateway guide states beta status, scoped bearer credentials, operator-provided trust inputs, returned trusted result and session/application binding. The attestation-backed guide states that caller authentication remains the relying system's job. The new log/test paragraphs are clearly an illustrative integration proposal, not observed deployment behavior. The DIAP primary abstract was reopened and used only as research context.

The existing Nov5 09:00 Europe/Stockholm schedule was preserved when this revised copy was saved and verified.

The user-supplied [Connect vision](https://claude.ai/artifact/ParjPaubYJkVdkWcaCx4pt) was read in its rendered public iframe on November 5. It separates Connect as the everyday app from Genesis Mesh as the trust layer, preserves independent owner control, and labels the cross-owner document read with exact phone approval as a proposed first proof. Phone-approval screens, production federation between separate operators and a second independent implementation are not asserted as shipped or proven by these articles. This is product-vision context, not implementation evidence.

Canonical documentation pages opened and checked on 2026-11-05:

- [Security model](https://docs.genesismesh.org/concepts/security-model.html)
- [Trust gateway](https://docs.genesismesh.org/concepts/rust-gateway.html)
- [Dormant package scope](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html)
- [Attestation-backed evaluation](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html)

## Exact revised article

The following text binds this claim review to the wording submitted for independent review. It retains the historical evidence inventory below.

# P2P transport is only half the handshake

**Portable Trust · Part 2 of 6**

*An authenticated connection gives a request a source. The receiver still needs to decide what that source may do.*

Consider an illustrative request: two machines find each other, establish an encrypted connection and exchange identity proofs. One then asks the other to export a customer dataset. The connection works. The export needs a separate decision.

This is a practical distinction in Genesis Mesh, because the transport code, membership checks and application trust boundary answer different questions.

## What the handshake actually checks

The [security model](https://docs.genesismesh.org/concepts/security-model.html) separates peer authentication from later authorization. The repository contains a [Noise XX handshake over WebSocket](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/transport/noise_handshake.py). The implementation exchanges certificates during the handshake and derives its X25519 transport key from the node's Ed25519 identity. Encryption alone is not the membership check.

The [peer-identity validator](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py) checks the certificate's network name, validity window, revocation against the available local CRL, and the authority signing key. It also binds the certificate identity to the static key used in the Noise session. That binding matters: presenting somebody else's valid certificate should not establish that the current peer owns its identity.

There is a scope limit here. This peer check requires the same network name. The existence of cross-sovereign recognition elsewhere in the project does not make the handshake an arbitrary cross-network federation mechanism. The [dormant-package decision](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html) marks this runtime internal and maintained for fixes, without new features. These are concrete implementation paths, not a claim that a production P2P network is currently operating through them.

## Where the receiving application decides

For an application verifying a join certificate, the beta [trust gateway](https://docs.genesismesh.org/concepts/rust-gateway.html) is a separate boundary. It checks trust artifacts against pinned authority keys, accepted roles, freshness rules and signed revocation state. It does not become another Network Authority, the operator's service that holds authority keys and signs trust records, or acquire that service's signing key.

With the [documented gateway configuration](https://docs.genesismesh.org/concepts/rust-gateway.html), production callers use a scoped bearer credential; the operator supplies the trust anchors and revocation state. A caller cannot substitute its own trusted issuer simply by including a different key in the request.

An HTTP 200 from `/verify` means the verification request was handled. The caller must inspect the returned `trusted` result. It must also bind the verified identity to the authenticated application session; verifying a supplied record does not establish that the caller owns the key in it.

Even a positive trust result does not grant every application operation. The component that can export the dataset must enforce the applicable local authorization decision before performing that export. The [security model](https://docs.genesismesh.org/concepts/security-model.html) documents boundary-policy enforcement and its configuration limits. Leaving optional enforcement disabled must not be described as a policy-protected route.

## Check the decision, not just the signature

The [boundary-decision verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/decisions.py) can return `accepted=true` with `authorized=false`: the record is a valid signed deny. Treating every authentic record as permission would erase the distinction the verifier preserves. The repository's [attestation-boundary tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_attestation_boundary.py) and [boundary-policy tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_boundary_policy.py) are concrete places to inspect those boundaries. Their presence is not a claim that this article reran the suite or validated a particular deployment.

The same verifier supports expected policy and attestation bindings. When the consuming integration supplies those expectations, it can reject a decision that names the wrong policies or membership record. It must still connect the verified result to the real operation and authenticated requester. The [attestation-backed evaluation guide](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) explicitly leaves caller authentication with the relying system. A decision for one subject must not be borrowed by another session.

## Why the research is relevant

[DIAP](https://arxiv.org/abs/2511.11619) brings decentralized identity proofs together with a hybrid peer-to-peer stack. It is useful context for separating discovery, authentication and the exchange that follows. Genesis Mesh is not presented here as a DIAP adapter, and the dataset example is not a vulnerability claim about that paper.

For a proposed integration test, keep the authenticated peer fixed and change the action: permit a status read, refuse a dataset export. Record which membership check ran, which local rule made the authorization decision and which component stopped the export. Then change the accepted trust state and repeat after the receiver has refreshed it. A receiver using an old CRL cannot act on a revocation it has never learned.

The [Connect vision](https://claude.ai/artifact/ParjPaubYJkVdkWcaCx4pt) puts this boundary into an everyday experience: Connect is the app, Genesis Mesh supplies trust underneath, and independent owners control access. Its first proposed proof is a cross-owner document read approved once for the exact document, version, action and expiry on the owner's phone, with evidence both owners can verify. Phone approval and production federation remain goals to prove, not capabilities established by the transport code discussed here.

## Check it yourself

Use the linked source and its documented setup. Start with the peer-identity validator and follow the certificate-to-static-key comparison. Then inspect the attestation-boundary and boundary-policy tests linked above: distinguish a rejected record from a verified deny. To reproduce the API behavior, use the gateway guide's documented configuration with pinned authority keys, an authenticated caller and accepted roles; inspect `trusted`, not HTTP status alone. Include an untrusted or revoked join certificate and confirm the consuming application refuses the action.

This is a documented procedure and source-inspection checklist, not executed in this review. Set up the dependencies and fixtures exactly as the linked repository describes; do not use a production export as the test action.

## Further reading

- [Security model](https://docs.genesismesh.org/concepts/security-model.html): admission, peer authentication and enforcement boundaries.
- [Trust gateway](https://docs.genesismesh.org/concepts/rust-gateway.html): configuration, verifier results and relying-application responsibilities.
- [Attestation-backed evaluation](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html): the signed decision and its membership binding.
- [Dormant runtime scope](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html): what the reference peer packages support.

For the wider project, visit the [website](https://genesismesh.org/), [documentation](https://docs.genesismesh.org/), [public trust console](https://mesh.genesismesh.org/) and [source repository](https://github.com/GenesisMeshLabs/genesismesh). The console is a trust-interface demonstration, not this dataset-export integration.


## Prior source inventory (reviewed November 4)

# Evidence review: P2P transport is only half the handshake

Reviewed: 2026-11-04. Original campaign idea: 10. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Transport membership

Noise XX over WebSocket and certificate-to-static-key binding are implemented. Certificate network, expiry, authority key and available CRL checks establish a membership boundary, not arbitrary application permission.

Sources: [source 1](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/transport/noise_handshake.py), [source 2](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py).

## Dormant scope

The mesh runtime remains dormant/internal. The same-network peer check is not evidence of general cross-network federation or a deployed production P2P network.

Sources: [source 1](https://docs.genesismesh.org/development/strategy.html), [source 2](https://docs.genesismesh.org/concepts/security-model.html).

## Gateway result

The independent gateway verifies supplied trust material with operator trust inputs. HTTP 200 is not permission; callers inspect trusted, bind identity to their session and enforce action authorization.

Sources: [source 1](https://docs.genesismesh.org/concepts/rust-gateway.html).

## Authentic deny

accepted=true can coexist with authorized=false in a valid signed denial. The article identifies source tests without claiming to have executed them.

Sources: [source 1](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/decisions.py), [source 2](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_attestation_boundary.py), [source 3](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_boundary_policy.py).

## Research scope

DIAP describes decentralized identity proofs and hybrid P2P transport. It is contextual research, not an integration or a demonstrated vulnerability in the paper.

Sources: [source 1](https://arxiv.org/abs/2511.11619).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No material correction identified. Core transport/peer/boundary implementation and the gateway verification implementation did not change between the cited snapshot and the checked current heads. No running deployment or end-to-end reproduction is asserted.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |

## Patreon synchronization

Verified 2026-11-05: the approved revision was saved to the existing [Patreon post](https://www.patreon.com/GenesisMeshLabs/posts/p2p-transport-is-174297160) and reopened. Its rendered body and all 21 links matched the approved source; the cover and public access were preserved. The existing public schedule remains 2026-11-05T09:00:00+01:00 (Europe/Stockholm). LinkedIn remains an unpublished draft.

Approved Markdown SHA-256: `67a069decf78f1d18693f2943300804b5fd4f6416e7beb2bb7c9eaaedc037b00`. Rendered-body SHA-256 after collapsing whitespace: `6489b392f193c5f84a7b66e503f82b77b422ac982ffca4df1d6162b58c817c27`. This is verification of the saved publication copy, not execution of a product example or proof that a scheduled post has been released.
