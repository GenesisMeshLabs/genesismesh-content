# The agent can reason. Should it grant itself authority?

An operations agent reads an email demanding an urgent payment. The message explains why approval should be skipped, supplies plausible details and insists that the transfer is already authorized. In this illustrative scenario, the agent may use the email to propose a payment. The email must not become the authority to spend.

[NIST's agent identity design tenets](https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems) recommend separating agent reasoning from deterministic policy decisions. That principle becomes useful only when the system has a concrete place where a proposed action can be refused.

## Put the rule outside the conversation

Genesis Mesh's Network Authority is an operator-run service for local trust and policy. Its [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) lets an operator publish and activate a signed `BoundaryPolicy`. The agent can request a decision; it does not acquire permission to rewrite the active policy by explaining its intentions.

The documented example uses `max_value.v1` to cap an amount and `boolean_required.v1` to require an MFA fact. These are explicit gates with configured inputs. A payment above the amount cap fails even when the request presents the required MFA value.

A controller sends an authenticated `POST /admin/boundary/evaluate` request containing the authorization basis, requested capability and context. The basis may be a membership attestation or agreement. The authority evaluates that request under the applicable policy and returns a signed `BoundaryDecision`. Its `PolicyBinding` identifies the policy versions, gate outcomes and context digest. The [example source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/boundary-policy-demo.py#L50-L108) shows this flow.

For the payment controller, that produces an inspectable answer to a bounded question: did this request satisfy these gates under this policy? It is more useful than asking the agent to promise that it followed instructions, because the answer is tied to explicit inputs and policy state.

## Enforce means something specific

A policy can contain gates in different modes. A failed enforce gate denies the request; an observe gate records an outcome without blocking it. The [policy implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/policy.py#L439-L511) makes that distinction explicit.

This is important during rollout. An operator may observe a new rule to understand its effects before making it blocking. But a dashboard showing a failed observed check is not evidence that the payment was refused. The operating procedure must match the configured mode.

The example also sets `BOUNDARY_POLICY_ENFORCEMENT=required`, which refuses the legacy policy-free route. Without checking that configuration, a team could demonstrate its new policy and still leave a route that does not require it. The [boundary-policy guide](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) includes the refusal as part of the example.

Unknown gate definitions are another useful failure case. The service should not reinterpret an unfamiliar rule as permission. The documented demonstration refuses an unknown gate type rather than treating its name as an implemented check. This is configuration validation, separate from an ordinary business-rule denial.

## The executor still owns the action

A signed decision does not establish the truth of caller-supplied facts. If the request includes `mfa_verified: true`, the controller must obtain that fact from the authentication process. Asking the model to set the field would move the trust problem into the request body.

The same applies to the payment amount. If the evaluated context says 500 but the executor transfers 5,000, the earlier decision does not authorize that payment. The controller must bind the decision to the same resource, operation and relevant values it executes.

Genesis Mesh's [governed-changes explanation](https://docs.genesismesh.org/concepts/governed-changes.html) helps distinguish a decision from evidence of a later action. An ALLOW is not a bank transfer receipt. It neither performs the external payment nor demonstrates that the recipient received funds.

Credentials matter for the same reason. If the agent can call the payment provider directly using a second credential, the policy service is not the effective spending boundary. Protecting that route is an integration responsibility; the [security model](https://docs.genesismesh.org/concepts/security-model.html) is relevant background for the operator-controlled trust boundary.

## Make the review concrete

For this scenario, an operator review should identify the source of the amount, the source of the MFA fact, the active cap and the component holding payment credentials. It should also show where a refusal stops the workflow before any transfer occurs.

That review focuses on authority, not the quality of the agent's explanation. The agent may be correct that the invoice is urgent. It may even have identified the right recipient. Neither observation changes the configured spending rule. A legitimate exception needs the operator's authorized process, not a more persuasive prompt.

## Check it yourself

Use an installed source checkout and the [boundary-policy demo](https://docs.genesismesh.org/examples/declarative-boundary-policy.html). It creates a temporary local authority and test authorization records:

```text
python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif
```

Expect a signed policy and a denied 2,500 request under the 1,000 cap, even with the MFA fact set. The example also refuses an unknown gate and the legacy route when policy enforcement is required.

This documented example was not executed in this review. In your integration, separately verify that a denied decision prevents the external call and that changing the amount after evaluation cannot reuse the earlier authorization.

## Further reading

- [Declarative boundary policy](https://docs.genesismesh.org/examples/declarative-boundary-policy.html): policy publication, evaluation and refusal examples.
- [Governed changes and evidence](https://docs.genesismesh.org/concepts/governed-changes.html): decisions and action records.
- [Security model](https://docs.genesismesh.org/concepts/security-model.html): trust boundaries and operator responsibilities.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
