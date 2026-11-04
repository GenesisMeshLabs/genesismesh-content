# Who trusts whom in a 6G network?

An illustrative network operator receives a request from another company's edge service. Encryption protects the connection, but which partner claims should the operator accept, and what may that service do?

[Beyond Certificates](https://arxiv.org/abs/2310.19366) investigates cross-domain access control using a **5G prototype** to explore a future 6G problem; neither that paper nor this scenario establishes a deployed Genesis Mesh 6G integration.

## Let the accepting domain define recognition

In Genesis Mesh's [recognition walkthrough](https://docs.genesismesh.org/examples/recognition-treaties.html), each sovereign domain controls its keys and Network Authority, the service issuing and evaluating its trust records.

Sovereign B issues a `MembershipAttestation`. Sovereign A signs a `RecognitionTreaty` naming B, accepted keys and permitted roles. A verifies B's attestation through that treaty. The accepting domain signs the relationship; B cannot expand A's acceptance merely by asserting trustworthiness.

The [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/treaty.py#L95) checks treaty status, validity, signature and subject, then applies its role scope to the attestation. An empty role scope grants nothing. In our scenario, A could recognize a partner's maintenance role without granting permission to change routing.

Recognition still needs an execution boundary. The receiving application must authenticate the requester, map accepted claims into local authorization and enforce the exact service operation. A foreign attestation does not automatically become a local authorization decision; telecom adapters remain integration work.

Revocation is concrete but local: the walkthrough accepts an attestation, revokes the treaty, then returns `treaty_locally_revoked`. A disconnected verifier cannot learn new revocations instantly. Operators still need authenticated updates and freshness limits. The trust record supplies no radio, latency or service-availability guarantee.

## Check it yourself

With a local checkout and [installed dependencies](https://docs.genesismesh.org/installation.html), run the documented example:

`python docs/examples/assets/scripts/recognition-treaty-demo.py`

It creates two local authorities; no external services are required. Expect acceptance before treaty revocation and refusal afterwards. This documented example was not executed in this review.

Name who signs the recognition relationship, who enforces the operation and how that service learns the relationship has ended.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/sdk/index.html) · [Trust UI demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh). The public demo does not demonstrate this illustrative application.
