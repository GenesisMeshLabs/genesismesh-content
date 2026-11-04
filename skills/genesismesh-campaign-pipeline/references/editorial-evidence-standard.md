# Editorial and Evidence Standard

This is a required release gate for every new or materially revised Genesis Mesh campaign, including titles, articles, Patreon posts, narration, captions, diagrams, and social copy. It does not certify existing campaigns. A persuasive draft is not a verified product description.

## 1. Substance before length

Lead with a concrete operator problem, explain the mechanism, show what a reader can inspect or try, and state the limits. Each article must contain:

1. A specific situation, actors, resource, authority boundary, and failure or decision. Mark invented scenarios as illustrative; do not imply a customer deployment.
2. A real Genesis Mesh flow: inputs and prerequisites, exact supported surface, responsible authority, signed artifacts or decision output, and the consuming system's next action.
3. At least one failure, denial, revocation, stale-state, or recovery path relevant to that flow.
4. Evidence beside material technical claims, a practical “Check it yourself” section, and a useful call to action.
5. What the mechanism does **not** establish. Verification is not authorization; authorization is not execution; a signature is not evidence that an action is safe or that its payload is true.

A useful long-form starting range is 900–1,600 words, with shorter focused notes and longer technical walkthroughs when warranted. Word count is guidance, never a quality gate or permission to pad. A short announcement can link to a substantive verified walkthrough; it cannot replace evidence with slogans.

Explain the Network Authority on first use. Keep portable trust for sovereign systems as the frame; agents are one application. Show who owns keys, who recognizes whom, who decides, who executes, and who verifies. Do not attribute local authority to a gateway or imply that Genesis Mesh chooses who deserves trust.

### Evergreen public articles, precise internal evidence

Generally describe capabilities without naming individual SDKs or version numbers in public-facing campaign prose, unless the user requests them or omission would create material ambiguity. Keep the article focused on the real flow, prerequisites and limits. Precise code/docs/test links can carry revision detail without version numbers in the narrative.

Keep SDK/platform coverage, full revisions, package versions and dated release checks in the internal evidence ledger. These checks remain mandatory; evergreen wording is not permission to hide availability gaps. Distinguish implemented capabilities from planned broader parity. Where coverage is partial, use a bounded statement such as “available in supported integrations; broader coverage is planned” only when evidence supports both parts. Do not turn “some implementations” into “all SDKs.” If a reader could reasonably assume unsupported behavior, clarify the scope and name the implementation or version only as much as necessary.

## 2. Research claims and product claims are different

- **Research:** cite the original paper, incident report, advisory, or primary dataset; record its date, scope and limitations. Separate a reported finding from our inference. Do not turn a theoretical property into a deployed guarantee.
- **Product:** inspect the actual implementation and applicable tests at a pinned revision. Vision, strategy, roadmap, and prior campaign copy support positioning, not implementation claims.
- **Formal methods:** identify the model, theorem/property, assumptions, tool/version and checked scope. A proof of a model is not a proof of all implementation, deployment or operational behavior.
- **Security incidents:** separate documented incident facts, an illustrative Genesis Mesh response, and residual risk. Never claim the product would have prevented an incident without evidence for that exact threat and deployment.
- **Performance, scale and interoperability:** cite reproducible measurements or named test vectors, versions, environment and limits. Never infer “all languages,” “production-ready,” “instant revocation,” or “zero downtime” from a successful example.

## 3. Pin evidence and classify every material claim

Create `evidence.md` beside the campaign. Keep unreleased/private source details in an ignored local review packet until approved for public disclosure. Public copy and citations must use reader-accessible sources.

Record the review date and full commit SHA for each source repository, package/release versions, and the intended publication date. Use immutable code/docs/test links (`blob/<full-SHA>/path#Lx-Ly`) for claims; a moving branch, repository homepage, screenshot or roadmap alone is insufficient. Verify paths and line ranges; never invent permalinks. Recheck current release/deployment status before publication.

Use one ledger entry per material claim:

```text
Claim ID and exact wording:
Affected assets/sections:
Surface and runtime/package version:
Availability: released | merged but unreleased | in flight | proposal | unknown
Release tag/artifact and deployment evidence (if claiming hosted availability):
Implementation permalink and relevant symbol/route:
Documentation permalink and version:
Test permalink and what it asserts:
Observed verification: command, revision, environment, date, result, log/artifact
Limitations, defaults, opt-ins, permissions and counterexamples:
Reader-accessible source/check-it-yourself link:
Reviewer and decision: verified | qualify | remove | blocked
```

Distinguish these evidence levels explicitly:

- **Documented:** documentation describes it; implementation has not been established.
- **Implemented:** inspected code contains it; release availability or execution may remain unverified.
- **Test-covered:** a test asserts it; this alone does not mean the test ran successfully.
- **Tested:** a named run passed against the stated revision and environment. State whether unit, integration, conformance, demo or live-deployment testing.

“Released” requires a release artifact/tag and version evidence, not a merge or an open PR. “Live” additionally requires evidence for the deployed environment. State in-flight work as in flight, not present-tense product behavior. If a source is inaccessible or contradictory, narrow or remove the claim and keep the relevant release gate blocked.

