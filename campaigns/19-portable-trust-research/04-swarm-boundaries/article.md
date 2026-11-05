# A swarm needs boundaries, not just coordination

**Portable Trust · Part 4 of 6**

*A task assignment and permission to change a resource need separate checks.*

One agent diagnoses an incident. Another prepares a patch. A third receives the instruction to deploy it. The handoffs may be sensible while the final request still exceeds the deployment agent's authority.

In this illustrative scenario, the organization permits staging changes but requires a separate authority basis for production. The important boundary is the component holding the deployment credentials. A task assignment must not silently expand what that component will execute.

[AgentNet](https://arxiv.org/abs/2504.00587) studies decentralized coordination through agents and changing connections. Its results provide research context for distributing work; they do not establish authorization at each organization's tool boundary. No AgentNet integration is claimed here.

## Follow the authority through the handoff

Genesis Mesh provides signed trust, decision and evidence records. It does not choose which agent should diagnose the incident or prepare the patch. An orchestrator can keep those responsibilities while the receiving application checks authority for the proposed resource change.

The beta [delegation-chain workflow](https://docs.genesismesh.org/examples/delegation-chain.html) gives that application an inspectable path. A root `AgreementRecord` can lead to signed `DelegatedAgreementRecord` hops. Each hop identifies its parent and binds the parent's terms through a digest.

The [chain verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390) checks linkage, signatures, capability containment and expiry ceilings. A child may retain or narrow its parent's capabilities; it cannot add a capability the parent did not hold.

For the deployment scenario, a staging-only delegation cannot acquire production authority merely because the next agent receives a more ambitious task. The capability names and resource mapping are application choices, not a built-in deployment connector.

Chain verification has a separate limit: it does not establish that the root authority is currently acceptable for a new action. The root agreement and the actual execution request still need their own verification. A cryptographically intact history can outlive the operator's decision to accept it.

## Evaluate the action the executor will perform

The [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) lets an operator publish rules and obtain a signed `BoundaryDecision` for a request. The Network Authority is the operator-run service that evaluates those rules. The executor remains responsible for the external deployment.

The controller must bind the evaluated principal, resource, capability and relevant parameters to the actual operation. An approval for one staging service does not authorize changing a different production service. Facts supplied to policy evaluation must come from trusted integration inputs; signing the result does not make an agent's assertion true.

A denied action should stop before the deployment callback. If the authority is unavailable, the integration needs its explicitly configured outage behavior. Unavailability and a verified denial are different outcomes; neither a task assignment nor a successful delegation check supplies a blanket exception.

## Make mediation mandatory only when bypass is closed

The beta [GenesisGuard example](https://docs.genesismesh.org/examples/process-level-mediation.html) shows a local execution boundary. A signed `ExecutionMediationRequest` references a stored decision and carries an invocation token and command. The [guard](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/mediation.py#L126-L267) checks the authorization artifacts and command policy before mediated subprocess execution.

A guard is advisory if the agent can avoid it, retain provider credentials or invoke an unrestricted subprocess. Mandatory mediation requires verified restrictions on those alternative routes, including direct network access. Starting the guard does not provide a kernel sandbox or hardware attestation.

Its [token-use counter](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py#L53-L111) is process-local and resets on restart. The guard does not fetch newly recorded revocations; expiry and other local checks still apply. This is neither immediate withdrawal propagation nor durable global usage accounting.

These mechanisms describe parts an integration can use. They are not a ready-made swarm connector or proof that an existing deployment has closed every bypass.

## Keep permission and execution evidence distinct

In a supported governed integration, the controller obtains a decision, performs the permitted action and submits signed `ExecutionEvidence`. The [governed-changes model](https://docs.genesismesh.org/concepts/governed-changes.html) distinguishes permission issued beforehand from the executor's later report and from judgments about actions observed afterward.

The authority does not deploy an application by recording those artifacts. A signed allow records permission. An executor's record describes what that executor reports doing. An independent observation can supply another account from the system where the change appeared. Evidence-store collection requires the relevant features to be enabled; it is not automatically on.

Client choice matters. The current [capability matrix](https://docs.genesismesh.org/sdk/index.html) identifies TypeScript, Rust and .NET as governed clients; Go remains a verifier plus thin client. Their operations differ, so a shared product version does not establish feature parity.

The [security model](https://docs.genesismesh.org/concepts/security-model.html) should accompany the integration review. Signed records do not prove that an agent was uncompromised, every side effect was reported or unchecked tools were inaccessible.

## Check it yourself

From an installed source checkout, follow the [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html):

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

The demo supplies example keys, agreements and a controlled scenario clock. Expect a valid two-hop chain to verify and an attempt to widen capabilities to fail. The manual flow requires a dual-signed root agreement, operator keys and recognition-graph exports; verify the root separately.

This documented example was not executed in this review. For your deployment integration, separately test a verified denial with a harmless callback, a staging-versus-production handoff and authority withdrawal between assignment and execution. Inspect what the final checker actually knows before connecting production credentials.

## Further reading

- [Delegation chains](https://docs.genesismesh.org/examples/delegation-chain.html): inspecting the supplied authority path.
- [Declarative boundary policy](https://docs.genesismesh.org/examples/declarative-boundary-policy.html): evaluating a concrete request.
- [Process-level mediation](https://docs.genesismesh.org/examples/process-level-mediation.html): guard deployment and bypass limits.
- [Governed changes and evidence](https://docs.genesismesh.org/concepts/governed-changes.html): decisions, execution reports and observations.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
