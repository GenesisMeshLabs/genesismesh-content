# The agent can reason. Should it grant itself authority?

An operations agent reads a supplier email that says a payment is urgent. It proposes a transfer above the company's normal limit. The email also insists that approval checks can be skipped.

This illustrative scenario has two different decisions: what the agent suggests, and what the organization permits. Giving the same reasoning process control over both lets the message it is reading influence its own authority.

[NIST's agent identity design tenets](https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems) call for architectural separation between reasoning and policy, supported by deterministic access decisions. That is design guidance, not certification of a particular product. Genesis Mesh provides a concrete way to examine the boundary.

## Put the rule under the operator's control

In Genesis Mesh, a Network Authority is the service an operator runs to issue and check trust records and make policy decisions for its domain. The [declarative boundary-policy walkthrough](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) shows an operator publishing and activating a signed `BoundaryPolicy`.

The policy selects relevant requests and configures registered gates. Its example caps an amount with `max_value.v1` and requires an MFA fact with `boolean_required.v1`. The agent does not edit those gates by adding a persuasive paragraph to its request.

A controller submits an authenticated `POST /admin/boundary/evaluate` request identifying the authorization basis, capability and context. In the example, a membership attestation carries the capability, while the request supplies an amount and an MFA flag. The Network Authority returns a signed `BoundaryDecision` containing a `PolicyBinding`: the policy versions, their digests, gate outcomes and context digest. [Runnable example source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/boundary-policy-demo.py#L50-L108)

The decision is useful because the consumer can examine the evaluated request and the rules behind it. It is not an instruction to trust arbitrary input facts.

## Bind the decision to the action

Suppose the request says "transfer 500" but the executor sends 5,000. A correct policy decision about the first request does not authorize the second. The consuming controller must bind its execution parameters to the evaluated context and retain control of the credentials that perform the transfer.

The same applies to `mfa_verified`. A field with that name does not prove MFA happened. A trusted integration must obtain the fact from the relevant authentication flow. Allowing the model to declare that it passed MFA would move the policy boundary back inside the model.

The [policy evaluator](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/policy.py#L439-L511) distinguishes enforcement from observation. A failed enforce gate denies; an observe gate records a result without denying. Missing inputs, unavailable gate implementations and gate errors cannot be casually interpreted as permission. Malformed or unauthenticated HTTP requests are separate error paths.

For deployments that require policy-bound decisions, the example uses `BOUNDARY_POLICY_ENFORCEMENT=required` and shows the legacy policy-free route being refused. Configuration is part of the boundary. A strong policy installed beside an unrestricted execution path does not constrain that path. [Policy service and tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_boundary_policy.py)

## What the result establishes

An allowed decision says the evaluated request passed the applied rules. It does not prove the external action ran, that the supplied facts were true, or that every way into the target system is governed. Execution and evidence submission remain separate responsibilities.

That separation is valuable. A model can propose a useful action without gaining the power to rewrite the rule that judges it. An operator can change policy without asking the model to remember a new instruction.

## Check it yourself

Use the [boundary-policy walkthrough](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) from an installed checkout. Its demo starts a temporary local Network Authority and creates its own test records:

```text
python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif
```

Inspect the signed policy and decision. The documented 2,500 request is denied by the 1,000 cap even with the MFA fact set. The example also exercises an unknown gate and refusal of the legacy route. This is a documented example, not executed in this review.

Then ask a deployment-specific question: which component can actually spend, write or delete, and can the agent reach it without this decision?


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