## 4. Inventory all relevant surfaces before writing

Start from the upstream repository's current manifests, public-surface contract, source tree and release artifacts. Do not assume last month's SDK list or feature parity. Add a row to `evidence.md` for every relevant surface, including unsupported or unverified rows:

- Network Authority HTTP/API and signed artifact formats.
- Gateway routes, authentication, forwarding/proxy behavior and operational boundaries.
- CLI and operator/admin workflows.
- Every maintained SDK language/package and any language-specific omissions or defaults.
- Edge runtime/device client, online authorization, offline grants, record admission and reconciliation.
- Demo applications, fixtures, conformance harness and deployment examples.

For each row, record exact package/version or revision, operation, code/docs/test links, release status, and known gaps. Mark an omitted surface “not relevant” with a reason. A shared name or protocol does not prove equivalent behavior across implementations. Do not say “the SDKs support…” unless the implied scope is verified. In public prose, describe the bounded capability and distinguish planned expansion without listing SDK names or versions by default; retain the exact verified language/version matrix internally. Name an implementation or version publicly only when needed to avoid material ambiguity or requested by the user.

Use real, inspected flows to ground the story. Depending on topic, trace:

- Recognition and revocation across two independently operated authorities: who signs, how the consumer verifies, what is fetched/cached, and when a changed decision is observed.
- A gateway request through the exact supported SDK/API to the authoritative service: identity, transport/authentication, response validation and downstream enforcement.
- A policy request through decision, actual execution and its recorded evidence: what “allowed” means and what it does not prove.
- An edge action with a pre-issued grant: issuance policy, scope/budget/expiry, device checks, signed use records, reconnect admission/quarantine, and revocation freshness.
- A key rotation or release upgrade: which signatures/records remain valid, compatibility checks and recovery/rollback conditions.

These are investigation prompts, **not assertions that every flow or feature is currently shipped**. Publish only flows established by the ledger. Use the actual API names, flags and artifact fields from inspected sources; never invent a plausible sample command.

## 5. Fallback semantics must be exact

Words such as “fallback,” “offline,” “cached,” “fail closed,” “automatic,” and “retry” require a trace of the relevant branch and tests for that exact surface/version. Record:

1. Trigger: endpoint missing, explicit configuration, unsupported route, timeout, connection error, HTTP status, malformed response, signature failure, denied policy, stale evidence, or expired grant. Do not conflate them.
2. Eligibility: opt-in/default flags, prerequisites, valid cached material and supported operations.
3. Path: same authority or another destination; local verification or local decision; online refresh or offline material. Identify the trust boundary and whether any data leaves it.
4. Outcome: returned value/error, preserved or lost validation, retry budget, execution effects and observable audit record.
5. Refusal: conditions that must not fall back, especially explicit denials, revoked/expired artifacts and invalid signatures. Verify rather than assume these refusals exist.
6. Freshness: exact TTL, clock assumptions, budget/counter behavior, revocation propagation and reconnect semantics, citing configurable defaults as defaults, not universal constants.

Never describe a configured alternate path as transparent error recovery, or cached verification as fresh authorization. Never imply a disconnected device learns a revocation immediately. A gateway failure must not be described as permission to bypass policy. If implementations differ, explain the difference.

## 6. Citations and a reader's next step

Place a primary-source link close to every material factual claim. A bibliography alone does not show which source supports which statement. Quote sparingly and accurately. Links to code establish implementation; links to docs establish documented use; test links and run results establish only their stated scope.

Every substantive article and publication description must provide:

- **Check it yourself:** an exact, tested example or documented procedure, prerequisites, expected result and at least one relevant denial/failure case. Keep the pinned version in the internal ledger and linked reproducible instructions rather than routinely inserting it into evergreen prose; expose any version constraint necessary for the reader to reproduce the example. If not run, say “documented example, not executed in this review.” Do not label it tested.
- **Website**, **documentation**, **demo**, and **GitHub** links, verified at review time. Prefer the specific relevant docs/demo/source over four generic homepages. If no public demo exists or it is unavailable, state that and link a reproducible local example instead; do not fabricate a URL.
- A distinction between illustrative footage/diagrams and actual product output. A recorded demo is not evidence that the live service is currently available.

Verify public access without relying on a private signed-in session. Keep secrets, private logs, customer data and temporary upload links out of public evidence.

## 7. Approval and release gates

Maintain `review.md` with the draft revision or content hashes, evidence snapshot, reviewer, review date, blocking issues, approval reference, approved assets/channels and decision. It is a review record, not permission by itself. Do not fabricate approval or infer it from silence, a successful test, a prior article, or a campaign status field.

Required sequence:

1. Research and evidence inventory completed; unresolved claims qualified or removed.
2. Editorial review: substantive flow, honest limits, citations and actionable reader links.
3. Technical review: status/version distinctions, all relevant surfaces and precise failure/fallback behavior.
4. User approves the exact article before voiceover or paid media generation.
5. Derived copy/assets checked against the approved article and the [design system](design-system.md). New claims require new evidence and review.
6. Final public-access/link, media, metadata and privacy checks; user explicitly approves publication to the specified channels.

