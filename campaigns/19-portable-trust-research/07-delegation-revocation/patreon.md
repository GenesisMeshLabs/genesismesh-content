# How do you revoke one delegation without breaking everything?

Imagine a reporting service used by two departments. Finance permits it to read invoices; operations permits it to read maintenance records. Finance withdraws its permission. The service should lose the invoice path without losing an independently valid maintenance path.

That is an illustrative design problem, not a Genesis Mesh customer deployment. It exposes a question that "revoke the agent" leaves unanswered: are we withdrawing an identity, a credential, a relationship, or one route by which authority reached the agent?

The [VERA paper](https://arxiv.org/abs/2608.30091) studies this distinction in delegation graphs. Under its stated model, removing an edge should remove authority only where no independent authorizing path remains. Its research contract is a useful design target. It is not evidence that Genesis Mesh implements VERA's graph algorithm or preserves every alternative path automatically.

## Start with the authority a request actually uses

Genesis Mesh provides a narrower, inspectable building block: a [beta delegation-chain example](https://docs.genesismesh.org/examples/delegation-chain.html). A root `AgreementRecord` describes agreed capabilities. A `DelegatedAgreementRecord` links to its parent, identifies the parties and carries delegated terms. Both sides sign the handoff.

For our reporting example, a finance agreement could grant `invoices.read`. Finance delegates that capability to a reporting agent, which may pass a subset onward. The CLI exposes `trust delegate create`, `cosign` and `verify`. This gives an operator concrete records to inspect instead of inferring authority from an agent's role description.

The [chain implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390) checks parent linkage, terms digests, capability containment, validity limits and signatures. It rejects a handoff that tries to add a capability absent from its parent. The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py#L552-L603) includes widening and verification failures; those tests were inspected, not executed for this article.

This matters when a permission changes. The consumer can identify which parent agreement and which chain justified a request. It need not treat every task performed by the same identity as one inseparable permission.

## The chain is evidence, not a revocation service

There is an important boundary. Verifying one supplied chain does not discover every other path through a multi-parent graph. Nor does a locally valid signature establish that an operator's current policy still permits an action.

The documented workflow requires a separate check of the root agreement's current validity. A change to the parent's terms invalidates the stored terms binding, requiring renewal; that is different from proving correct edge revocation across a whole graph. The inspected chain verifier does not provide VERA's alternative-path preservation service. [Delegation limits](https://docs.genesismesh.org/examples/delegation-chain.html)

A practical integration therefore needs an explicit withdrawal model: what record is withdrawn, how consumers learn it, which future requests are re-evaluated, and how already dispatched work is handled. Those are application and operating decisions. Calling a signature "revoked" without defining the observation point hides the real failure mode.

For independently authorized work, evaluate the other agreement on its own merits. Do not manufacture a new permission simply because one path disappeared, and do not promise that every unrelated task survives unless the runtime actually implements and tests that behavior.

## Check it yourself

Use the [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) with an installed Genesis Mesh checkout, a root agreement, operator keys and the example recognition graphs. Its local demo is:

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

Follow the create, cosign and verify steps. The documented valid chain is accepted. Then try a capability outside the parent scope: creation must refuse it. The walkthrough also explains wrong-key and parent-terms failures. This is a documented example, not executed in this review.

Use that exercise to draw your own authority paths. Before designing a revoke button, name exactly what it withdraws and where that withdrawal takes effect.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
