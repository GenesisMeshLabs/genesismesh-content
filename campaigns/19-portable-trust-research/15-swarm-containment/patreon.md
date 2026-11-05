# Can a swarm limit a compromised member?

A coordinator delegates a dataset-reading task to a specialist. The specialist is compromised and starts asking for writes. Another agent is willing to help. In this illustrative scenario, the danger is not confined to one bad response: authority can spread through apparently routine handoffs unless each receiving system checks what the previous participant was actually allowed to pass on.

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) studies confinement under the assumption that the model itself may be compromised. Its broker results are not a Genesis Mesh security guarantee. The useful question for this article is narrower: what can a receiver verify about a chain of delegated capabilities, and what must still be enforced outside that chain?

## Give each handoff an inspectable record

Genesis Mesh treats the parties as independently operated trust domains. A signed `AgreementRecord` provides the root of the delegation chain. The [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) then creates a `DelegatedAgreementRecord` for each handoff, naming the parent, the delegator, the recipient and the delegated terms.

In the dataset example, the coordinator can pass on a reading capability already present in the parent terms. The specialist cannot turn that record into a valid delegation of a writing capability outside the parent's set. This is useful even when the specialist's language model is fully under an attacker's control: the receiving verifier evaluates signed artifacts rather than accepting the specialist's explanation of why it needs more authority.

The [builder and verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) bind each record to its parent terms by digest. The delegator signs, and the recipient adds its signature. The final verification requires valid signatures from the keys supplied for both participants. An attractive task description or a familiar participant name cannot substitute for those keys.

That key mapping is itself part of the receiver's trust configuration. The chain is not a mechanism for deciding which organizations deserve recognition. The verifier must be given the correct keys for the root parties and the relevant keys for each hop; accepting attacker-provided key mappings would change the question being answered.

## Verify the path, not just the last signature

The [chain verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) first verifies the root agreement's signatures. It then checks parent identifiers, the parent-terms digest, the capability subset, the expiry ceiling and the delegation signatures. These are concrete relationships among records. A signature alone would not establish that the signer held the authority it was handing onward.

Continuity matters after the first handoff. A root-agreement party may create the first delegation, but a later delegator must be the preceding recipient. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) cover unauthorized later-hop delegators as well as attempts to widen capabilities. That prevents a participant from inserting itself into a path merely because it can sign a new record.

For the compromised specialist, a fabricated writing hop should fail the capability-subset check. Extending the child record beyond the parent's expiry should fail the validity-ceiling check. These failures identify a broken delegation claim before the receiving service considers executing the requested dataset action.

However, an expiry ceiling is not a check that the whole relationship is valid now. The inspected verifier does not take a current-time parameter or fetch current revocation state. A cryptographically consistent chain can still need rejection by the service's current policy. The distinction is visible in the [verification function](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py).

## Put enforcement at the resource boundary

The dataset service still checks the current relationship, target resource and operation parameters before execution. Capability-set attenuation is not a general policy engine for arbitrary dataset constraints. If a reading capability is too broad for the task, preserving that broad capability through several valid signatures does not make the original scope safer.

The service must also use the verification result. Logging a failed delegation while performing the write would preserve evidence of the failure without containing it. The operator should make the acceptance decision part of the execution path and specify how a denial reaches the caller. This is an integration responsibility, not a property created merely by producing a chain file.

A separate [process-level guard](https://docs.genesismesh.org/examples/process-level-mediation.html) illustrates another boundary. Its execution path can constrain an agent only when the operator removes direct credentials and alternate routes to tools or subprocesses. Advisory instrumentation does not meet that condition. The guide explicitly separates advisory use from mandatory mediation.

The [guard implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py) also has limits: its in-memory invocation budget resets on restart, and it makes no revocation fetches. New token revocations remain unseen, while expiry and other local checks still apply. It is not kernel enforcement or hardware attestation. Delegation and guard CLI commands are [beta](https://docs.genesismesh.org/reference/public-contract.html).

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html), the root agreement, the parties' keys and the recognition-graph exports described by the walkthrough:

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

Inspect an accepted handoff and an attempt to delegate a capability outside the parent's set. Check the parent digest, both signatures and the keys used to verify them. Read the [delegation tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) for forged widening and unauthorized later-hop cases. Separately identify where your service checks present validity and resource parameters. The example and tests were not executed in this review.

## Further reading

- [Delegation-chain walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html)
- [Process-level mediation and bypass conditions](https://docs.genesismesh.org/examples/process-level-mediation.html)
- [Public surface stability](https://docs.genesismesh.org/reference/public-contract.html)

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/) | [Public demo](https://mesh.genesismesh.org/) | [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
