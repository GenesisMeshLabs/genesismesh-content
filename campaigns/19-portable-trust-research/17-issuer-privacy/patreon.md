# Can a credential reveal your organization even when it hides your name?

A contractor wants access to a research dataset. The service only needs to learn that the contractor has the required capability. Yet the credential may identify the organization that issued it, the underlying agreement or a stable identifier that links several visits.

This illustrative case shows why removing a person's name is not the same as minimizing disclosure.

[IRAC research](https://arxiv.org/abs/2512.20234) addresses issuer-hiding anonymous credentials: proving eligibility without singling out the issuer from an approved set. Its construction and privacy claims belong to that paper. Genesis Mesh's selective-disclosure example uses a different mechanism, with different visible information.

## Start with the exact artifact

The Genesis Mesh [selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) demonstrates a signed commitment to a capability set. A holder presents one capability and a Merkle path that lets a verifier recompute the committed root. The complete capability list does not have to travel with that proof.

The actual [models](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) make the privacy boundary clearer than a slogan. `CapabilityCommitment` includes the capability count, `agreement_id`, `issuer_sovereign_id`, timestamp and signature. `CapabilityMembershipProof` includes `prover_sovereign_id`, the revealed capability and its path. Those fields remain visible. This is not issuer anonymity, and it does not hide the agreement identifier in the commitment.

For the dataset service, the operator first chooses which issuer keys it accepts. In the reference implementation, `commit_capabilities` builds and signs the commitment; `prove_capability_membership` creates a proof; `verify_capability_proof` checks the issuer signature, leaf and path against that commitment. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) also contains a gate that compares the commitment's agreement and the revealed capability with the requested context.

That is where the service's authority boundary belongs. A proof for one capability must not become permission for a different operation or an unrelated agreement. The service still owns its access policy and the actual dataset response. The Network Authority, where used for a broader governed flow, is the operator's decision service; it does not make a membership proof anonymous or execute the data transfer.

## Fewer fields are not a complete privacy guarantee

The commitment uses hashes of capability strings. Common, guessable capability names can be tested against exposed hashes. The guide explicitly distinguishes this mechanism from formal zero-knowledge proofs. It also leaves the count visible, and a repeated identifier may create linkage. These limits matter even when the full list is absent.

The verifier's success result proves the particular signature and membership checks it performs. It does not prove that the presenter is anonymous, that the commitment is freshly authorized for every use, or that copied evidence cannot be replayed in an application. Those properties need their own protocol and enforcement design. The accompanying [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py) cover proof failures; they are not a privacy certification.

The selective-disclosure functions and CLI are beta surfaces in the [public contract](https://docs.genesismesh.org/reference/public-contract.html).

## Check it yourself

Use the [development installation](https://docs.genesismesh.org/installation.html) and the walkthrough's agreement and signing-key prerequisites. Run its local example:

```text
python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif
```

Inspect both the proof and the commitment, not only the terminal's "valid" result. List every identifier, timestamp, count and disclosed capability the verifier receives. The documented valid proof should verify; a modified revealed capability without a matching leaf produces `leaf_hash_mismatch`. This example was not executed in this review.

Before deploying, write down what the verifier must learn and what it should not learn. Compare that list with the serialized artifacts. Selective disclosure is useful when its actual boundary matches the privacy requirement.

[Website](https://genesismesh.org/)  |  [Documentation and local demo](https://docs.genesismesh.org/examples/selective-disclosure.html)  |  [Public console](https://mesh.genesismesh.org/)  |  [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)
