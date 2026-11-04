# A valid payment can still be an unauthorized purchase

An assistant receives approval to buy a one-month service from a named provider. The payment succeeds. Later, the owner discovers that the assistant bought an annual plan from a reseller.

Nothing in that illustrative story requires the payment signature to be invalid. The failure is the missing connection between the owner's instruction and the economic effect.

[A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060) examines these cross-stage relationships in models of x402, MPP, ACP and AP2. Its results concern the modeled protocols, their assumptions and specified implementation checks. They are not proof that every deployment is vulnerable, or that another product automatically resolves the findings.

For a Genesis Mesh integration, the design question is concrete: can the controller show that the operation it executed is the operation its authority approved?

## Preserve the request, not just the verdict

A Network Authority, the service controlled by a sovereign operator, can evaluate a request against signed, active boundary policies. Its signed `BoundaryDecision` includes a `PolicyBinding`: policy versions and digests, gate outcomes and `context_digest`, the hash of the canonical request context. The [policy walkthrough](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) explains those artifacts.

The [context model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/context.py#L44) contains the requester, provider, requested capability and application-defined request parameters. The [policy-binding model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/boundary_policy.py#L225) identifies the digest field. Together, they provide material with which an integration can check a particular request, rather than treating an ALLOW as a reusable bearer instruction.

For a purchase adapter, a proposed context might identify the merchant, service, billing period, amount and currency. These are illustrative application fields. Genesis Mesh does not infer their commercial meaning or decide that two merchant identifiers represent the same legal counterparty.

The integration must normalize those values before evaluation and keep the exact request snapshot. It must validate their provenance as well: a signed decision based on a caller-supplied false price does not turn that price into a verified quote.

## Carry the binding into the executor

The documented `governedAction` helper verifies the authority's decision, expected policies and applicable attestation, checks the response's context identifier and checks expiry again after reading resource history. A verified denial prevents the callback. [Client implementation](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L360).

That is useful plumbing, but it is not a payment-specific intent checker. The callback is supplied by the application. It can still call the wrong merchant API, read a mutable shopping cart or submit an altered quantity unless the adapter is written to prevent those changes.

A careful adapter should compare its frozen purchase request with the intended execution arguments immediately before submission, and verify the relevant signed context binding. If any field changes, it should stop and obtain a new decision. It also needs provider-specific idempotency and reconciliation. Those are integration requirements, not behavior supplied by the generic helper.

An expiry check is a ceiling, not a promise that every condition stays true until then. The application must decide whether the operation needs a fresh decision closer to execution, particularly after queues, retries or changed commercial terms.

## Record the effect separately

After the action, an executor signs execution metadata. The [governed-action guide](https://docs.genesismesh.org/sdk/typescript/governance.html) distinguishes that result from authorization and explains the evidence outbox. If evidence delivery fails after a successful action, repair delivery of the evidence; do not blindly repeat the action.

For the purchase scenario, a provider transaction reference can help reconciliation, but the evidence signer is reporting what it observed. A signed report is not independent proof of fulfillment. The payment provider, merchant and resource inventory remain separate sources of truth.

The useful review exercise is therefore a chain of comparisons: owner's mandate to evaluated request, evaluated request to submitted operation, and submitted operation to observed result. A mismatch at any transition deserves an explicit outcome.

## Check it yourself

Use the [local policy demo](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) with a checkout and installed dependencies:

`python docs/examples/assets/scripts/boundary-policy-demo.py --no-gif`

It starts a temporary local authority with required policy enforcement. Inspect the allowed and denied requests and the signed policy binding. The [governed-action test source](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts) additionally includes a correctly signed response for another context and a decision that expires during the resource-head lookup. These are source-inspected examples, not tests executed in this review.

No purchase is made by this exercise. Before adding a payment adapter, make the changed-merchant and changed-amount cases explicit rejection tests.

Explore [Genesis Mesh](https://genesismesh.org/), the [documentation](https://docs.genesismesh.org/sdk/index.html), the [public trust demo](https://mesh.genesismesh.org/) and the [source repository](https://github.com/GenesisMeshLabs/genesismesh). The public demo is a trust-system interface, not a demonstration of the illustrative application in this article.
