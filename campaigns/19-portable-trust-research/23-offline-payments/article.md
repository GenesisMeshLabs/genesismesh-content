# What can you trust when an offline payment happens?

An illustrative delivery vehicle loses connectivity at a charger. It holds earlier permission to request service. Does that also prove available funds, prevent double spending or establish settlement?

[PayOff](https://arxiv.org/abs/2408.06956) researches private offline CBDC payments; Genesis Mesh's pre-issued authorization is a separate mechanism, not that payment protocol.

## A grant bounds permission

A Network Authority, the operator-controlled service issuing and evaluating trust records, can use [beta grant routes](https://docs.genesismesh.org/reference/public-contract.html) to issue a signed `CapabilityGrant`. It specifies a registered bearer key, capabilities, validity interval, use budget and closed parameter envelope. Time tokens bound progression from a known chain position. [Grant models](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/grants.py#L266).

The [worked example](https://docs.genesismesh.org/examples/pre-issued-grants.html) authorizes credential rotation within a permitted lifetime range. Adapting that pattern to charging would require an application-specific controller. The grant's use budget does not create a balance, reserve funds or enforce shared spending across wallets.

A holder records signed `GrantExecutionEvidence`, including sequence, previous-use digest, request parameters and reported outcome. On reconnection, the authority checks submitted uses against scope, budget, time-token and revocation rules before admitting evidence. The [use verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/grants.py#L766) defines those checks.

Admission happens after the reported action. Refusing or quarantining evidence cannot undo energy delivery or a payment; the consuming controller remains responsible for actual execution and recovery.

Disconnection also prevents immediate knowledge of a new revocation. Expiry and budgets bound exposure but do not make rolled-back device state tamper-proof. Payment value conservation, replay protection, double-spending handling and final settlement need an independently specified payment protocol. A valid grant establishes none of those guarantees.

## Check it yourself

With a local checkout and installed dependencies, follow the [grant walkthrough](https://docs.genesismesh.org/examples/pre-issued-grants.html):

`python docs/examples/assets/scripts/pre-issued-grants-demo.py --no-gif`

Its setup enables grants, out-of-band records and the evidence store, registers an executor key and activates a lifetime policy. Expect an in-envelope use to be admitted; an out-of-envelope use is refused and retained as quarantine evidence. This documented example was not executed in this review.

For an offline design, identify exactly which claims come from authorization and which require payment-system evidence.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
