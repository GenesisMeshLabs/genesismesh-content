# Who trusts whom in a 6G network?

Imagine a network operator accepting a request from an edge service run by another company. The connection is encrypted. The service has an identity. The remaining question is local: which claims from that company should this operator accept, and what may the service do here?

This illustrative scenario is relevant to networks built from independently operated functions and infrastructure. It does not describe a deployed Genesis Mesh telecom integration.

The [Beyond Certificates research](https://arxiv.org/abs/2310.19366) explores cross-domain access control with decentralized identifiers and verifiable credentials. Its prototype uses a **5G Service-Based Architecture** to investigate a problem relevant to future 6G systems. Calling it a prototype matters: neither the paper nor this article establishes a deployed 6G network.

## Start with an explicit recognition relationship

Genesis Mesh provides a concrete example of two sovereign domains recognizing one another without sharing an authority. Each domain has its own keys and Network Authority, the service its operator controls for issuing and evaluating trust records.

In the [recognition-treaty walkthrough](https://docs.genesismesh.org/examples/recognition-treaties.html), Sovereign B issues a `MembershipAttestation`. Sovereign A signs a `RecognitionTreaty` that names B, B's accepted keys and the roles A is prepared to recognize. A then checks B's attestation through that treaty.

The signature on the treaty belongs to the accepting domain. B cannot enlarge A's acceptance policy simply by asserting that it is trustworthy. The verifier checks the treaty's status, validity, signature and subject, then applies its allowed-role scope when checking the attestation. These checks are visible in the [treaty verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/treaty.py#L95).

For the telecom scenario, the design idea is to recognize a partner's edge-maintainer role for a defined relationship, while keeping the receiving operator's service permissions local. The role names and telecom adapters would be integration choices. The demonstrated mechanism is the scoped recognition record, not a prebuilt interface to a mobile-network function.

## Recognition needs a second boundary

Accepting an assertion that a service belongs to a partner does not authorize every operation it requests. Reading diagnostic information and changing routing configuration have different consequences.

The receiving application needs to authenticate the requester, map the accepted identity to the local request, and enforce a decision at the service boundary. Genesis Mesh's [attestation-backed evaluation example](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) shows a local authority loading an attestation, applying active policies and signing a `BoundaryDecision`. It explicitly leaves proof that the caller is the attested subject to the relying system.

These are two demonstrated building blocks, not a claim that presenting any foreign attestation automatically feeds the local evaluation route. A telecom integration must define how recognized foreign claims become the appropriate local authorization basis. It must also bind the decision to the exact service operation and preserve the downstream service's own controls.

That separation lets the operator change a local permission without pretending that the partner's identity disappeared.

## The refusal is part of the design

The recognition demo accepts an attestation, revokes the treaty in the accepting domain, then rejects the same attestation with `treaty_locally_revoked`. Tests also cover a role outside the treaty's scope and an empty role scope that grants nothing. [Recognition test source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_recognition_treaties.py).

This is a result at the verifier that has the changed state. It is not instantaneous revocation across disconnected sites. The design still needs authenticated distribution, freshness limits and defined behavior when an edge location cannot obtain updates. A valid old record cannot carry news it has never received.

Nor does a trust record supply radio scheduling, network slicing, latency guarantees or service availability. Those remain properties of the telecom system and its implementation.

## Give each operator a decision it can own

Consider a maintenance service that needs to read diagnostics during a joint investigation. Operator A might accept Operator B's statement that the service has a maintenance role. A would still decide which local diagnostic resource is in scope, whether the request is permitted now and which service enforces that decision. Recognition can reduce ambiguity about the partner's claim without transferring control of A's infrastructure.

A useful integration specification would name the accepted issuer, permitted roles, target resources and responsible executor. It would also describe the difference between an unknown partner, an out-of-scope role and a relationship that has been revoked. These are design requirements for the illustrative telecom application, not a claim that Genesis Mesh supplies those telecom mappings.

The [recognition example](https://docs.genesismesh.org/examples/recognition-treaties.html) demonstrates a direct relationship between A and B. It does not make every organization B recognizes acceptable to A. If another contractor joins the maintenance chain, A needs an explicit basis for accepting its claims.

The [attestation-backed evaluation guide](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html) then helps separate a local decision from the service call. The integration should preserve the accepted claim and local policy basis with the operation it permits. That gives reviewers a concrete question to answer after a failure: which authority accepted the claim, and which component allowed the effect?

## Check it yourself

With a local checkout and the [documented installation prerequisites](https://docs.genesismesh.org/installation.html), run:

`python docs/examples/assets/scripts/recognition-treaty-demo.py`

The [local walkthrough](https://docs.genesismesh.org/examples/recognition-treaties.html) creates two authorities in a temporary directory; Docker, DNS and external services are unnecessary. Expect an accepted attestation before treaty revocation and a refusal afterwards. This documented example was not executed in this review.

Use those two outcomes as the beginning of an integration review. Identify which domain signs the relationship, which service enforces the operation, and how that service learns the relationship has ended.

## Further reading

- [Recognition-treaty walkthrough](https://docs.genesismesh.org/examples/recognition-treaties.html)
- [Attestation-backed evaluation](https://docs.genesismesh.org/examples/attestation-backed-evaluation.html)
- [SDK coverage overview](https://docs.genesismesh.org/sdk/index.html)
- [Website](https://genesismesh.org/)
- [Documentation](https://docs.genesismesh.org/sdk/index.html)
- [Public demo](https://mesh.genesismesh.org/)
- [GitHub source](https://github.com/GenesisMeshLabs/genesismesh)

The public demo is a trust-system interface, not a demonstration of this illustrative application.