Until applicable gates pass, retain draft status and do not publish, push campaign drafts to the public repository, schedule posts or mark them release-ready. Approval to write does not approve release. Existing scripts and JSON status fields do **not** automatically enforce these gates; the operator must check the review packet before invoking a publishing action. Any automation added later must fail closed when evidence or approval is missing. Material changes or stale release evidence require re-review of affected claims and renewed approval of changed public content.

## Dated source examples: 2026-11-04 review

These are starting points found in the campaign audit, not a permanent capability matrix or a claim that this editorial review executed product tests. Recheck implementation, docs, tests, package registry and deployed behavior before reusing any claim. Source-head presence is not release availability.

- **Core/edge:** reviewed revision `8d0869b75f107bde4cae3b6a9e2be99dca47fcb7`. The [edge operating guide](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/docs/operations/edge-agent.md#L156-L195) documents distinct grant and break-glass triggers: grants can cover throttled, failing and unreachable authority cases; break-glass is available only when the authority is unreachable, no usable grant exists and a justification is supplied. DENY remains final, and an out-of-envelope action is refused even with justification. Do not flatten this into “offline fallback.” The [grant guide](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/docs/operations/grants.md#L316-L338) describes offline limits; inspect matching implementation/tests before claiming verified behavior.
- **Rust SDK:** reviewed revision `89e5091184680c935d3fd4acea391446dcc6cd9e`. Its [governance implementation](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/src/governance.rs#L408-L543) distinguishes network/timeout/429/5xx fallback eligibility from `admin_auth_throttled`, `evidence_store_unavailable` and unreadable responses. This does not establish identical edge or other-language behavior.
- **Gateway:** reviewed revision `adb20f1ed16dc7c6ca03b415636ccc6834775d01`. The [key/snapshot guide](https://github.com/GenesisMeshLabs/gateway/blob/adb20f1ed16dc7c6ca03b415636ccc6834775d01/docs/key-succession.md#L10-L55) describes pinned keys, periodic CRL refresh, retention of a verified snapshot on refresh failure and denial/readiness behavior once stale. The [sync implementation](https://github.com/GenesisMeshLabs/gateway/blob/adb20f1ed16dc7c6ca03b415636ccc6834775d01/src/gateway/sync.rs#L120-L145) is a separate implementation source. Do not describe retained snapshots as unlimited availability, or assume the gateway delegates all behavior to an SDK.
- **.NET SDK:** reviewed revision `0ba9c53afd38cf09700fcc38a810f42a1873fd3a`. [Governance code](https://github.com/GenesisMeshLabs/sdk-dotnet/blob/0ba9c53afd38cf09700fcc38a810f42a1873fd3a/src/GenesisMesh.Sdk/Governance.cs#L702-L816) and [GrantHolder code](https://github.com/GenesisMeshLabs/sdk-dotnet/blob/0ba9c53afd38cf09700fcc38a810f42a1873fd3a/src/GenesisMesh.Sdk/GrantHolder.cs#L724-L774) contain work beyond the core 1.8.1 documentation's capability description. The release/registry check in this audit still found published 1.8.1, not a published 1.9 package. The correct distinction is implemented on the inspected head versus verified published release, not “.NET has no offline support” or “1.9 is shipped.” Recheck the [official package index](https://api.nuget.org/v3-flatcontainer/genesismesh-sdk-dotnet/index.json) and [release list](https://github.com/GenesisMeshLabs/sdk-dotnet/releases).
- **TypeScript and Go:** inspected audit heads were `161ef82f6c99f8656c424eab87ab92404cdf1c55` and `9956c44deabb844293f413261454c12fe98d814d` respectively. Inventory their actual public functions and tests rather than borrowing Rust/.NET claims. The core [TypeScript governance guide](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/docs/sdk/typescript/governance.md) is a concrete distinction to check: an evidence outbox is not a general offline action scheduler. Do not rerun a side effect merely because submission of its evidence failed.

These examples deliberately expose documentation/head/release differences. Resolve those differences in each campaign's claim ledger; do not hide them behind a generic “SDK support” sentence.

### Inspected test examples (not executed in this review)

- [Rust break-glass tests](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/tests/record_outbox.rs#L964-L1026): unreachable/silent authority versus denial, invalid signature and refusal paths.
- [Rust grant fallback tests](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/tests/grant_holder.rs#L268-L305): spent time token and unreachable-authority fallback.
- [Edge scenario assertions](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/edge/tests/scenario.rs#L610-L636): out-of-grant refusal and no-grant authority refusal under throttling.
- [.NET break-glass tests](https://github.com/GenesisMeshLabs/sdk-dotnet/blob/0ba9c53afd38cf09700fcc38a810f42a1873fd3a/tests/GenesisMesh.Sdk.Tests/BreakGlassTests.cs#L291-L418): transient execution, denial/refusals and unreadable-body failures.

Use these to locate evidence, then record an actual run and its environment if claiming tested behavior. Test source alone is not a passing run or proof of release availability.
