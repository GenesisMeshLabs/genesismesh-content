# What if the agent is fully compromised?

Imagine a reporting agent that ignores every instruction and tries to run an unauthorized command. What stops it besides its own willingness to cooperate?

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) argues for this untrusted-model assumption; its experiments do not certify a Genesis Mesh deployment.

Genesis Mesh's beta [GenesisGuard workflow](https://docs.genesismesh.org/examples/process-level-mediation.html) places a local sidecar before mediated subprocess execution. The agent sends a signed `ExecutionMediationRequest` referencing a stored boundary decision and carrying an invocation token, capability and command.

The [guard](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L126-L267) checks the request signature, trusted operator decision, token issuer, bearer, capability, expiry and agreement match. It also checks the full command against an allowlist; prefix rules intentionally leave their argument tail unconstrained. A missing token or unauthorized command is refused. Successful mediation can produce a signed `MediatedExecutionReceipt`, not proof that the program was harmless.

The operator must close bypass paths. In advisory mode, the agent can simply avoid the guard. Mandatory mediation requires verified restrictions on direct subprocess, network and credential access; starting GenesisGuard alone supplies no kernel sandbox.

Two further limits matter under compromise: the [token counter](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py#L53-L111) is process-local and resets on restart, and the guard does not fetch revocations. A withdrawal elsewhere is not immediately visible; local expiry and other checks still apply. Stolen keys remain usable within surviving permissions, and a pre-execution decision does not cancel work already underway.

## Check it yourself

Use an installed checkout and the [mediation walkthrough](https://docs.genesismesh.org/examples/process-level-mediation.html), with its agent/operator/issuer keys, decision, token and command allowlist:

```text
python docs/examples/assets/scripts/process-level-mediation-demo.py --no-gif
```

The script validates artifacts, constructs a receipt with an example process ID, and rejects an allowlist mismatch. It does not demonstrate an isolated live subprocess. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py#L730-L864) cover additional token refusals. This documented example was not executed in this review.

Separately verify that the compromised agent cannot perform the same action directly.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
