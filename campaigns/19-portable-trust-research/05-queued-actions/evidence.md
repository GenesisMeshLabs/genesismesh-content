# November 5 editorial revision: Revoked, but still running: the actions that happen too late

The user requested articles around 900 words, canonical documentation links throughout, and a final Further reading section. This reviewed revision was subsequently saved to the existing Patreon post and verified as recorded below. Source-based review only: no product tests, demonstrations or live actions were executed.

## Current verification and changed claims

Current source/release refresh confirms TypeScript head 8154ca7ac459ffbcd22d35900ca72f8093165bfc and v1.9.1 unchanged. The governed-action guide was reopened: it requires explicit verifier options, checks policy/attestation and context bindings, rechecks expiry after the resource-head lookup and separates callback execution from evidence delivery. Existing outbox/single-process/crash limits retain their source inspection basis; no callback or flush was run.

Replaced the ambiguous statement that broader client coverage is planned with a current per-client scope instruction. The current SDK matrix confirms .NET governed-client support from v1.9.0; older prose in the governed-changes page still omits it and is not used as availability evidence. Documentation links were expanded beside relevant claims and in a final Further reading section. No general queue fencing, provider cancellation, rollback or universal SDK parity is asserted. Patreon synchronization is verified below.

Canonical documentation pages opened and checked on 2026-11-05:

