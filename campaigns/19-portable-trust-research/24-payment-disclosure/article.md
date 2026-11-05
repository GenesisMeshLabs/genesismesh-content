# Prove permission without exposing the whole payment trail

A service needs to know whether a device may request a purchase. Does it also need the device's unrelated permissions, organizational relationships and past transactions?

In this illustrative design problem, the first task is to identify the exact fact each participant needs. “Give every participant the whole signed record” can make verification convenient while exposing information that was never necessary for the decision.

[Research on an offline digital euro using Groth-Sahai proofs](https://arxiv.org/abs/2407.13776) explores a payment protocol with zero-knowledge techniques, offline transfer and retroactive double-spending detection. It includes an initial implementation. Its privacy claims belong to that protocol and its assumptions; they are not properties inherited by any system that signs a permission.

Genesis Mesh has smaller, concrete mechanisms worth examining, with limits worth keeping visible.

## Reveal one capability, inspect the surrounding record

The reference implementation's [beta selective-disclosure functions](https://docs.genesismesh.org/reference/public-contract.html) can construct a signed `CapabilityCommitment` over a set of capabilities. A holder builds a `CapabilityMembershipProof` for one capability. The verifier checks the commitment's signature, the revealed capability's leaf hash and the Merkle path back to the committed root. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L156) does not require sending the full capability list in that proof.

This is a Merkle membership proof, not a formal zero-knowledge protocol. A successful check establishes membership in the supplied signed commitment. It does not establish a payment balance, an owner's current purchase mandate or a merchant's right to receive money.

The surrounding fields matter. The [commitment schema](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py#L20) includes `agreement_id`, `issuer_sovereign_id`, `capability_count` and a timestamp. The proof includes a prover identifier. Those identifiers remain visible in the normal records. A design that needs to hide the issuer or make transactions unlinkable cannot claim those properties simply because the full capability list is absent.

Predictable capability names also make broad secrecy claims unsafe. The scheme uses deterministic hashes. The absence of plaintext is not proof that a verifier cannot infer information from a small set of possibilities.

## Bind the disclosed fact to the request

Genesis Mesh's `SelectiveDisclosureGate` checks two important relationships after proof verification: the commitment's agreement must match the request's agreement, and the revealed capability must match the requested capability. [Gate implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L308).

For a conceptual charging request, proving one capability should not authorize a different service. A proof for reading an account should not silently become permission to buy something.

The gate still relies on the consumer's choice of trusted issuer keys and its surrounding authentication and authorization path. It does not prove that the presenter owns a payment credential or that the underlying agreement remains acceptable under every current condition. Payment-specific replay protection, mandate limits and settlement are separate integration work.

The [documented walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) is useful for learning the primitive. Its broad introductory privacy wording should be read alongside the actual record fields above. The concrete claim is reduced disclosure of the capability set, not anonymous commerce.

## Minimize what the authority records too

A Network Authority is the service operated by a sovereign domain to issue and evaluate trust records. For its configurable policy gates, `disclose_input` defaults to false: the gate's recorded input describes presence and type rather than copying the raw value. The [policy model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/boundary_policy.py#L106) and [input-recording code](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/context/registry.py#L183) show this distinction.

That setting does not hide the request from the authority evaluating it, encrypt every log or control a merchant's records. Data minimization requires reviewing the complete path: request, decision, evidence, monitoring and retention. Stable identifiers and timestamps may still connect events even when individual values are omitted.

The useful starting point is therefore a disclosure inventory, not a promise of privacy. For every field, name who receives it, why that party needs it and how long it persists.

## Evaluate the whole exchange, not one proof

For the illustrative charging service, start with a recipient-by-recipient inventory. The gatekeeper might need to verify one capability; a payment provider might need transaction details; an operator might retain evidence for troubleshooting. Those requirements do not mean every participant should receive the same record.

The [selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) supplies a concrete object to inspect. Alongside its omitted capability list, record the agreement and issuer identifiers, the count, the timestamp and the proof's presenter identifier. Ask whether another record exposes the same values. A smaller payload can still carry a stable link between interactions.

The hash construction deserves the same scrutiny. Capability leaves are deterministic, unsalted hashes of capability strings in the [tree builder](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py#L94). A small vocabulary of likely capability names may let a recipient test guesses against exposed hashes. The exact leakage depends on the proof and surrounding information; no attack was executed for this article.

A practical acceptance criterion would therefore be specific: the recipient should receive the required capability proof and only the additional metadata the application intentionally discloses. Test that criterion across requests, responses, audit records and logs. It is a design objective to validate, not a property established simply by choosing the word privacy for the feature.

## Check it yourself

With a local checkout and installed dependencies, follow the [selective-disclosure demo](https://docs.genesismesh.org/examples/selective-disclosure.html):

`python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif`

Inspect the generated commitment and proof. Confirm that the proof omits the full capability list, then list the identifiers it still exposes. The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py#L256) includes invalid signatures and a mismatching root; inspect those refusal cases too. This is a documented example and source review, not an execution performed for this article.

Before applying the idea to payments, define a precise privacy property, such as hiding unrelated capabilities, and test that property across every record the counterparty receives.

## Further reading

- [Selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html)
- [Declarative boundary policies](https://docs.genesismesh.org/examples/declarative-boundary-policy.html)
- [Public contract and beta classifications](https://docs.genesismesh.org/reference/public-contract.html)
- [Website](https://genesismesh.org/)
- [Documentation](https://docs.genesismesh.org/sdk/index.html)
- [Public demo](https://mesh.genesismesh.org/)
- [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)

The public demo is a trust-system interface, not a demonstration of this illustrative application.
