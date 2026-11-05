# Your car can pay. Who gave it permission?

An electric vehicle reaches a charger and can authenticate to a payment service. Its owner allowed charging on the journey. Does that authorize any price, any merchant or a subscription bundled into the session?

This is an illustrative design problem. A usable payment credential answers a different question from an owner's bounded mandate.

[Research on CBDC-based machine-to-machine payments](https://portalcientifico.upm.es/en/ipublic/item/9930578) proposes a preliminary model connecting consumer IoT with a two-tier digital-currency architecture. It motivates the machine-commerce setting here. Genesis Mesh is not that payment system, and the flow below is not an implemented EV or CBDC integration.

## Make the mandate an explicit policy input

The owner or fleet operator needs a controller that translates a purchase request into a small set of facts: the authenticated vehicle, charging provider, intended service, amount, currency and authorization window. These are application facts; the integration must obtain and validate them rather than trusting whatever the vehicle supplies.

Genesis Mesh supplies a general authorization mechanism for such a controller. A Network Authority, the operator-controlled service that issues and evaluates trust records, can admit a subject with a signed `MembershipAttestation` and evaluate a requested capability under active policies. The [attestation-backed example](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) uses a vendor's allowed applications to demonstrate this boundary.

An EV integration could adapt that pattern to a charging mandate. Names such as `charging.purchase` or `merchant_id` would be application-defined labels, not existing Genesis Mesh payment APIs.

The policy engine already has concrete gates for required parameters, maximum numeric values, allowlists and claims in the authority-held attestation. Their [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/registry.py#L453) shows how missing or wrongly typed facts are handled. A controller could use integer minor units and an explicit currency to avoid an ambiguous “amount,” but that monetary representation and its validation must be designed by the integration.

A per-request maximum is not an account balance or a daily spending budget. Enforcing a total across concurrent purchases requires additional durable state and concurrency controls. Calling a numeric gate a “wallet limit” would overstate what it does.

## Put the check before the effect

In a supported governed client, `governedAction` composes evaluation, decision verification, a caller-supplied action and execution evidence. It requires trusted authority keys and expected policy bindings; attestation-based authorization also requires the expected attestation. A verified denial does not run the action callback. [Governed-action guide](https://docs.genesismesh.org/sdk/typescript/governance.html).

The payment adapter would be that callback. It remains responsible for checking that the merchant, amount, currency and service it submits are exactly the approved purchase, and for using the payment provider's own authentication and idempotency controls. Genesis Mesh does not supply the payment operation.

After the callback, an executor signs metadata describing the result. Permission, attempted execution and confirmed payment remain different facts. If evidence submission fails after payment, repeating the payment is not a safe way to repair the audit record. The [client implementation](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/src/governance.ts#L360) and its [tests](https://github.com/GenesisMeshLabs/sdk-typescript/blob/8154ca7ac459ffbcd22d35900ca72f8093165bfc/tests/governance.test.ts) distinguish the action from subsequent evidence delivery.

## Let the refusal stop at the right place

Suppose the charger changes its quote before the controller submits the purchase. The adapter should reject the mismatch and obtain a new authorization if appropriate. It should not reinterpret an earlier approval as permission for the changed price.

If the authority denies the original request, the ordinary governed-action path must not call the payment provider. If a payment result is uncertain, the controller needs provider-specific reconciliation before retrying. Neither a signature nor an audit entry guarantees that money moved or that energy was delivered.

That is the useful role for a portable trust layer: make the mandate and its decision inspectable, while the owner, controller, merchant and payment system retain their distinct responsibilities.

## Define the mandate before choosing the payment rail

For the illustrative vehicle, the owner might permit one charging session at an approved provider, within a stated ceiling and a limited time window. A subscription, parking charge or purchase from another merchant would be a different request. Expressing that distinction clearly is the controller's first job, before deciding how a payment provider will move money.

The [declarative-policy walkthrough](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) is a useful starting point for separating facts from rules. The integration would need an unambiguous amount representation, a currency, a validated merchant identity and a specific service. It should explain where each fact came from, and what happens if a required fact is missing. A permissive default for an unknown merchant would defeat the purpose of the owner's mandate.

There is also a concurrency question. If two charging requests each fit a per-request maximum, both could still exceed the owner's intended total. A proposed budget service would need to reserve capacity consistently and release or reconcile that reservation after the provider reports the outcome. That is additional application state, not behavior created by adding a numeric policy gate.

The resulting design has identifiable responsibilities: the owner defines the mandate, the authority evaluates the submitted request, and the controller enforces the approved purchase against the payment provider.

## Check it yourself

Start with a local Network Authority, operator setup credentials, a registered executor key, active policies and the evidence store enabled, as described in the [governed-action walkthrough](https://docs.genesismesh.org/sdk/typescript/governance.html).

Use its documented non-payment callback first. Confirm an allowed request reaches the callback and a denied request does not. Inspect the separate execution evidence and queued evidence result. This is a documented procedure, not executed in this review; it is not a payment demo.

Before connecting money, specify the exact purchase tuple and the durable rule that prevents two concurrent approvals from exceeding the owner's mandate.

## Further reading

- [Attestation-backed evaluation](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html)
- [Declarative boundary policies](https://docs.genesismesh.org/examples/declarative-boundary-policy.html)
- [Governed-action walkthrough](https://docs.genesismesh.org/sdk/typescript/governance.html)
- [Website](https://genesismesh.org/)
- [Documentation](https://docs.genesismesh.org/sdk/index.html)
- [Public demo](https://mesh.genesismesh.org/)
- [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)

The public demo is a trust-system interface, not a demonstration of this illustrative application.