- [Governed actions](https://docs.genesismesh.org/sdk/typescript/governance.html)
- [Governed changes](https://docs.genesismesh.org/concepts/governed-changes.html)
- [Out-of-band changes](https://docs.genesismesh.org/operations/out-of-band-changes.html)
- [SDK matrix](https://docs.genesismesh.org/sdk/index.html)

## Exact revised article

The following text binds this claim review to the wording submitted for independent review. It retains the historical evidence inventory below.

# Revoked, but still running: the actions that happen too late

**Portable Trust · Part 5 of 6**

*The important revocation check is the one that can still stop the effect.*

Consider an illustrative queued job: it passes authorization and enters a queue. Minutes later, an operator revokes the credential. The worker wakes up and forwards the original request to an external provider.

The revocation record may be correct. Whether the job stops depends on where the worker checks authority, what it knows at that moment and whether the provider has already committed the action.

## Follow the request past the queue

Write the timeline as authorization, enqueue, dequeue, provider acceptance and external effect. A check before enqueue covers a different window from a check before the worker sends. Even the latter does not automatically cancel a request already accepted by a provider.

[Authorization Revocation for Long-Running AI Agents](https://arxiv.org/abs/2609.21284) develops a formal treatment of work associated with withdrawn authority, including enforcement at protected sinks. Its evaluation uses a bounded, provider-free trace suite. It is useful for specifying what must stop and where; it does not prove that arbitrary external providers support cancellation, or that Genesis Mesh implements the paper's protocol.

## What Genesis Mesh records

The [governed-changes documentation](https://docs.genesismesh.org/concepts/governed-changes.html) separates prior decisions, grant-authorized changes and after-the-fact judgments. This distinction lets an integration describe an action that was authorized before execution differently from one that occurred outside the governed path.

Once the appropriate evidence features are enabled, a controller can submit signed execution evidence associated with a decision. An observer can [report a change seen in an external system](https://docs.genesismesh.org/operations/out-of-band-changes.html). A judgment records the authority's evaluation of an observed or exceptional action. A later judgment is not permission that existed before the worker ran.

Evidence admission checks the report against the relevant trust and decision state. Refusal or quarantine can identify a record that should not be admitted as an ordinary governed action. If the worker already changed the provider's resource, however, the authority's treatment of the evidence is a later event. It does not reverse the provider's action.

## An evidence queue with a specific job

The [governed-action example](https://docs.genesismesh.org/sdk/typescript/governance.html) documents `governedAction(gm, recorder, request, callback)`. Verification binds the decision to the expected policies and, for an attestation-based allow, the expected attestation. An empty expected-policy list is an explicit empty binding. The helper checks the context ID and expiry, including a recheck after looking up the resource head. A verified deny does not call the action callback or submit execution evidence. Invalid, expired or mismatched decisions raise `DecisionVerificationError`.

After the callback runs, evidence delivery is another problem. The implementation's [governance helper](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts), [outbox](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/outbox.ts) and [evidence-store client](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/evidence_store.ts) support persisted pending evidence and later flushing. If uploading the report fails after the action, retry the evidence, not the action callback. Repeating the callback could repeat the external effect.

This outbox is an evidence-delivery queue, not a general job scheduler that reauthorizes arbitrary queued provider work. `FileOutbox` is documented for a single process per directory, without cross-process locking. A crash during the action can leave no outcome record; the controller must reconcile the external state instead of assuming the missing report proves nothing happened. 

## Where the controller still has work to do

The Network Authority, the operator's service that issues signed trust decisions, also judges records. It does not reach into a queue, cancel every provider request or perform a cloud remediation merely because a record says remediation is needed. The controller must implement those external actions, under whatever permissions and provider behavior actually apply.

This example uses one governed-client implementation; consult the integration matrix for each client's current operations and limits. The [integration guide](https://docs.genesismesh.org/sdk/index.html) describes which clients provide that workflow. The evidence-outbox behavior does not establish universal queue fencing, and an application must verify the operations its own integration exposes.

For a queued system, the integration needs to define whether authority is rechecked at dequeue, how retries bind to the intended action, what happens after a timeout with an uncertain provider outcome, and which cancellation operation can still reach an accepted job. Those are requirements to implement and test, not features inferred from the existence of signed evidence.

Prevention means the protected effect did not occur. Remediation is a later action to address an effect. Rollback requires restoring a previous state and may be impossible. A complete report should say which outcome is established and leave an uncertain outcome unresolved.

## A proposed failure test

Hold a simulated provider request after acceptance. Revoke authority, release it and inspect the result. Repeat with a retry and worker restart. Capture the last authorization check, the provider's acceptance, the observed effect and the authority's later evidence verdict separately.

## Check it yourself

Follow the linked governed-action example with its documented `ExecutionRecorder`, verifier options and expected bindings. The documented prerequisites are `EVIDENCE_STORE=on` (off by default), active policies, privileged setup and a registered executor key. Use a harmless callback and `FileOutbox` directory owned by one process. Retry pending evidence with `gm.evidenceStore.flushPending()`. Inspect the verified-deny branch first: the callback must not run. Then simulate failure of evidence submission after the callback succeeds, and use the documented flush operation to retry delivery without calling the action again.

This is the documented helper/outbox procedure with a proposed failure injection, not executed in this review. Retain separate counts for callbacks and evidence submissions. If the process crashes during the callback, reconcile the external outcome before deciding whether another action is safe.

## Further reading

- [Governed actions](https://docs.genesismesh.org/sdk/typescript/governance.html): decision verification, the callback and later evidence delivery.
- [Governed changes and evidence](https://docs.genesismesh.org/concepts/governed-changes.html): authorization, observations and judgments.
- [Changes outside the controlled path](https://docs.genesismesh.org/operations/out-of-band-changes.html): reporting and judging an observed external change.
- [Current integration matrix](https://docs.genesismesh.org/sdk/index.html): each client's supported scope.

Find more on the [website](https://genesismesh.org/), [documentation](https://docs.genesismesh.org/), [public trust console](https://mesh.genesismesh.org/) and [source repository](https://github.com/GenesisMeshLabs/genesismesh). The console does not demonstrate cancellation at your external provider.


## Prior source inventory (reviewed November 4)

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

## Patreon synchronization

Verified 2026-11-05: the approved revision was saved to the existing [Patreon post](https://www.patreon.com/GenesisMeshLabs/posts/revoked-but-that-174297277) and reopened. Its rendered body and all 16 links matched the approved source; the cover and public access were preserved. The existing public schedule remains 2026-11-05T16:00:00+01:00 (Europe/Stockholm). LinkedIn remains an unpublished draft.

Approved Markdown SHA-256: `719cdd797b0bf3a9583107b5e0880d9acba3cc787d3d61b0c407d14f46439b47`. Rendered-body SHA-256 after collapsing whitespace: `10c217411897106c15e0a27182173716d28219799842a447be93fd3e7064870b`. This is verification of the saved publication copy, not execution of a product example or proof that a scheduled post has been released.
