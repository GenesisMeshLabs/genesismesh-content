# Offline trust and revocation: what a disconnected system can know

*How pre-issued grants bound authority, and what happens when the network returns.*

Consider an illustrative outage: a controller disconnects at 10:00. Its operator revokes a permission at 10:05. At 10:06, the controller receives a request that would previously have been allowed.

The signature still verifies. The revocation has not reached it.

Offline trust starts with that limit. A disconnected system can verify information it holds; it cannot discover a change nobody has delivered. The practical questions are which actions may continue, within what bounds, and what can be established afterwards.

## Authorize a bounded change before the outage

In Genesis Mesh, each sovereign operates a Network Authority (NA), the service that issues signed trust records and policy decisions. A **pre-issued grant** lets that authority authorize a bounded class of changes before a controller loses connectivity.

The [worked example](https://docs.genesismesh.org/examples/pre-issued-grants.html) follows a remote controller rotating a service credential. A policy caps credential lifetime at 90 days. The authority issues a narrower grant:

- One registered bearer key and the capability `secret.manage`.
- Four hours of validity and three uses in total.
- At most two uses after the chain position named by a signed time token.
- A closed parameter envelope: integer `lifetime_days` values from 1 to 60.

The [issuance check](https://github.com/GenesisMeshLabs/genesismesh/blob/8d0869b75f107bde4cae3b6a9e2be99dca47fcb7/genesis_mesh/trust/grants.py#L645-L736) must establish that the applicable enforce-mode policies allow every request the envelope permits throughout the grant's validity. A range reaching 400 days can fail with `grant_gate_may_deny`. A gate depending on a per-request external fact, such as `attributes.owner`, cannot simply be assumed safe in advance.

The [grant routes are beta](https://docs.genesismesh.org/reference/public-contract.html) and require these opt-in authority settings:

```text
EVIDENCE_STORE=on
EVIDENCE_OUT_OF_BAND=on
EVIDENCE_GRANTS=on
```

The [runbook](https://docs.genesismesh.org/operations/grants.html) also covers operational status and verifier compatibility. Enabling the authority does not upgrade every consumer.

## What happens while disconnected

The controller holds its own executor key. Before acting, the [grant-holder implementation examined here](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/src/grant_holder.rs#L630-L692) checks capability, resource scope, parameters, known revocations, key-vouching horizon, validity and budgets.

Two 30-day rotations fit our example. A third needs more than an unused total allowance: the signed time-token budget must permit it too.

Each rotation produces signed `GrantExecutionEvidence`, including the grant digest, unique use ID, sequence, previous-use digest, time token, resource and outcome metadata. The outbox keeps **evidence**, not a general queue of actions to repeat. A credential version identifier belongs in that record; the secret itself does not.

Time tokens constrain what a holder can claim, but do not make its clock trustworthy. The [time rules](https://docs.genesismesh.org/operations/grants.html#time) include a fixed 300-second skew allowance and ordering checks. The upload window equals the grant's validity duration after the claimed execution time: four hours here.

A compromised holder can still backdate within the permitted bounds. Small budgets and short validity reduce exposure; they do not make the device honest.

## Expiry, outage and DENY are different

Do not assume an expired grant means the action cannot run.

The [grant-holder path examined here](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/src/grant_holder.rs#L816-L825) can use explicitly configured **break-glass** when the authority is unavailable and the grant is expired, exhausted or revoked, or its time-token allowance is spent. Without that configuration it refuses. A parameter or resource mismatch does not trigger this fallback.

Break-glass records an exception for later judgement. It does not turn that action into pre-issued authorization. A returned DENY is an authority decision, not an outage, and must not become permission through fallback.

The [edge-agent runbook](https://docs.genesismesh.org/operations/edge-agent.html) describes stricter rules: an NA `429` or `5xx` permits only a covering grant, never break-glass. Connection failure, timeout and specifically classified proxy errors are different paths. A usable covering grant takes priority; if none exists, a held grant naming the capability but excluding the parameters or resource prevents break-glass even with justification. The [classifier](https://github.com/GenesisMeshLabs/sdk-rust/blob/89e5091184680c935d3fd4acea391446dcc6cd9e/edge/src/decision.rs#L50-L80) defines eligible proxy responses precisely.

Consult the [current integration matrix](https://docs.genesismesh.org/sdk/index.html) for the operations and limits of the client you use. Coordinated version numbers do not establish identical fallback behavior.

## Reconnection reconciles what already happened

The controller uploads uses in chain order. The authority checks them and assigns positions in the resource's evidence history. That is admission order, not proof of physical execution order across disconnected devices.

A refused use can still be important evidence. An authentic use rejected for an envelope mismatch or revocation may be retained as quarantine. If it legitimately continues the holder's chain, it keeps that position; admitted-use budgets and chain length are therefore different counts. Other failures, including secret-bearing records and chain gaps, have [different handling](https://docs.genesismesh.org/operations/grants.html#a-refused-use-keeps-its-place).

Revoking a grant rejects uses dated at or after revocation. Retiring a compromised bearer key rejects its signed uses regardless of claimed execution time. Neither undoes a rotation already performed offline. The holder learns new revocations only when it receives fresh state.

## Check it yourself

The repository provides a documented local demonstration. From a prepared checkout, with its dependencies installed:

```bash
python docs/examples/assets/scripts/pre-issued-grants-demo.py --no-gif
```

This is a documented example, not executed in this review. Follow the [linked walkthrough](https://docs.genesismesh.org/examples/pre-issued-grants.html). It shows covered uses admitted and an authentic out-of-envelope use quarantined.

Then test an isolated resource or fake action: revoke during an outage, exhaust the token budget, expire the grant, return a DENY and reconnect. Capture four things: the request, local authorization basis, actual side effect and authority's later treatment.

Finally, compare the records with an external change log and verify an audit pack using [the offline verifier](https://docs.genesismesh.org/operations/independent-verification.html). Supply independently held keys and anchors. This second implementation is a same-project port, so agreement cannot rule out a mistake both implementations share.

## Further reading

- [Grant walkthrough](https://docs.genesismesh.org/examples/pre-issued-grants.html): issue a bounded grant and inspect admitted and quarantined uses.
- [Grant runbook](https://docs.genesismesh.org/operations/grants.html): envelopes, time tokens, revocation and reconnect limits.
- [Edge-agent runbook](https://docs.genesismesh.org/operations/edge-agent.html): the device's distinct fallback and freshness rules.
- [Offline verification](https://docs.genesismesh.org/operations/independent-verification.html): independently held keys, anchors and the second verifier's limits.

Find more on the [website](https://genesismesh.org/), [documentation](https://docs.genesismesh.org/), [public trust console](https://mesh.genesismesh.org/) and [source repository](https://github.com/GenesisMeshLabs/genesismesh). The console is not a demonstration of an offline device.
