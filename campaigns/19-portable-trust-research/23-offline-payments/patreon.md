# What can you trust when an offline payment happens?

A delivery vehicle loses connectivity at a charging point. It holds permission obtained earlier, and the charger has a local way to accept a payment. What has each side actually established?

This illustrative situation has several independent questions. Was the vehicle authorized to request this service? Is the payment instrument valid? Can it be spent twice? Has the merchant received final value? When connectivity returns, do the records agree?

[PayOff](https://arxiv.org/abs/2408.06956) studies a CBDC design with private offline payments, holding limits and safeguards for secure-element failure. It also identifies residual privacy leakage and growth in offline message and storage requirements. Its payment mechanisms are not Genesis Mesh capabilities.

Genesis Mesh contributes a different building block: bounded authorization issued before disconnection, with signed evidence examined later.

## What a pre-issued grant contains

A Network Authority is the operator-controlled service that issues and evaluates trust records. With the [beta grant routes](https://docs.genesismesh.org/reference/public-contract.html) enabled, it can issue a signed `CapabilityGrant` for a registered bearer key, defined capabilities, a validity interval, a maximum number of uses and a closed parameter envelope. A signed time token limits how far use can progress beyond a known chain position. These fields are defined in the [grant models](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/grants.py#L266).

The [worked grant example](https://docs.genesismesh.org/examples/pre-issued-grants.html) uses credential rotation. The authority checks a permitted lifetime range against applicable policy before issuing the grant. A range that includes values the policy may deny is refused. The example is an authorization workflow, not a payment demonstration.

In a future charging integration, a similarly bounded grant could express permission for a narrowly defined service request. Merchant identity, amount representation and the connection to the charger would require an application-specific design. A grant's use count does not create a balance, reserve funds or enforce a shared monetary budget across wallets.

## Local action and later admission are different events

A holder operating within a grant records a signed `GrantExecutionEvidence`: the grant identifier and digest, use sequence, previous-use digest, capability, request parameters, time token and reported outcome. When the record reaches the authority, the authority evaluates the use and places admitted evidence in resource history. [Record schema](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/grants.py#L383).

The admission rules include capability and envelope checks, budget, time-token ordering and validity, upload timing and known revocation. The [use verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/grants.py#L766) is explicit about which inputs it needs. The associated [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_grants.py#L336) cover chain order, conflicting positions and out-of-envelope use.

This can make a later discrepancy inspectable. It cannot make an already performed physical or financial action disappear. A quarantined record means the authority refused that evidence under its rules, not that a charger retroactively stopped supplying energy.

Likewise, assigning an order to admitted records is not distributed payment settlement. Two disconnected actors may have acted before either knows the other's state.

## Disconnection leaves an information gap

A disconnected holder cannot learn a revocation that happened after its last update. Expiry, use budgets and time-token limits bound some of that exposure; they do not create live knowledge. The [grant operating guide](https://docs.genesismesh.org/operations/grants.html) also discusses clock trust, key compromise and offline limits.

The holder's state and signing key matter. An attacker who can roll state back or copy authority material creates a different threat from an honest device temporarily losing its network. Later evidence checks and refusal paths must not be described as tamper-proof prevention at every offline endpoint.

A payment protocol must independently specify value conservation, replay and double-spending handling, settlement finality and recovery. A valid Genesis Mesh authorization record does not establish those properties.

## Check it yourself

Use a local checkout with installed dependencies and the [grant demo](https://docs.genesismesh.org/examples/pre-issued-grants.html):

`python docs/examples/assets/scripts/pre-issued-grants-demo.py --no-gif`

The documented setup enables the evidence store, out-of-band records and grants, registers the executor key and activates a lifetime policy. Expect in-envelope uses to be admitted; an out-of-envelope use is refused and retained as quarantine evidence. The example then examines policy change, revocation and audit records. This is a documented example, not executed in this review.

For an offline payment design, draw a separate box for each guarantee. Put Genesis Mesh's grant and evidence checks in the authorization box, and require independent evidence for every claim in the payment box.

Explore [Genesis Mesh](https://genesismesh.org/), the [documentation](https://docs.genesismesh.org/sdk/index.html), the [public trust demo](https://mesh.genesismesh.org/) and the [source repository](https://github.com/GenesisMeshLabs/genesismesh). The public demo is a trust-system interface, not a demonstration of the illustrative application in this article.
