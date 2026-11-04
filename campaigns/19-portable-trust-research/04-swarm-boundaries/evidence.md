# Evidence review: A swarm needs boundaries, not just coordination

Reviewed: 2026-11-04. Original campaign idea: 9. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Product boundary

Signed authority and execution records do not make Genesis Mesh a swarm scheduler. A task assignment and an enforceable resource permission remain separate.

Sources: [source 1](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/VISION.md), [source 2](https://docs.genesismesh.org/concepts/governed-changes.html).

## Delegation

Capability/validity attenuation and signatures at each hop are documented. Root agreement and the exact action still require their own verification.

Sources: [source 1](https://docs.genesismesh.org/examples/delegation-chain.html).

## Mediation limits

The guard is mandatory only if alternative credential, subprocess and network paths are removed. Its token budget is process-local and resets on restart; no network calls means no newly learned revocation. This is not kernel or hardware attestation.

Sources: [source 1](https://docs.genesismesh.org/examples/process-level-mediation.html).

## Evidence and availability

Supported governed clients obtain decisions and report execution. Signatures do not prove an uncompromised agent or a complete account of effects. Client coverage differs, as the current matrix records.

Sources: [source 1](https://docs.genesismesh.org/sdk/index.html), [source 2](https://docs.genesismesh.org/concepts/security-model.html).

## Research scope

AgentNet studies decentralized coordination and changing task graphs. The article does not claim an AgentNet integration or that those coordination results prove tool-boundary authorization.

Sources: [source 1](https://arxiv.org/abs/2504.00587).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No material correction identified. The exact published body uses the current documentation links. “Broader client coverage is planned” does not identify .NET as future work or claim universal present parity; Go remains a thin client in the current matrix. The statement retains the campaign’s stated future direction without promising timing.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |
