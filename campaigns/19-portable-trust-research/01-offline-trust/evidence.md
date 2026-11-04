# Evidence review: Offline trust and revocation: what a disconnected system can know

Reviewed: 2026-11-04. Original campaign idea: 1. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Bounded issuance

The four-hour, three-use credential-rotation example, two uses per time token, and integer 1–60-day envelope are documented. The policy issuer checks the complete permitted envelope; a per-request external attribute cannot simply be assumed safe.

Sources: [source 1](https://docs.genesismesh.org/examples/pre-issued-grants.html), [source 2](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/grants.py).

## Offline use and fallback

The inspected holder checks scope, parameters, validity, known revocations, key horizon and budgets. Configured break-glass remains distinct from grant authority. Resource/parameter mismatch does not justify fallback; a returned deny is not an outage.

Sources: [source 1](https://github.com/GenesisMeshLabs/sdk-rust/blob/b67c248717d5d99aca6f4dad320692f3f6c07c69/src/grant_holder.rs), [source 2](https://docs.genesismesh.org/operations/grants.html).

## Edge-specific classification

A genuine NA 429/5xx permits a covering grant, not break-glass. Unreachable authority includes the documented proxy-error exceptions. A held grant excluding parameters/resource blocks the exceptional route.

Sources: [source 1](https://github.com/GenesisMeshLabs/sdk-rust/blob/b67c248717d5d99aca6f4dad320692f3f6c07c69/edge/src/decision.rs), [source 2](https://docs.genesismesh.org/operations/edge-agent.html).

## Time and reconciliation

Signed tokens and small budgets constrain offline use without proving an honest clock. Quarantine, chain placement and admission counts differ. Later rejection does not undo an external effect.

Sources: [source 1](https://docs.genesismesh.org/operations/grants.html#time), [source 2](https://docs.genesismesh.org/operations/grants.html#a-refused-use-keeps-its-place).

## Independent verification limit

The Rust audit verifier is a same-project port. Independently retained keys, anchors and external change records matter; agreement between implementations cannot eliminate shared mistakes.

Sources: [source 1](https://docs.genesismesh.org/operations/independent-verification.html).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No new operational contradiction found. The Rust security fix hardens undated record verification; it does not change this article’s bounded grant example or the standalone verifier/edge behavior. Preserve the distinction between the historic source revision examined in the article and current supported releases.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |
