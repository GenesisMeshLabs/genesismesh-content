# Your car can pay. Who gave it permission?

An electric vehicle reaches a charger. Its owner approved charging, but did that include any price, merchant or bundled subscription? This illustrative scenario separates possession of a payment credential from permission to buy.

[Research on machine-to-machine payments](https://portalcientifico.upm.es/en/ipublic/item/9930578) proposes a preliminary consumer-IoT/CBDC model; Genesis Mesh supplies authorization building blocks, not an EV or payment product.

## Make the owner's mandate enforceable

A proposed controller would validate the vehicle, merchant, service, amount, currency and time window, then submit those application-defined facts for evaluation. It must establish their provenance rather than trust an unverified quote.

A Genesis Mesh Network Authority, the operator-controlled service issuing and evaluating trust records, evaluates requests under active policies. Its [policy gates](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/registry.py#L453) support required parameters, numeric maxima, allowlists and attestation claims. A per-request maximum does not enforce a shared balance or daily budget; aggregate spending needs durable state and concurrency controls.

In the [documented governed-action flow](https://docs.genesismesh.org/sdk/typescript/governance.html), `governedAction` verifies the authority's decision using trusted keys, expected policies and the applicable attestation. On the ordinary online path, a verified denial prevents the application's callback. An allowed callback executes separately from subsequent signed execution evidence.

For this design, that callback would be a payment adapter. It must match the actual merchant, amount, currency and service to the approved purchase, and reject a changed quote. Provider authentication, idempotency and reconciliation remain its responsibility; Genesis Mesh does not submit the payment.

The [client implementation](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L360) separates action from evidence delivery. If evidence upload fails after payment, repairing the record must not charge the owner again. Neither authorization nor signed execution metadata proves settlement or energy delivery.

## Check it yourself

Follow the [governed-action walkthrough](https://docs.genesismesh.org/sdk/typescript/governance.html) with a local authority, setup credentials, registered executor key, active policies and enabled evidence store.

Use its non-payment callback. Expect an allowed request to execute and a denied request to stop before the callback; inspect execution evidence separately. This documented procedure was not executed in this review.

Before connecting money, specify the approved purchase fields and how concurrent requests share the owner's budget.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
