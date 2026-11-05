# Can a credential reveal your organization even when it hides your name?

A contractor needs to show a dataset service that it has permission to read a particular collection. The contractor would prefer not to reveal every capability in its agreement. It also wants to avoid exposing which organization issued its credentials. In this illustrative case, those are two different privacy requirements, and meeting one does not establish the other.

The [IRAC research](https://arxiv.org/abs/2512.20234) examines issuer-hiding credentials: revealing the issuer can expose sensitive context about a holder even when the holder's own identity is hidden. Genesis Mesh does not claim to implement IRAC. Its selective-disclosure example provides a narrower starting point for examining what an actual capability proof reveals.

## Begin with the information the verifier needs

The dataset service needs evidence about the requested capability, plus the trust and policy context required to accept it. Giving the service an entire agreement may expose unrelated capabilities. The [selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) demonstrates a Merkle commitment to a capability set, followed by a proof that one capability belongs to that set.

A Merkle tree connects hashes of individual values to one root hash. The holder presents the selected capability and the hashes needed to reconstruct its path to that root. The verifier can check membership without receiving the complete list of capability strings. That reduces what must be sent in the interaction; it does not automatically conceal every fact about the agreement or its participants.

The concrete Genesis Mesh artifacts are `CapabilityCommitment` and `CapabilityMembershipProof`. The [model definitions](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) are important here because a privacy review must inspect the serialized fields, not rely only on a diagram showing a hidden list.

The commitment includes the Merkle root and capability count, but also the agreement identifier, issuer sovereign identifier and timestamp. The proof includes the revealed capability, leaf hash, path and prover identifier. These are visible metadata. Calling the output "selective disclosure" does not make the issuer anonymous or hide the existence of the underlying agreement.

## Follow the commitment and proof

The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) builds the commitment from the agreed capability set and signs it with the issuer's key. In the contractor example, the issuer is the party whose commitment the service is willing to accept. Selecting that issuer and its verification key is a trust decision made by the receiving operator.

The holder keeps the agreement locally and constructs a proof for the requested capability. The service checks the commitment signature and the relationship between the revealed capability, its leaf hash, the proof path and the signed root. A changed capability cannot simply be substituted into an otherwise unchanged proof and treated as verified.

The [selective-disclosure gate](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) also checks that the commitment's agreement identifier and revealed capability match the request context. This matters because a valid membership proof is about a particular committed set. It is not a universal credential for any agreement or any request that uses a similar-looking capability label.

After verification, the dataset service still decides whether to execute the requested read. The resource, current relationship and operation parameters remain part of that decision. The proof does not contact every authority involved or establish that a previously acceptable permission remains current. A cryptographically valid membership result and a present authorization result answer different questions.

## What remains visible or inferable

For the contractor's first requirement, the mechanism can avoid transmitting the full capability list. For its second requirement, the visible `issuer_sovereign_id` directly defeats a claim that the issuer is hidden. The agreement and prover identifiers can also help a recipient correlate presentations. The [serialized model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) makes those boundaries inspectable.

There is a further limit in the leaf construction. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) hashes capability strings without a salt. When possible capability names come from a small, predictable dictionary, an observer can hash candidate names and compare them with exposed hashes. The exact inference depends on the tree and visible path, but an unsalted hash is not a strong secrecy promise for a guessable value.

The right claim is therefore selective transmission of capability information, with visible metadata and possible inference. This is not formal zero-knowledge proof, issuer-hiding authentication or general anonymity. A membership proof alone also does not provide freshness or replay prevention. The relevant disclosure commands and public functions are classified as [beta](https://docs.genesismesh.org/reference/public-contract.html).

For an operator designing a privacy-sensitive service, the practical exercise is to write down what each recipient can see. Include identifiers, counts, timestamps, repeated presentations and the recipient's existing knowledge. If concealing the issuing organization is essential, this implementation does not satisfy that requirement merely because it omits the other capability strings.

## Check it yourself

Use a disposable [development installation](https://docs.genesismesh.org/installation.html), the example agreement and synthetic issuer/prover keys. Follow the local walkthrough:

```text
python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif
```

Inspect both `commitment.json` and `proof.json` before evaluating the privacy claim. The documented valid proof should verify; changing the revealed capability without changing its matching leaf produces `leaf_hash_mismatch`. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py) provide source coverage for verification failures. Compare visible identifiers with the information your service actually needs. Neither the example nor tests were executed in this review.

## Further reading

- [Selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html)
- [Public surface stability](https://docs.genesismesh.org/reference/public-contract.html)
- [IRAC issuer-privacy research](https://arxiv.org/abs/2512.20234)

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/) | [Public demo](https://mesh.genesismesh.org/) | [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
