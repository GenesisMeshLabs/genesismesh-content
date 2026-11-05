# What if the agent is fully compromised?

A reporting agent has permission to run a limited local tool. After reading hostile input, it ignores every instruction and tries to execute a different command. Assume the model is no longer cooperating. What stops the action?

This is an illustrative threat model, not a report of an incident. [Delegation Without Trust](https://arxiv.org/abs/2609.00267) argues for evaluating agent systems under an untrusted-model assumption. Its experiments motivate the question; they do not certify a Genesis Mesh deployment or transfer their measured results to it.

The useful boundary is the component that can refuse execution even when the agent asks convincingly.

## Put a check before the subprocess

Genesis Mesh's beta [GenesisGuard workflow](https://docs.genesismesh.org/examples/process-level-mediation.html) places a local sidecar before mediated subprocess execution. The operator supplies trusted keys, authorization artifacts and command policy. The agent requests an operation through that boundary.

An `ExecutionMediationRequest` references a stored boundary decision and carries an invocation token, capability and command. The agent signs the request. The decision is identified by `decision_id`; it is not embedded as an entire decision object in the request. The [request model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/mediation.py#L24-L55) defines those fields.

The [guard's validation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L126-L267) checks the request signature, trusted operator decision, token issuer, bearer, capability, expiry and agreement match. It also checks the command against the configured allowlist. A missing token or an unauthorized command is refused before the mediated execution path proceeds.

For our reporting agent, the operator can permit the intended reporting invocation without allowing the agent to substitute an unrelated command merely because the same agent key signed both requests. Identity establishes who requested the operation; the decision, token and command policy constrain what that request may do.

The beta [invocation-token guide](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) explains the credential used in this flow. Possessing a valid token does not remove the other mediation checks.

## Treat the command policy as real authority

The allowlist needs careful review. Exact command rules and prefix rules have different effects. Prefix rules intentionally leave the trailing argument sequence unconstrained; the [matching implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L65-L123) shows this behavior.

That matters if an allowed executable can read arbitrary paths, launch other programs or interpret a script supplied as an argument. Allowing its name is not proof that every permitted argument combination is harmless. The operator must understand the program being exposed and choose a rule appropriate to the resource it can reach.

Successful mediation can produce a signed `MediatedExecutionReceipt`. That is evidence that the mediation step occurred under the recorded identifiers. It is not proof that the program's output was correct, that every consequence was desirable or that an allowed command contained no vulnerability.

The request, decision and receipt therefore serve different purposes. Keeping them distinct makes a later review more informative than a single “agent approved” message.

## Close the route around the guard

A compromised agent will not voluntarily use a boundary it can bypass. In advisory mode, it can avoid GenesisGuard and invoke a subprocess directly. The [deployment guidance](https://docs.genesismesh.org/examples/process-level-mediation.html) explicitly distinguishes this mode from mandatory mediation.

Mandatory mediation requires verified restrictions on direct subprocess, network and credential access. Starting the sidecar alone does not supply a kernel sandbox. The host environment and credential design must make the guarded route the effective route to the protected operation.

For the reporting scenario, inspect where the agent's process can write, which credentials it can read and which services it can contact. If it can reach the same resource through an unchecked API, a refusal at the guard has not contained that action. The [security model](https://docs.genesismesh.org/concepts/security-model.html) provides wider context for those trust boundaries.

## Account for restart and withdrawal

Two implementation limits are especially relevant under compromise. The token-use counter is process-local and resets on guard restart. The guard does not fetch revocations. These properties are visible in the [guard implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py#L53-L111) and should remain explicit in the deployment's security claim.

A withdrawal recorded elsewhere is therefore not immediately visible to this local guard. Token expiry and the other local checks still apply, but they are not a live revocation channel. Likewise, a process-local budget should not be presented as durable usage accounting across restarts or multiple guards.

Stolen keys can still be used within permissions the receiving boundary continues to accept. A pre-execution check also does not cancel work already underway. Incident procedures must address those cases in the surrounding system instead of assuming the presence of a signed artifact resolves them.

## Check it yourself

Use an installed source checkout and the [mediation walkthrough](https://docs.genesismesh.org/examples/process-level-mediation.html), with its agent, operator and issuer keys, stored decision, token and command allowlist:

```text
python docs/examples/assets/scripts/process-level-mediation-demo.py --no-gif
```

The script validates artifacts, constructs a receipt with an example process ID, and rejects an allowlist mismatch. It does not demonstrate an isolated live subprocess. The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_process_level_mediation.py#L730-L864) covers additional token refusals.

This documented example was not executed in this review. In a deployment, separately verify that the compromised agent cannot perform the same operation directly, and test the promised behavior across a guard restart.

## Further reading

- [Process-level mediation](https://docs.genesismesh.org/examples/process-level-mediation.html): guard setup and advisory versus mandatory deployment.
- [Invocation-bound tokens](https://docs.genesismesh.org/examples/invocation-bound-tokens.html): the scoped credential used by the guard.
- [Security model](https://docs.genesismesh.org/concepts/security-model.html): operator and execution boundaries.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
