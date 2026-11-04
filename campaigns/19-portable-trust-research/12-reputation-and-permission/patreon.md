# Should an agent's reputation give it authority?

A highly rated service wins a task to prepare a procurement report. Does that also permit it to export private contracts or place orders?

This illustrative scenario separates selection from permission. An [ERC-8004 ecosystem study](https://arxiv.org/abs/2606.26028) reports reputation weaknesses in its observed dataset; it is not a verdict on every reputation system.

Genesis Mesh's Network Authority is an operator-run service for local trust and policy. In its [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html), a controller presents an authorization basis, requested capability and context for evaluation against operator-controlled rules.

Suppose the service holds an agreement limited to `reports.read`. A request for `contracts.export` needs separate authority. The [boundary engine](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/engine.py#L45-L118) checks capability, validity and freshness in the supplied context before returning a signed `BoundaryDecision`. Better reviews do not add capabilities to the agreement.

Configured policies can add gates using facts supplied by the integration. An enforce gate can deny; an observe gate records without blocking. That distinction lets an operator inspect a new signal without treating it as permission. A new evaluation type still needs trusted implementation and testing; no universal reputation connector is implied. [Policy implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/policy.py#L439-L511)

The controller must establish where a score came from and what it means. A signature cannot make a review honest. The executor must also bind the actual resource and operation to the evaluated request and protect alternative access paths.

An allowed decision records the authority's answer. It does not prove the provider's output is accurate or that the action completed.

## Check it yourself

From an installed source checkout, follow the [declarative-policy demo](https://docs.genesismesh.org/examples/declarative-boundary-policy.html), which creates a temporary authority and test records:

```text
python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif
```

Inspect the signed decision: the amount-cap request is denied, while the business-hours gate configured in observe mode records its outcome without becoming an enforcement rule. An unknown gate type is refused. This documented example was not executed in this review.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
