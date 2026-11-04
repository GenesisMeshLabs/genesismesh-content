# A valid payment can still be an unauthorized purchase

An illustrative assistant is allowed to buy a monthly service, but submits an annual subscription to another merchant. The payment signature may be valid; the purchase still differs from the owner's instruction.

[A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) studies such cross-stage relationships in protocol models, not every deployment.

## Carry the approved request into execution

In Genesis Mesh, a Network Authority, the service controlled by a sovereign operator, evaluates requests against active policies. Its signed `BoundaryDecision` can contain a `PolicyBinding` identifying policy versions, gate outcomes and `context_digest`, the hash of the canonical request context. [Policy-binding model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/boundary_policy.py#L225).

A proposed purchase adapter would preserve a validated request containing merchant, service, period, amount and currency. Those are application-defined fields, not an existing Genesis Mesh payment API. A signed decision does not validate a false quote's provenance.

The [documented `governedAction` implementation](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L360) verifies the authority's decision, expected policies and applicable attestation, checks the context identifier and rechecks expiry after reading resource history. A verified denial prevents the callback.

The callback remains application code. The helper does not automatically compare every purchase field or recompute `context_digest`. The adapter must verify the relevant signed context binding and compare the preserved request with the actual execution arguments. A changed merchant, price or subscription period should stop execution and require a new decision.

After execution, signed metadata records the executor's reported outcome. Evidence delivery and the payment operation remain separate: repairing a failed evidence upload must not buy the service again. Provider idempotency, reconciliation and fulfillment checks remain integration responsibilities. This is an illustrative authorization design, not a payment product.

## Check it yourself

With a local checkout and installed dependencies, follow the [policy walkthrough](https://docs.genesismesh.org/examples/declarative-boundary-policy.html):

`python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif`

Expect allowed and denied requests and inspect their signed policy bindings. The [client tests](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts) also cover a wrong context and expiry during resource-history lookup. This documented example and inspected test source were not executed in this review.

Before adding a payment adapter, make changed-merchant and changed-amount cases explicit rejection tests.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
