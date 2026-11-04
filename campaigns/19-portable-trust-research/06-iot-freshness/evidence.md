# Evidence review: Offline IoT trust has a freshness budget

Reviewed: 2026-11-04. Original campaign idea: 13. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Device and authority

The enrolled device keeps separate node/executor keys. Applications perform effects after consulting the local agent. Grants require the evidence feature switches and remain beta routes.

Sources: [source 1](https://docs.genesismesh.org/operations/edge-agent.html), [source 2](https://docs.genesismesh.org/operations/grants.html).

## Freshness defaults

The runbook documents a 60-second connected sync interval, one-day default snapshot limit and roughly five-minute clock assumption. Signed source times determine freshness; these are defaults/assumptions, not a universally safe budget.

Sources: [source 1](https://docs.genesismesh.org/operations/edge-agent.html).

## Exceptional path

Stale snapshots stop grant use but do not prohibit every justified exceptional action. Genuine NA errors differ from unreachable/proxy failures; explicit denial and out-of-envelope requests remain refused.

Sources: [source 1](https://docs.genesismesh.org/operations/edge-agent.html), [source 2](https://github.com/GenesisMeshLabs/sdk-rust/blob/b67c248717d5d99aca6f4dad320692f3f6c07c69/edge/src/decision.rs).

## Reconnect

Revocation becomes locally knowable on synchronization. Durable evidence delivery and later refusal do not undo physical effects. Simulation and hardware safety claims remain distinct.

Sources: [source 1](https://docs.genesismesh.org/operations/edge-agent.html).

## Research scope

The ESP32-class connectivity-aware research uses qualitative attack scenarios and leaves full quantitative evaluation for later. It is not a Genesis Mesh hardware benchmark.

Sources: [source 1](https://d2j16w31g89z0j.cloudfront.net/site/icoin2026/abs/P1-27.pdf).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No material correction identified. The edge implementation is explicitly unaffected by the missing-record-time advisory. The article correctly qualifies freshness with the break-glass path and clock assumptions and reports no physical tests.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |
