# Should an agent's reputation give it authority?

A service has excellent reviews. Your procurement agent chooses it to prepare a comparison report. Does that also permit the service to read private supplier contracts or place an order?

In this illustrative scenario, reputation helps choose a candidate. Permission determines what that candidate may do with a particular resource. Treating the first as the second turns a useful signal into an unbounded grant.

An [empirical study of the ERC-8004 ecosystem](https://arxiv.org/abs/2606.26028) examines identity registrations and reputation records across three chains. Its authors report weaknesses in comparability, interaction grounding and manipulation resistance within their observed dataset. That is evidence about the ecosystem and period they studied, not a universal finding about every reputation system.

For Genesis Mesh, the useful question is simpler: how does the resource owner express an actual rule instead of relying on a general feeling of trust?

## Make the request specific

Genesis Mesh's Network Authority is an operator-run service for its own trust and policy decisions. In its [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html), a controller presents an authorization basis and a requested capability with relevant context. The authority evaluates signed, operator-controlled rules.

For our procurement example, imagine an agreement limited to `reports.read`. A request for `contracts.export` needs its own valid authority; popularity does not add that capability to the agreement. The [boundary engine](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/engine.py#L45-L118) checks capabilities, validity and freshness in the supplied context before returning a signed `BoundaryDecision`.

An operator can add configured gates using facts the integration supplies. A `BoundaryPolicy` might restrict a resource class or require an additional approval fact. Its signed decision can identify exactly which policy versions and gate outcomes applied. That is an inspectable local choice, rather than a global reputation score declaring who deserves access.

If reputation is an input to a policy, the operator must define what the signal means, who produced it and how it is refreshed. Genesis Mesh does not independently establish that a third-party review is honest merely because the review, its digest or an evaluation result has been signed.

## Keep a good score from erasing a hard limit

Suppose a provider's reviews improve between two requests. That may justify a human changing policy after review. It should not silently change the scope of an already signed agreement.

The [configured-policy implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/policy.py#L439-L511) distinguishes `enforce` from `observe`. An enforce gate can deny a request; an observe gate records a result without blocking it. That distinction is useful when introducing a new signal. Operators can observe its behavior before making it a prerequisite, while retaining existing capability and identity checks.

This is not a promise that reputation can be dropped into a universal scoring plugin. The documented gate registry has specific supported types. A new kind of evaluation requires an implementation the operator trusts, plus integration and testing. An unexplained score should not be smuggled into a Boolean field and treated as independently verified evidence.

## Permission still needs an executor

An approved read should cause only the approved read. The service handling the protected data must validate the decision and bind the actual resource and operation to the evaluated request. The organization also needs to control alternative credentials and APIs that could bypass that check.

A signed decision is useful evidence of the authority's answer. It does not prove the provider's output is accurate, that an approved action completed, or that no information leaked through another route.

Genesis Mesh is portable trust for sovereign systems. Its role here is to make authority and its basis inspectable while the resource owner keeps control of the decision.

## Check it yourself

Start with the [declarative-policy demo](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) in an installed source checkout:

```text
python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif
```

The local example creates a temporary authority and signed policies. Inspect the denied amount-cap request and the business-hours gate configured in observe mode: the latter records its outcome without becoming an enforcement rule. The example also refuses an unknown gate type. This is a documented example, not executed in this review.

For your own integration, list the signals used to select a service separately from the authority required to access a resource. A good reputation can support a decision. It should not make the decision disappear.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
