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
