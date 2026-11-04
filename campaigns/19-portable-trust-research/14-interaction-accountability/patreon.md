# Make agent-to-agent interactions accountable

A purchasing agent requests an invoice. The supplier allows the request, performs a lookup and reports success. In this illustrative exchange, an auditor needs to separate permission from the executor's account of what happened.

[BlockA2A](https://arxiv.org/abs/2508.01332) studies accountability across agents; its architecture and experimental results are not Genesis Mesh guarantees.

## Give each claim an author

Genesis Mesh's Network Authority is the operator's service that evaluates requests and signs decisions. The receiving application performs the action. A `BoundaryDecision` records permission; executor-signed `ExecutionEvidence` records the reported outcome. The [governed-changes guide](https://docs.genesismesh.org/concepts/governed-changes.html) describes that boundary.

The [execution record implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) carries the decision reference, capability, parameters, outcome, time and sequence. Each record can link to the previous record's digest. Verification checks sequence continuity, links and signatures against the supplied executor keys; an expected capability can also be checked.

Removing a middle record leaves a gap. But removing the ending is different: records one and two can verify even when record three was withheld. This verifier has no independently supplied final count. Compare the chain with a separately retained provider count or observation.

A valid executor signature also does not prove the invoice was correct or that every query was reported. Permission, execution and the truth of the report remain distinct. The example's execution CLI is [beta](https://docs.genesismesh.org/reference/public-contract.html).

## Check it yourself

Use the [development installation](https://docs.genesismesh.org/installation.html) and the [walkthrough's](https://docs.genesismesh.org/examples/execution-evidence-chain.html) agreement, signed decision, executor key and known verifier keys:

```text
python docs/examples/assets/scripts/execution-evidence-chain-demo.py --no-gif
```

The ordered chain should verify; supplying records one, three, two produces `sequence_gap`. A valid prefix still verifies, so compare it with the expected count. The [source tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py) cover sequence and signature failures. This example was not executed in this review.

[Website](https://genesismesh.org/) | [Documentation/local demo](https://docs.genesismesh.org/examples/execution-evidence-chain.html) | [Public console](https://mesh.genesismesh.org/) | [Source](https://github.com/GenesisMeshLabs/genesismesh)
