# A swarm needs boundaries, not just coordination

**Portable Trust · Part 4 of 6**

*A task assignment and permission to change a resource need separate checks.*

Consider an illustrative deployment: one agent diagnoses an incident. Another prepares a patch. A third is asked to deploy it. The coordination may be correct while the final request still exceeds the third agent's authority.

A useful deployment boundary can distinguish staging from production, one resource from another and preparation from execution. It also needs an answer when the authority is unavailable. Those decisions belong in the integration that can actually perform the change.

## Follow the deployment request

Genesis Mesh supplies signed trust and decision records rather than a swarm scheduler. The [project vision](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/VISION.md) keeps agent frameworks outside the core product. An orchestrator can remain responsible for assigning work while the receiving application checks authority at its own boundary.

The [governed-changes model](https://docs.genesismesh.org/concepts/governed-changes.html) distinguishes a prior decision, a change authorized under a pre-issued grant and a later judgment about an action. For the deployment example, that means identifying the requesting principal, the target resource, the requested capability and parameters, and the executor that will report the result. Saying “the agent was assigned this task” leaves those checks unspecified.

## Delegation still needs an execution boundary

The [delegation-chain walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) gives a more concrete way to narrow delegated authority: capability and validity subsets, with signatures checked at each hop. Verifying that chain does not grant permission for every interaction. The root agreement and the particular execution request still need their own verification.

The [process-level mediation example](https://docs.genesismesh.org/examples/process-level-mediation.html) exposes another integration limit. A guard is advisory if the agent can bypass it, retain the provider credentials or invoke an unrestricted subprocess. Making it mandatory requires removing those alternative paths. It is not kernel or hardware attestation. Its in-memory token budget resets on restart, and the guard makes no network calls, so a revoked token remains usable there until its expiry. Those limits matter when the proposed guarantee is containment rather than simply better records.

## Evidence follows the executor

In a supported governed integration, the controller obtains a decision, performs the permitted action and submits signed execution evidence. Broader client coverage is planned; the [integration guide](https://docs.genesismesh.org/sdk/index.html) identifies the available operations. The authority's decision and the executor's report answer different questions. A signed allow records permission; an executor's record describes what that executor reports doing. An independent observation can add evidence from the system where the change appeared.

The Network Authority, the operator's service that signs trust decisions and judges evidence, does not deploy the application by recording any of these artifacts. Nor does a signed record prove that an agent was uncompromised or that every side effect was reported. The [security model](https://docs.genesismesh.org/concepts/security-model.html) should be read alongside the integration: policy protects the route where it is enforced, not every tool the agent can reach.

## Test the handoff, not just the conversation

[AgentNet](https://arxiv.org/abs/2504.00587) studies decentralized coordination through agents and changing connections. It provides research context for distributing work. Its coordination results do not establish authorization at each participating organization's tool boundary, and no AgentNet integration is claimed here.

A useful integration test would send the same deployment agent a staging request and a production request. Show the rule and enforcement point that explain the difference. Then revoke authority after assignment but before execution, and inspect the information available at that final check. Test outage and exceptional execution separately.

## Check it yourself

From a prepared checkout with its documented dependencies installed:

```bash
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

The linked walkthrough requires a dual-signed root agreement, operator keys and recognition-graph exports for its manual flow. Widening capabilities fails with “exceed parent scope”; a wrong verification key fails with `invalid_delegator_signature` or `invalid_delegate_signature`. Verify the root agreement separately, then test a verified deny with a harmless callback before connecting a deployment tool.

This is a documented example and integration checklist, not executed in this review. Inspect the process-mediation example's credential and subprocess assumptions before calling its guard mandatory. A broad child delegation or a denied action should not be accepted merely because the task was assigned.

**Builds on our video** [Why Every Trust Decision Needs a Signed Record](https://www.youtube.com/watch?v=gp5yqnNQdZI)

**Go deeper:**

[Governed changes](https://docs.genesismesh.org/concepts/governed-changes.html)

**Next:** Revoked, but still running: the actions that happen too late

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
