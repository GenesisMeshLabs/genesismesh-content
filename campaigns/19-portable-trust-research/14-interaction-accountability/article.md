# Make agent-to-agent interactions accountable

An invoice assistant asks another organization's service to retrieve three account records. The request is approved, but the last lookup returns only a partial result. Later, someone reviewing the workflow sees a chat message saying "done." In this illustrative case, that message is too weak to answer who authorized the work, which service performed it and what the service reported.

The [BlockA2A research](https://arxiv.org/abs/2508.01332) studies verifiable agent interactions and accountability. Its architecture and evaluation are not Genesis Mesh guarantees. The relevant Genesis Mesh mechanism is a signed execution record linked to a decision, with successive records connected so a verifier can inspect their order and integrity.

## Separate permission from the report of execution

Genesis Mesh is a portable trust layer for independently operated systems. Its Network Authority is the operator's service for trust decisions and signed control material. A resource-owning service remains responsible for applying an allowed decision and performing the requested action. The [governed changes guide](https://docs.genesismesh.org/concepts/governed-changes.html) makes a useful distinction: the authority signs a decision, while an executor signs the record of what it did.

For the invoice workflow, a signed `BoundaryDecision` records the authorization outcome. That does not mean the account lookup happened. The service may fail before execution, return incomplete data or encounter a downstream error. An audit needs the decision and the later execution report, because they answer different questions.

The [execution-chain walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html) starts with an agreement and an allowed decision, then records three executions under that decision. The service signs each `ExecutionEvidence` record. The example deliberately gives the third record a partial outcome, making the difference between permission and completion visible.

The [record model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/execution.py) carries decision, context and agreement identifiers; the executor's sovereign identity; executed capability and parameters; execution time; outcome; sequence number; and the previous evidence digest. These fields let a reviewer inspect a concrete report rather than infer execution from the assistant's description of its intentions.

## Follow the links between records

Each later record includes `prev_evidence_digest`, the digest of the preceding record's canonical body. The executor signs that link as part of the new record. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) therefore gives the verifier something stronger than three independent messages: an ordered sequence whose links can be checked.

The verifier receives the evidence chain and a mapping from executor identities to trusted public keys. Those keys are an input chosen by the verifying party; a record does not make its own signer trustworthy merely by naming an identity. If the caller supplies an expected capability, the verifier checks that each record names it.

The [verification routine](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) checks sequences starting at one, digest links and executor signatures. It rejects missing signatures, invalid keys, capability mismatches when that check is requested, and broken links. When a decision with an embedded freshness proof is supplied, it also rejects a reported execution time beyond that proof's validity window. That last check is conditional; callers should not assume it ran without supplying the relevant decision.

In the invoice example, changing the order from records one-two-three to one-three-two produces a gap at the second supplied record. The [walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html) shows the refusal as `sequence_gap`. A reviewer can identify the failed position instead of accepting an undifferentiated "audit complete" result.

## An intact chain is not a complete history

The important limit is at the end. The inspected [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) has no required final record count or independently expected head digest. A valid prefix can therefore verify even if a later record was omitted. Removing a middle record is different from withholding the tail.

For the invoice reviewer, seeing two valid records cannot prove there were only two executions. The application needs an independent expectation of completion, such as an externally retained final count or checkpoint, and must compare the supplied evidence with that expectation. That is an integration requirement, not a completeness guarantee furnished by this chain verifier.

There is another boundary at the signer. A valid signature attributes a statement to the corresponding key; it does not prove that an outcome string is truthful or that the returned account data is correct. If the executing service lies, the signed record can preserve its claim for investigation, but the claim still needs corroboration. The records also contain parameters and identifiers, so operators should decide what belongs in an exported audit packet.

For an operator review, keep the original decision, the ordered records and the independently selected verifier keys together. Ask the service owner to explain a partial outcome instead of normalizing it into success. Also document how the reviewer knows the workflow is finished. Those questions make the evidence useful without pretending that cryptographic integrity answers every operational question.

The execution commands are [beta](https://docs.genesismesh.org/reference/public-contract.html). This article describes the inspected reference flow, not automatic instrumentation of every agent framework or a promise that all clients produce equivalent evidence.

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html). Follow the walkthrough's agreement, decision and executor-key setup, with the corresponding public key available to the verifier:

```text
python docs/examples/assets/scripts/execution-evidence-chain-demo.py --no-gif
```

The documented result is a valid ordered chain, followed by a refusal when records are reordered. Inspect the partial outcome and each signed link. Then examine how the [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py) cover sequence and signature failures, and separately consider the valid-prefix limitation. Neither the example nor these tests were executed in this review.

## Further reading

- [Execution evidence chain walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html)
- [Decisions, execution and governed changes](https://docs.genesismesh.org/concepts/governed-changes.html)
- [Public surface stability](https://docs.genesismesh.org/reference/public-contract.html)

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/) | [Public demo](https://mesh.genesismesh.org/) | [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
