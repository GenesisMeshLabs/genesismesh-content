# What if the agent is fully compromised?

Assume an agent ignores every instruction. It tries to run a shell command, reuse another agent's permission and call a service directly with credentials it found.

This illustrative threat model is more useful than asking whether the agent usually behaves. The question is what it can still reach when its reasoning cannot be trusted.

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) argues for evaluating agent systems under an untrusted-model assumption. Its experiments concern the authors' design and test setup. They do not establish the security of a Genesis Mesh deployment. They do suggest a practical question for one: where is the enforcement component, and can the compromised process go around it?

## Examine a real execution gate

Genesis Mesh documents a beta local sidecar called GenesisGuard in its [process-level mediation example](https://docs.genesismesh.org/examples/process-level-mediation.html). The agent submits a signed `ExecutionMediationRequest` referencing a stored boundary decision and carrying an invocation token, requested capability and subprocess command.

The guard's [validation function](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L126-L267) verifies the agent request, a decision signed by a configured operator, and a token from a configured issuer. It checks that the decision allows execution and is unexpired, that the token belongs to the requesting agent and grants the capability, and that token and decision refer to the same agreement.

It also checks the command against an allowlist. Matching is over the command arguments, not just the executable name. Allowing one Python script must not silently authorize arbitrary `python -c` code. Prefix rules deliberately leave a tail unconstrained, so choosing them is an operator security decision. [Allowlist logic](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L65-L123)

The guard can produce a signed `MediatedExecutionReceipt` for an execution it mediated. That record is evidence of the guard's participation and reported result, not a guarantee that the program's behavior was harmless.

## The bypass path decides the outcome

Now return to the compromised agent. If it can spawn a process directly, it can ignore GenesisGuard. If it holds a cloud credential, it may call the cloud API without asking the guard at all.

The documentation explicitly distinguishes advisory mode from mandatory mediation. Advisory mode observes executions sent through the guard; it does not block unmediated ones. Mandatory mediation requires the deployment to remove direct execution and credential paths and to verify that bypass attempts are blocked. GenesisGuard does not supply a kernel sandbox or hardware isolation by itself. [Deployment requirements](https://docs.genesismesh.org/examples/process-level-mediation.html)

Consider a permitted report-generation command. An operator could keep its credentials in a guarded broker, restrict the agent's process and network access, and expose only the report operation. That is an integration design, not something achieved by starting a sidecar alone. The broker, its credentials, command policy and host restrictions become part of the trusted system.

The guard also has operational limits: its token-use counter is held in memory for one process and resets on restart. It does not fetch revocations, so a withdrawal elsewhere is not immediately visible; local expiry and other checks still apply. A durable shared budget or fresh revocation check needs additional design. [Guard implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py#L53-L111)

A stolen agent key remains a serious problem: it can authenticate requests as that agent within whatever permissions still apply. The guard does not make key theft harmless. Nor does a successful pre-execution check cancel a side effect already underway.

## Test refusal, then test escape

The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py#L730-L864) includes missing tokens, another bearer's token, unknown issuers, mismatched agreements and invocation-budget exhaustion. These are useful checks of the mediated path. They are not proof that a production host has no alternative path.

A deployment review needs both: refusal tests for the gate and escape tests for the environment around it.

## Check it yourself

Use the [process-level mediation walkthrough](https://docs.genesismesh.org/examples/process-level-mediation.html) with the example agent, operator and token-issuer keys, valid decision/token artifacts and an explicit command allowlist:

```text
python docs/examples/assets/scripts/process-level-mediation-demo.py --no-gif
```

The script demonstrates artifact validation and constructs a receipt with an example process ID; it does not demonstrate an isolated live subprocess. Its allowlist mismatch shows a rejection. The walkthrough and tests cover additional missing-token cases. This is a documented example, not executed in this review.

Before calling a deployment enforced, separately prove that the same agent cannot perform the action directly. The strongest policy in the intended path does not constrain a path the policy never sees.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
