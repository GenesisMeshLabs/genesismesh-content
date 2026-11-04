# Prove permission without exposing the whole payment trail

An illustrative charging service needs to check one device permission. Must it also receive the device's unrelated capabilities and relationships?

[Offline digital-euro research](https://arxiv.org/abs/2407.13776) explores a protocol using Groth-Sahai zero-knowledge proofs; Genesis Mesh's selective disclosure is a different, narrower primitive.

## Reveal the capability, inspect what remains visible

Genesis Mesh's [beta selective-disclosure functions](https://docs.genesismesh.org/reference/public-contract.html) construct a signed `CapabilityCommitment` over a capability set. A holder presents a `CapabilityMembershipProof` for one capability. The verifier uses trusted issuer keys to check the signature, leaf hash and Merkle path without receiving the full list. [Implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L156).

The local `SelectiveDisclosureGate` also requires the commitment's agreement to match the request's agreement, and the revealed capability to match the requested capability. A proof for reading an account must not become permission to purchase. [Gate](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L308).

The consuming application still authenticates the requester, applies current authorization policy and controls execution. Membership in a signed set does not establish ownership of a payment credential, an owner's purchase mandate or settlement. The charging adapter remains an illustrative integration.

What is disclosed still matters. The [commitment schema](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py#L20) includes `agreement_id`, `issuer_sovereign_id`, `capability_count` and a timestamp; the proof includes a prover identifier. These fields can expose relationships or link events. Deterministic hashes also do not guarantee secrecy for predictable capability names.

This is a Merkle membership proof, not a formal zero-knowledge protocol or a promise of anonymous commerce. Evaluate privacy against every record the counterparty receives, not just the omitted capability list.

## Check it yourself

With a local checkout, installed dependencies and trusted issuer keys, follow the [selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html):

`python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif`

Inspect a valid proof and the identifiers it exposes. The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py#L256) covers refusal for an invalid signature or mismatching root. The documented example and test source were inspected, not executed in this review.

Before using this pattern, name the exact privacy property you need and test the complete disclosure.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
