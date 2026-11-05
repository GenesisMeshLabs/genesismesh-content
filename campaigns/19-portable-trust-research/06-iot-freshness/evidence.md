# November 5 editorial revision: Offline IoT trust has a freshness budget

The user requested articles around 900 words, canonical documentation links throughout, and a final Further reading section. This reviewed revision was subsequently saved to the existing Patreon post and verified as recorded below. Source-based review only: no product tests, demonstrations or live actions were executed.

## Current verification and changed claims

Current source/release refresh confirms core a54b2d81f205c9b0203158f846f7ad44dc677063, Rust SDK/edge b67c248717d5d99aca6f4dad320692f3f6c07c69 and published v1.9.1 unchanged. The edge-agent runbook was reopened on November5 and remains explicitly beta. Existing claims distinguish NA429/5xx from unreachable proxy errors, grants from break-glass, explicit DENY and out-of-envelope refusal, signed snapshot freshness, and later evidence admission from physical execution. No universal SDK fallback behavior or hardware safety property is inferred.

The revision adds beta beside the edge-agent introduction, repeats precise canonical links at the failure discussion and ends with a further-reading section. Scenarios remain proposed simulator checks, not executed product/hardware tests. Patreon synchronization is verified below.

Canonical documentation pages opened and checked on 2026-11-05:

