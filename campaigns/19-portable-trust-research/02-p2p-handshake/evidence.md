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
