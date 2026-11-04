# How do you revoke one delegation without breaking everything?

Imagine a reporting service with two permissions: finance grants invoice access; operations grants maintenance access. Finance withdraws its permission. Should the unrelated maintenance work stop?

The [VERA paper](https://arxiv.org/abs/2608.30091) studies preserving independent authority paths when one delegation is revoked; that research contract is not an implemented Genesis Mesh guarantee.

Genesis Mesh's [beta delegation-chain workflow](https://docs.genesismesh.org/examples/delegation-chain.html) makes the authority behind a request inspectable. In our illustrative scenario, finance starts with an `AgreementRecord` granting `invoices.read`. It creates a `DelegatedAgreementRecord` for the reporting agent, which cosigns the handoff. The CLI provides `trust delegate create`, `cosign` and `verify`.

Each hop identifies its parent and binds its terms. The [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390) checks linkage, capability containment, validity limits and signatures. An attempted extra capability fails; changed parent terms break the stored digest. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603) cover scope escalation.

This establishes a supplied chain's integrity. It does not discover every alternative path, prove current permission to execute, or automatically stop work already dispatched. The consumer must check the root agreement's current validity and apply its own execution policy.

For the reporting service, that means identifying which agreement justified each request, deciding how withdrawals reach consumers, and separately evaluating the maintenance agreement. A valid signature alone cannot establish that invoice access is still permitted. Precise graph-wide revocation requires additional runtime behavior and testing.

## Check it yourself

Use the [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) from an installed source checkout, with its example agreement, operator keys and recognition graphs:

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

The controlled-time example verifies a two-hop chain and refuses a capability outside its parent's scope. Inspect the parent identifiers and terms digest to see exactly what the permission depends on. This documented example was not executed in this review.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
