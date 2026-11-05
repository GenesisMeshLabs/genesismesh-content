# Shared source and release review

Source and GitHub release evidence rechecked 2026-11-05. The six current main commits and six latest releases are unchanged from November 4. This is a source-based review, not a product test run or deployment certification.

| Repository | Inspected commit | GitHub release |
|---|---|---|
| genesismesh | [`a54b2d81f205c9b0203158f846f7ad44dc677063`](https://github.com/GenesisMeshLabs/genesismesh/commit/a54b2d81f205c9b0203158f846f7ad44dc677063) | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | [`8154ca7ac459ffbcd22d35900ca72f8093165bfc`](https://github.com/GenesisMeshLabs/sdk-typescript/commit/8154ca7ac459ffbcd22d35900ca72f8093165bfc) | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | [`ade949888eacd0ccc16126941427e1211f82aec8`](https://github.com/GenesisMeshLabs/sdk-go/commit/ade949888eacd0ccc16126941427e1211f82aec8) | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | [`b67c248717d5d99aca6f4dad320692f3f6c07c69`](https://github.com/GenesisMeshLabs/sdk-rust/commit/b67c248717d5d99aca6f4dad320692f3f6c07c69) | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | [`241d99b7508b378ce7c613dfc0baeed7cc5df56c`](https://github.com/GenesisMeshLabs/sdk-dotnet/commit/241d99b7508b378ce7c613dfc0baeed7cc5df56c) | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | [`2e6486ee6a6481adca1be3b9dae70a4ef32036f9`](https://github.com/GenesisMeshLabs/gateway/commit/2e6486ee6a6481adca1be3b9dae70a4ef32036f9) | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |

On 2026-11-04, the public package registries independently confirmed version 1.9.1 for [genesis-mesh on PyPI](https://pypi.org/project/genesis-mesh/1.9.1/), [genesis-mesh-sdk on npm](https://registry.npmjs.org/genesis-mesh-sdk) and [genesismesh-sdk-dotnet on NuGet](https://api.nuget.org/v3/registration5-gz-semver2/genesismesh-sdk-dotnet/1.9.1.json). Those registry observations have not been refreshed on November 5. GitHub release tags resolve to the inspected commits. Rust SDK distribution uses Git; its edge/verifier binaries and gateway release binaries are recorded in their release pages, not inferred to exist on crates.io.

The [SDK matrix](https://docs.genesismesh.org/sdk/index.html), reopened on 2026-11-05, distinguishes the governed clients from Go's narrower wrapper surface. .NET governed-client support shipped in 1.9.0. Some older documentation paragraphs still describe the earlier scope. Each article's evidence ledger identifies the implementation it actually uses; no cross-language parity is inferred from coordinated version numbers.

The website and public trust console were opened again on 2026-11-05 without signing in or taking product actions. The website's marketing copy still mentioned 1.8.1, and the console displayed Operational Ready and runtime 1.9.0. The separately checked GitHub releases remain 1.9.1; the package registry observations above are dated November 4. Page availability and status labels do not prove a scenario was executed or that all current source is deployed. No live demo scenario was run during this review.

The four video links retained by the existing six articles were also opened on 2026-11-04. Each page displayed the expected title and a playable YouTube player: [Trust API and SDKs](https://www.youtube.com/watch?v=E2UQRM7c3Vo), [Edge Infrastructure](https://www.youtube.com/watch?v=J7OpYQy3ZkU), [Signed Records](https://www.youtube.com/watch?v=gp5yqnNQdZI), and [Portable Trust Across Boundaries](https://www.youtube.com/watch?v=y3GBM5h-RdY). This checks link availability, not the execution of a current product demonstration.

The Rust 1.9.1 [security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) concerns undated records verified against key history. The corresponding TypeScript issue was fixed in 1.9.0. These version-specific findings remain in the source ledger; articles avoid turning a pinned example into an unqualified latest-version guarantee.

For every package, the distinction remains: documentation describes a workflow, inspected implementation shows code, tests establish asserted cases, and an executed run would establish only that run's outcome. The documented examples in these articles were not executed for this editorial review.

## Publication-copy verification

On 2026-11-05, the six existing Patreon copies were saved and reopened after the approved editorial updates. Rendered text and ordered links matched the approved source for each post; public access, covers, titles and existing URLs were preserved. The two published posts remain live, and the four scheduled posts retain their recorded Europe/Stockholm release times. Per-package review records contain the source and normalized rendered-text hashes. This checks the saved publication copy, not execution of any product example or a future scheduled release. LinkedIn remains unpublished.
