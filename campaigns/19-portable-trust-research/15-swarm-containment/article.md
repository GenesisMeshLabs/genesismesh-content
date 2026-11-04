# Can a swarm limit a compromised member?

A coordinator delegates a dataset-reading task to a specialist. The specialist is compromised and asks to modify the dataset. This illustrative handoff needs both narrow authority and a receiving service that enforces it.

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) studies confinement under a compromised-model assumption; its broker results are not a Genesis Mesh containment guarantee.

## Check every handoff

The Genesis Mesh [delegation example](https://docs.genesismesh.org/examples/delegation-chain.html) starts from a signed `AgreementRecord`. Each `DelegatedAgreementRecord` names its parent, delegator, recipient and delegated terms, binds the parent's terms by digest, and carries both parties' signatures.

The [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) checks the root agreement's signatures, links, digest, capability subset, expiry ceiling and delegation signatures. After the first hop, the delegator must be the preceding recipient. The specialist cannot produce a valid chain that widens reading authority into modification.

That does not authorize a specific dataset operation. The receiver still checks the current relationship, requested resource and parameters before executing. The chain's capability check is not a general resource-policy engine.

A separate [process-level guard](https://docs.genesismesh.org/examples/process-level-mediation.html) can constrain its execution path only when the operator removes bypass routes and direct credentials. Its [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py) has an in-memory budget that resets on restart and makes no revocation fetches: new token revocations remain unseen, while expiry and other local checks still apply. It is not kernel or hardware attestation. Delegation and guard CLI commands are [beta](https://docs.genesismesh.org/reference/public-contract.html).

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html), the root agreement, parties' keys and recognition-graph exports:

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

The [walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) accepts a valid handoff and refuses a capability outside the parent's set. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) also cover forged widening and unauthorized later-hop delegators. Neither example nor tests were executed in this review.

[Website](https://genesismesh.org/) | [Documentation/local demo](https://docs.genesismesh.org/examples/delegation-chain.html) | [Public console](https://mesh.genesismesh.org/) | [Source](https://github.com/GenesisMeshLabs/genesismesh)
