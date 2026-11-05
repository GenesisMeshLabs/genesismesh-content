# How do you revoke one delegation without breaking everything?

A logistics company authorizes a coordinator to read shipment status. The coordinator delegates part of that work to a regional service, which delegates again to a routing agent. Later, the company withdraws the regional service's role. Should the routing agent lose every permission, including one granted through an unrelated partner?

That is an illustrative scenario, but the ambiguity is real: removing one delegation and disabling an identity are different operations. [VERA's research on authority-preserving edge revocation](https://arxiv.org/abs/2608.30091) examines how valid alternative paths can survive a withdrawal. Its graph model is a research contribution, not a capability this article attributes to Genesis Mesh.

## Make the path explicit

Genesis Mesh's beta [delegation-chain workflow](https://docs.genesismesh.org/examples/delegation-chain.html) addresses a narrower foundation: checking the authority represented by a supplied chain. Instead of accepting “the coordinator said I could,” a receiver gets records identifying the parties, the parent agreement and the capabilities passed onward.

The root is an `AgreementRecord`. A delegated hop uses a `DelegatedAgreementRecord`, signed by the delegator and delegate, with a reference to its parent and a digest binding the parent's terms. Further hops build on that record. In our scenario, the routing service can inspect the coordinator-to-region-to-agent path before considering the requested shipment read.

The verifier checks parent linkage, bound terms, capability containment, expiry ceilings and signatures. A child may retain or narrow its parent's capabilities; it cannot introduce an additional capability. These checks are implemented in the [pinned delegation verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py#L283-L390).

That makes a concrete refusal possible. If the regional service received only shipment-reading authority, its child record cannot add shipment cancellation. Likewise, changing the parent's terms does not leave a valid child silently attached to the altered agreement: the digest comparison detects the mismatch. The [scope and tampering tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) document those cases as source assertions; they were not run for this article.

## What the receiving system must decide

A verified chain answers whether these records form an acceptable delegation under the checked rules. It does not establish that the root authority is still valid for a new action right now.

This distinction matters at the moment of withdrawal. A previously issued chain can remain cryptographically intact even after an operator decides that its authority should no longer be accepted. The receiver needs a current authorization policy for that decision. Chain verification alone does not supply a live revocation service or search a graph for another surviving path.

For the logistics operator, the integration question is therefore precise: which authority basis is this request presenting, and what current policy allows us to accept it? If a second partner relationship exists, it needs its own valid basis. The application cannot infer that relationship merely because the agent has the same identity.

Genesis Mesh's [boundary-policy workflow](https://docs.genesismesh.org/examples/declarative-boundary-policy.html) is useful background for the separate policy decision. It does not turn the delegation example into an implementation of VERA. The organization still chooses which sources, policy and freshness requirements govern its own receiving boundary.

The executor owns the final resource boundary. It must map the verified capability to the actual shipment operation and retain control of the credentials that perform it. A check for reading shipment status cannot authorize cancellation simply because both actions use the same backend API.

## Design the withdrawal before the incident

A useful operational review starts with three questions. Which agreement or delegated hop is being withdrawn? Which receivers must learn about that change? What happens to a request that was already accepted?

Those questions prevent a misleading success criterion. Removing a record from a local list is not evidence that every receiver has stopped accepting its older copy. Nor does refusing the next request undo a cancellation already sent to a carrier. The chain verifier is a validation mechanism, not a distributed cancellation system.

Keep these responsibilities visible when designing the integration: the grantor defines scope, each delegator stays within it, the receiver establishes present acceptability, and the executor binds the decision to the operation. A signed history helps explain how authority arrived; current-use policy decides whether it remains usable.

For workflows that also need a short-lived invocation credential, the beta [invocation-token guide](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) describes a separate artifact. Its issuer validation and usage accounting have their own limits. Adding that token should not be described as automatic global revocation.

## Check it yourself

Use an installed source checkout and the [delegation-chain example](https://docs.genesismesh.org/examples/delegation-chain.html). The demo supplies its example keys, agreement records and a controlled scenario clock:

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

Expect a valid two-hop chain to verify and a delegation outside its parent's capability scope to be refused. Inspect the parent references and terms digests alongside the result. The script's fixed scenario time is intentional; do not reuse historical validity dates as fresh operational credentials.

This documented example was not executed in this review. It checks the supplied chain, not a live withdrawal propagated across several organizations. A deployment test should separately demonstrate that the receiver refuses a withdrawn basis and cannot execute the protected operation through an unchecked route.

## Further reading

- [Delegation chains](https://docs.genesismesh.org/examples/delegation-chain.html): records, signatures and the local example.
- [Declarative boundary policy](https://docs.genesismesh.org/examples/declarative-boundary-policy.html): the separate policy decision.
- [Invocation-bound tokens](https://docs.genesismesh.org/examples/invocation-bound-tokens.html): scoped credentials and their limits.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
