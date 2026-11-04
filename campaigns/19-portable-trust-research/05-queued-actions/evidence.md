# Evidence review: Revoked, but still running: the actions that happen too late

Reviewed: 2026-11-04. Original campaign idea: 4. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Decision before effect

A queue admission check and a provider-side enforcement point cover different times. Evidence admission or after-the-fact judgment cannot cancel an already committed provider effect.

Sources: [source 1](https://docs.genesismesh.org/concepts/governed-changes.html), [source 2](https://docs.genesismesh.org/operations/out-of-band-changes.html).

## Governed helper

The documented helper verifies decision bindings, context and expiry, including the recheck after resource-head lookup. A verified denial does not call the action; verification failures raise the documented error.

Sources: [source 1](https://docs.genesismesh.org/sdk/typescript/governance.html), [source 2](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts).

## Outbox semantics

The outbox retries evidence, not the action callback. FileOutbox is single-process-per-directory. A crash during an action requires external reconciliation rather than inferring that no effect occurred.

Sources: [source 1](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/outbox.ts), [source 2](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/evidence_store.ts).

## Coverage

This is one documented governed-client workflow, not a generic queue scheduler. Current capability matrix includes TypeScript, Rust and .NET governed clients, while Go remains a thinner surface.

Sources: [source 1](https://docs.genesismesh.org/sdk/index.html).

## Research scope

The long-running-agent paper’s provider-free, bounded trace evaluation does not establish arbitrary provider cancellation, global idleness, rollback or a Genesis Mesh implementation of its protocol.

Sources: [source 1](https://arxiv.org/abs/2609.21284).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No material correction identified. The cited TypeScript implementation snapshot already contains the behavior released in 1.9.0; no src files changed between that snapshot and checked 1.9.1. “One documented implementation” is an example scope, not a claim that only one client exists. The broader-coverage plan does not contradict the current Go limitation.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |
