# Your agent has an identity. Is it still the same agent?

A procurement assistant restarts after an update. It presents the same identity key as yesterday, but its system prompt has changed and a new purchasing tool is available. Should yesterday's identity check be enough to let it act?

This is an illustrative scenario. The operator has at least three questions: who is presenting the request, what configuration is being declared, and what that requester may do now. One successful check cannot answer all three.

[AgentDID](https://arxiv.org/abs/2604.25189) explores identity authentication and dynamic execution-state verification for agents, including a challenge-response mechanism. It is useful research context for this separation. It does not establish that Genesis Mesh implements AgentDID or can prove that a remote agent is uncompromised.

## A declaration the operator can check

Genesis Mesh's reference implementation provides a narrower mechanism: a signed `ModelAttestation`. The logic-attestation functions are classified as beta in the [public contract](https://docs.genesismesh.org/reference/public-contract.html). It contains an agent identifier, model identifier and version tag, hashes of the system prompt and tool list, timestamps, and an optional token identifier. The raw system prompt is hashed when the attestation is created. These are concrete fields in the [record model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/attestation.py#L47).

An operator supplies an `AttestationPolicy` and trusted agent public keys. The `verify_model_attestation` function checks the signature and expiry, then compares the declared model, prompt hash and tool hash with the configured allowlists. A `LogicAttestationGate` can add that check to a local boundary evaluation. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L86) makes this an explicit integration step.

For our assistant, the operator could permit the approved model and prompt hash, and a tool list limited to preparing purchase requests. If the assistant honestly declares an added payment tool, the tool-manifest check can refuse it. A declared prompt change can similarly produce `system_prompt_not_permitted`. The [test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_verifiable_logic_attestation.py#L253) contains these refusal cases; those tests were inspected, not executed for this article.

Configuration matters. An empty allowlist permits any value in that dimension. A policy with no allowed prompt hashes does not pin the prompt. The record includes a model version tag, but this verifier's model allowlist checks `model_id`; recording a version is not the same as enforcing an allowed version. If an application needs that restriction, it must implement and review it explicitly.

## What the signature cannot observe

A signed declaration binds the signer to the bytes it supplied. It does not measure the actual process, independently inspect the model host or prove that the declared prompt was used. A compromised signer could declare an approved configuration while running something else. Hashing a prompt also does not make a predictable prompt secret against guessing.

There is another small but significant boundary: `require_bound_token` checks that a token identifier is present. The inspected verifier does not compare it with an expected token for this invocation. That stronger binding belongs in the consuming integration. Neither a populated field nor a reassuring function name should be mistaken for that check. [Verifier logic](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/logic_attestation.py#L86).

Permission remains separate. A Network Authority, the service operated by a sovereign domain to issue and evaluate its trust records, can evaluate a request under an active membership attestation and local policies. The resulting signed decision identifies the attestation and policy basis. The relying application still authenticates the caller and controls execution. The [attestation-backed evaluation guide](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) explains this division.

The practical value is a more precise refusal: “this declared tool set is outside our policy,” alongside a separate decision about the requested purchase. That is more useful than treating a persistent identity as a permanent description of the software behind it.

## Review an update at the execution boundary

For the procurement assistant, an operator could maintain an approved configuration record alongside the deployment procedure. Before an update, the operator would compare the intended model, prompt and tool set with the policy that will actually be loaded. After the update, the controller would verify the new declaration before allowing a purchase request to proceed. This is an illustrative integration procedure, not an additional measurement service supplied by Genesis Mesh.

The [logic-attestation walkthrough](https://docs.genesismesh.org/examples/verifiable-logic-attestation.html) gives the concrete declaration and policy objects to inspect. For this application, the review should ask what happens when one expected hash is absent, when the declaration expires, and when the signing key is no longer trusted. A failed check should produce an explicit stopped request; it should not silently become approval to use yesterday's declaration.

Keep the outcome precise. A valid result says the signed declaration satisfied the configured checks. The operator still needs its own deployment controls to establish what code and configuration actually ran. It also needs a separate purchase decision based on current authority and the requested operation. Preserving those distinctions makes an incident review useful: investigators can identify whether the configuration claim, local permission or downstream execution departed from the intended process.

## Check it yourself

Use a local checkout and the dependencies in the [installation guide](https://docs.genesismesh.org/installation.html). Follow the [logic-attestation walkthrough](https://docs.genesismesh.org/examples/verifiable-logic-attestation.html), or run its documented demo:

`python docs/examples/assets/scripts/verifiable-logic-attestation-demo.py --no-gif`

The prerequisites are an agent signing key, its trusted public key and an operator policy. Compare a permitted declaration with a changed prompt or tool set; the expected result is acceptance for the permitted declaration and a named refusal for the mismatch. Then inspect which fields the policy actually checks. This is a documented example, not executed in this review.

Before your next agent update, write down which facts identity establishes and which facts the execution boundary must establish again.

## Further reading

- [Logic-attestation walkthrough](https://docs.genesismesh.org/examples/verifiable-logic-attestation.html)
- [Attestation-backed evaluation](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html)
- [Public contract and beta classifications](https://docs.genesismesh.org/reference/public-contract.html)
- [Website](https://genesismesh.org/)
- [Documentation](https://docs.genesismesh.org/sdk/index.html)
- [Public demo](https://mesh.genesismesh.org/)
- [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)

The public demo is a trust-system interface, not a demonstration of this illustrative application.
