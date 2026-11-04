# The agent can reason. Should it grant itself authority?

An operations agent reads an email demanding an urgent payment and instructing it to skip approval. In this illustrative scenario, the message may influence the proposal; it must not rewrite spending authority.

[NIST's design tenets](https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems) recommend separating agent reasoning from deterministic policy decisions.

Genesis Mesh's Network Authority is an operator-run service for local trust and policy. Its [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) lets the operator publish and activate a signed `BoundaryPolicy`. The example caps an amount with `max_value.v1` and requires an MFA fact with `boolean_required.v1`.

A controller sends an authenticated `POST /admin/boundary/evaluate` request with the authorization basis, capability and context. The authority returns a signed `BoundaryDecision` whose `PolicyBinding` identifies policy versions, gate outcomes and the context digest. A persuasive sentence cannot replace the configured rule. [Example source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/examples/assets/scripts/boundary-policy-demo.py#L50-L108)

The executor still owns the crucial boundary. It must use trusted facts and perform exactly the evaluated action. If the request says 500 but the executor transfers 5,000, the earlier decision does not authorize that payment. Likewise, `mfa_verified` must come from the authentication process, not the agent's assertion.

A failed enforce gate denies; an observe gate records without blocking. The example sets `BOUNDARY_POLICY_ENFORCEMENT=required` to refuse the legacy policy-free route. An ALLOW establishes neither execution nor the truth of caller-supplied facts. Credentials and alternative execution paths still need protection. [Policy implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/policy.py#L439-L511)

## Check it yourself

From an installed source checkout, follow the [boundary-policy demo](https://docs.genesismesh.org/examples/declarative-boundary-policy.html), which creates a temporary local authority and test records:

```text
python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif
```

Expect a signed policy and a denied 2,500 request under the 1,000 cap, even with the MFA fact set. The demo also refuses an unknown gate and the legacy route. This documented example was not executed in this review.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
