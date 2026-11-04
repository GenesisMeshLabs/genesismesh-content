# Your agent has an identity. Is it still the same agent?

An illustrative procurement assistant restarts with yesterday's identity key, a changed prompt and a new purchasing tool. Should the same identity still receive the same permission?

[AgentDID](https://arxiv.org/abs/2604.25189) researches agent identity and execution-state verification; Genesis Mesh's mechanism is a narrower configuration declaration.

## Check the declaration before the action

Genesis Mesh's [beta logic-attestation functions](https://docs.genesismesh.org/reference/public-contract.html) create a signed `ModelAttestation` containing model identity, prompt and tool hashes, timestamps and an optional token identifier. An operator supplies trusted agent keys and an `AttestationPolicy`; `verify_model_attestation` checks signature, expiry and configured model, prompt-hash and tool-hash allowlists. A `LogicAttestationGate` integrates that check into a local boundary evaluation. [Implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L86).

For our assistant, a declared prompt change can trigger `system_prompt_not_permitted`. Empty allowlists permit any value, however. The recorded model version is not allowlisted, and `require_bound_token` checks token presence, not equality with an expected invocation token. Additional restrictions require consuming-application checks.

The signature binds the signer to its declaration. It does not measure the running process: a compromised signer could declare approved settings while executing something else.

Permission remains separate. A Network Authority, the operator-controlled service issuing and evaluating trust records, evaluates local policy. The relying application authenticates the caller, binds the decision to the requested action and controls execution. The [attestation-backed guide](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) describes this boundary. A valid declaration alone must not become permission to purchase.

## Check it yourself

With a local checkout, [installed dependencies](https://docs.genesismesh.org/installation.html), signing key, trusted public key and operator policy, follow the [logic-attestation walkthrough](https://docs.genesismesh.org/examples/verifiable-logic-attestation.html):

`python docs/examples/assets/scripts/verifiable-logic-attestation-demo.py --no-gif`

Expect acceptance for a permitted declaration and refusal for a changed prompt or tool set. Inspect the policy fields before interpreting that result. This documented example was not executed in this review.

Before an agent update, identify what identity establishes and what the execution boundary must check again.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