- [Edge agent](https://docs.genesismesh.org/operations/edge-agent.html)
- [Pre-issued grants](https://docs.genesismesh.org/operations/grants.html)
- [Break-glass](https://docs.genesismesh.org/operations/emergency-changes.html)

## Exact revised article

The following text binds this claim review to the wording submitted for independent review. It retains the historical evidence inventory below.

# Offline IoT trust has a freshness budget

**Portable Trust · Part 6 of 6**

*A disconnected device needs an explicit limit on how old its authority information may become.*

Consider an illustrative outage: an edge controller has a valid credential and a cached grant, but no connection to its authority. Its next request could read a sensor or change a physical resource. A valid signature cannot tell the device about a revocation issued after the last connection.

Before an outage, the operator needs to specify which actions may proceed, for how long and on what evidence. Credential validity, grant expiry and revocation freshness answer different parts of that question.

## What runs on the device

The [Genesis Mesh edge-agent runbook](https://docs.genesismesh.org/operations/edge-agent.html) documents a beta edge agent that runs on a node. It enrolls with a one-time invite and keeps separate node and executor keys on the device. Local services ask it about a requested action; the services still perform the external change.

While connected, the agent asks the Network Authority, the operator's service that signs trust decisions, for a decision scoped to its node. When current authority cannot be obtained, a pre-issued grant can cover a bounded request. The [grant runbook](https://docs.genesismesh.org/operations/grants.html) defines the bearer, capabilities, validity interval, parameter envelope and maximum uses. Signed time tokens and chained use records support later verification. Grants and their evidence prerequisites require operator configuration and are off by default; the grant routes are beta.

The edge agent holds a snapshot of revocation information. Its documented default maximum age is one day, with a normal synchronization interval of 60 seconds and a clock assumption within roughly five minutes of the authority. These are implementation defaults and assumptions, not a safety certification or a recommended budget for every device. Snapshot freshness derives from its signed times, rather than treating a download time as proof that the information was newly issued.

When the snapshot is stale, the agent stops using grants. That is a concrete freshness boundary worth testing. It also means the operator must inspect the exceptional route before claiming that every action stops there.

## Break-glass is a separate decision

The [edge-agent failure rules](https://docs.genesismesh.org/operations/edge-agent.html) have their own classification, so a controller's fallback behavior must not be assumed to apply to it. An NA 429 or 5xx response is treated as throttled or failing, allowing a covering grant but not break-glass. There is a specific exception: a proxy's 502, 503, 504 or 520–527 page without the NA's JSON error body is classified as unreachable, alongside connection, DNS, TLS and timeout failures. A suitable grant may cover the gap. An explicit deny cannot be overridden by a grant or break-glass.

When the authority is actually unreachable and no usable grant covers the action, a caller's justification may permit [exceptional execution](https://docs.genesismesh.org/operations/emergency-changes.html) under the documented rules. Requests that fall outside a matching grant's scope remain refused. A hard requirement to stop on stale authority must therefore be checked at the precise local action boundary, including the exceptional route, rather than inferred from grant expiry alone.

The edge agent records activity in a durable outbox for later submission. Revoking a node at the authority also ends the associated authority that the runbook describes, including its grants and executor registration. The disconnected device learns the new state at its next synchronization. Refusing its later evidence cannot stop a physical effect it already produced while offline.

## Put the research beside the implementation

[Connectivity-Aware Hybrid Access Control for Low-Power IoT Devices](https://d2j16w31g89z0j.cloudfront.net/site/icoin2026/abs/P1-27.pdf) explores connectivity states and TTL-based freshness on an ESP32-class design. Its evaluation is qualitative, with quantitative performance work left for later. This is research context, not a Genesis Mesh hardware benchmark.

A safe simulator can vary the last signed snapshot, expire a grant, exhaust its use budget, replay old revocation information and change the local clock. Record whether each request waits, proceeds under a grant or uses break-glass. Reconnect and inspect the authority's later verdict separately from the effect.

These tests are proposed here, not reported hardware results. Real physical systems need independent safety engineering and protections. The trust layer can help make the authority budget explicit; it cannot decide which physical action is safe or deliver revocation information across a disconnected link.

## Check it yourself

Follow the linked edge-agent runbook's documented enrollment and local-service setup in a simulator. Enable `EVIDENCE_STORE=on` and `EVIDENCE_OUT_OF_BAND=on`, plus `EVIDENCE_GRANTS=on` for grants, all off by default. Pin the NA genesis root key and use HTTPS as documented. Use the guide's grant and evidence prerequisites and record the configured snapshot-age limit, grant envelope and use budget. Exercise the documented connected, grant and exceptional paths separately: explicit deny, NA 429/5xx, unreachable authority and stale signed snapshot are different cases. Include an out-of-envelope request with a justification and verify that the request is still refused.

This is a documented procedure with proposed simulator cases, not executed in this review. Reconnect and inspect evidence admission separately from the simulator's action log. No physical actuator or production resource is required to examine these trust boundaries.

## Further reading

- [Edge-agent runbook](https://docs.genesismesh.org/operations/edge-agent.html): device keys, snapshots, failure classification and reconnect behavior.
- [Pre-issued grants](https://docs.genesismesh.org/operations/grants.html): scope, time tokens, use budgets and evidence admission.
- [Emergency changes and break-glass](https://docs.genesismesh.org/operations/emergency-changes.html): exceptional changes and the later judgment.

Explore the [website](https://genesismesh.org/), [documentation](https://docs.genesismesh.org/), [public trust console](https://mesh.genesismesh.org/) and [source repository](https://github.com/GenesisMeshLabs/genesismesh). The console is not an offline hardware demonstration. Choose the freshness budget for the actual operation and test its refusal path before deployment.


## Prior source inventory (reviewed November 4)

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

## Patreon synchronization

Verified 2026-11-05: the approved revision was saved to the existing [Patreon post](https://www.patreon.com/GenesisMeshLabs/posts/offline-iot-has-174297309) and reopened. Its rendered body and all 12 links matched the approved source; the cover and public access were preserved. The existing public schedule remains 2026-11-06T16:00:00+01:00 (Europe/Stockholm). LinkedIn remains an unpublished draft.

Approved Markdown SHA-256: `e2518dd0f507de054979a69b8aa5abeafb2542785ad39d31f8a0325087f3db3b`. Rendered-body SHA-256 after collapsing whitespace: `4aad929fa5aeaaf1a807b67f886bf1987f618bff42c3a106be030754c21fd005`. This is verification of the saved publication copy, not execution of a product example or proof that a scheduled post has been released.
