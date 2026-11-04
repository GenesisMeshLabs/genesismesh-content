# Make agent-to-agent interactions accountable

A purchasing agent asks a supplier's service to retrieve an invoice. The supplier permits the request, performs a lookup and reports success. Later, an auditor needs to distinguish three statements: who requested access, who allowed it and what the service says it did.

That illustrative exchange becomes difficult to investigate when everything is compressed into one "success" log line. Each party controls a different part of the story.

[BlockA2A](https://arxiv.org/abs/2508.01332) explores identity, authorization and accountability across agent interactions using its own architecture and prototype. Its experiments are research context here, not evidence that Genesis Mesh implements its architecture or reproduces its results.

## Preserve the boundary between permission and execution

In a Genesis Mesh governed integration, the Network Authority is the operator's service that evaluates requests and signs decisions. The receiving application owns execution. A signed `BoundaryDecision` records the decision; an executor signs `ExecutionEvidence` describing its reported outcome. Those authors have different responsibilities. The [governed-changes guide](https://docs.genesismesh.org/concepts/governed-changes.html) describes that separation and the settings needed to retain evidence.

For the invoice example, record the requested capability, the resource, the actual parameters and the executor identity. The [execution record implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) carries a decision reference, capability, parameters, outcome, timestamp and sequence number. It signs that record with the executor's key. Signing a report does not run the provider's API or establish that the report is truthful.

A denial must stop the application's controlled execution path. An allowed request can still fail at the provider. The resulting execution report should say failure or partial completion when that is what happened. Retrying delivery of a report must not be confused with repeating the original action.

## A chain answers a narrower question

The [execution-evidence example](https://docs.genesismesh.org/examples/execution-evidence-chain.html) connects each record to the preceding record's digest. Its verifier checks sequence continuity, links and signatures against the executor keys supplied by the verifier. It can also check an expected capability.

This gives an auditor useful failure signals. Removing a middle record leaves a sequence gap. Altering signed data breaks verification. Using an unexpected capability can be refused when the caller supplies that expectation. The [source tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py) exercise these classes of failure.

But a shorter valid prefix can still verify. If the real chain contains records one, two and three, presenting only one and two does not tell this verifier that three ever existed. It has no independently supplied expected final length. Compare it with a provider counter or another separately retained observation.

There is another boundary: an executor signature establishes the signer of a claim. It does not prove that the invoice was correct, that no other query happened or that the agent was uncompromised. Independent provider observations can help investigate those questions; they should remain identifiable as separate evidence.

This walkthrough uses the beta execution CLI; the [public contract](https://docs.genesismesh.org/reference/public-contract.html) defines the compatibility boundary.

## Check it yourself

The [walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html) uses an existing agreement, a signed boundary decision, an executor key and the verifier's known public keys. Follow the [development installation](https://docs.genesismesh.org/installation.html), then run its local demonstration:

```text
python docs/examples/assets/scripts/execution-evidence-chain-demo.py --no-gif
```

Inspect the three records and their links. The documented ordered chain verifies; supplying records one, three, two produces `sequence_gap`. Also try the valid prefix one, two and compare it with an independently retained expected count. The example is documented, not executed in this review.

The public console below is an available demonstration interface; it is not proof that this workflow ran against your systems.

For your next integration, keep the decision, the executor's report and the external observation distinct. That gives each claim an author and makes disagreements visible instead of hiding them behind a single green check.

[Website](https://genesismesh.org/)  |  [Documentation and local demo](https://docs.genesismesh.org/examples/execution-evidence-chain.html)  |  [Public console](https://mesh.genesismesh.org/)  |  [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)
