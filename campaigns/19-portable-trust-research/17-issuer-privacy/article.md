# Can a credential reveal your organization even when it hides your name?

A contractor needs to prove access to a dataset. In this illustrative case, the verifier needs one capability, not the contractor's entire affiliation trail.

[IRAC research](https://arxiv.org/abs/2512.20234) explores issuer-hiding credentials; Genesis Mesh's selective-disclosure example uses a different mechanism and does not implement that privacy guarantee.

## Inspect the commitment too

The [Genesis Mesh walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) signs a Merkle commitment to a capability set. The holder presents one capability and a path to that root instead of the complete list.

The [actual models](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) still expose the capability count, agreement ID, issuer ID and timestamp in `CapabilityCommitment`; `CapabilityMembershipProof` also names the prover. These are visible metadata, not issuer anonymity.

Using issuer keys chosen by the operator, `verify_capability_proof` checks the signature, leaf and path. The [context gate](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) separately compares the commitment's agreement and revealed capability with the requested operation. The dataset service still owns access policy and execution.

Leaves are unsalted hashes of capability strings. Guessable names can be tested against exposed hashes; this is not a formal zero-knowledge proof. A valid membership result does not establish anonymity, fresh permission or replay prevention. These functions and CLI commands are [beta](https://docs.genesismesh.org/reference/public-contract.html).

## Check it yourself

Use the [development installation](https://docs.genesismesh.org/installation.html) and the walkthrough's agreement and signing keys:

```text
python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif
```

Inspect both serialized artifacts. List every identifier, timestamp, count and capability received by the verifier. A valid proof should verify; changing the revealed capability without updating its leaf produces `leaf_hash_mismatch`, as covered by the [source tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py). This documented example was not executed in this review.

[Website](https://genesismesh.org/) | [Documentation/local demo](https://docs.genesismesh.org/examples/selective-disclosure.html) | [Public console](https://mesh.genesismesh.org/) | [Source](https://github.com/GenesisMeshLabs/genesismesh)
