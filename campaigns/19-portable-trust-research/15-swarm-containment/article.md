# Can a swarm limit a compromised member?

A coordinator gives an analysis agent access to a dataset. The agent delegates a smaller reading task to a specialist. Then the specialist is compromised and asks to modify the dataset.

This illustrative swarm has two problems to solve. The handoff must not create extra authority, and the dataset service must enforce the limit even when the specialist stops cooperating.

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) evaluates multi-agent systems under an untrusted-model assumption: confinement should survive a compromised model. Its broker and experimental results belong to that research. They are not a containment certification for Genesis Mesh or for an application using it.

## Make every handoff inspectable

The Genesis Mesh [delegation-chain example](https://docs.genesismesh.org/examples/delegation-chain.html) starts from a signed `AgreementRecord`. Each `DelegatedAgreementRecord` names its parent, the party delegating, the recipient, the delegated terms and a digest of the parent's terms. Both parties sign the handoff.

For the dataset story, the coordinator could pass a reading capability onward while withholding modification. The exact resource restrictions still need a policy and enforcement design for that dataset; a generic capability name does not bind every parameter automatically.

The [chain verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) checks the root agreement, parent linkage, parent-terms digest, capability subset, expiry ceiling and signatures. For later hops, the delegator must be the previous hop's recipient. A party cannot merely point at another delegation and claim its rights. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) include scope escalation, unauthorized handoff, changed parent terms and wrong signing keys.

That is a concrete boundary for the signed chain. It does not turn the specialist into a safe program. Nor does chain verification alone authorize a particular tool call. The receiving system still needs to check the current relationship and requested operation.

## Put enforcement where the action happens

Genesis Mesh also documents a [process-level mediation example](https://docs.genesismesh.org/examples/process-level-mediation.html). A deterministic guard checks a signed request, a stored decision, an invocation token and an explicit command allowlist before starting a process. The Network Authority is the operator's service that signs trust decisions; the guard and the application remain responsible for the execution path they control.

The distinction between advisory and mandatory mediation matters more than the presence of a guard process. If the compromised specialist holds the provider credential or can invoke an unrestricted alternative process, it can walk around the checked path. The operator must remove those routes before treating mediation as a boundary.

The [guard implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py) also records practical limits: it is not kernel or hardware attestation; the invocation budget is in memory and resets on restart; the guard makes no network calls and does not learn a newly revoked token before its expiry. A local limit must not be advertised as instant swarm-wide containment.

The delegation and guard CLI commands are beta surfaces in the [public contract](https://docs.genesismesh.org/reference/public-contract.html); this example does not promise a stable swarm integration API.

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html) and the [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html). Its prerequisites are the root agreement, the parties' keys and their recognition-graph exports.

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

Verify a valid handoff, then follow the documented failure case that requests a capability outside the parent's set. Creation should refuse the widening; a forged widening in a chain is rejected by verification. Check the unauthorized second-hop tests as well. This is a documented example and source review, not an executed test in this review.

For a deployment, add a separate exercise: have the specialist attempt the forbidden operation through every route it can reach. Passing the signed-chain check alone does not answer that question.

A useful swarm handoff states both what the next member receives and where that limit will be enforced. The smaller delegation is only as effective as the boundary that consumes it.

[Website](https://genesismesh.org/)  |  [Documentation and local demo](https://docs.genesismesh.org/examples/delegation-chain.html)  |  [Public console](https://mesh.genesismesh.org/)  |  [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)
