# Identity should survive a network move

An inventory agent starts on an engineer's laptop, moves to a warehouse edge machine, then runs in a cloud account. In this illustrative case, the operator wants the inventory service to recognize the same administrative domain after each move. A new address should not silently create a new trust relationship, and a familiar name should not excuse an unfamiliar key.

That problem motivates the proposed [Agent Identity URI Scheme](https://arxiv.org/abs/2601.14567), which separates naming from network location. Genesis Mesh does not claim to implement its `agent://` scheme. Its relevant mechanism is a more specific one: a sovereign domain publishes identity material that another operator can check against a cryptographic anchor.

## Start with the domain, not the address

In Genesis Mesh, a sovereign is an independently administered trust domain. Its Network Authority is the operator's online service for membership credentials and trust material. The [sovereign identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) distinguishes the domain's stable `sovereign_id` from its public `endpoint`. The endpoint helps another system find the service; it does not establish that the service deserves trust.

For the inventory operator, this means keeping two questions separate. Where can the authority be reached today? Which authority does the receiving service recognize? Updating a hostname can answer the first without answering the second. A successful connection to the new machine is useful operational evidence, but it is not proof that the machine represents the same domain.

The concrete documents are available through `GET /sovereign.json` and `GET /genesis`. The [public route implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) exposes the identity metadata and genesis block. The former includes the sovereign and network names, root public key, genesis Network Authority key, current signing-key information and advertised endpoint.

Those fields do not all carry the same authority. The identity document is unsigned. The [specification's verification requirements](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) tell consumers to compare the required trust fields with the root-signed genesis block: `sovereign_id`, `network_name`, `root_public_key` and `network_authority.public_key`. Descriptive metadata and the endpoint cannot replace that check.

## What the receiving operator actually trusts

The consumer needs a trusted root key obtained through its own onboarding or recognition process. Downloading a root key from the same untrusted endpoint being evaluated is not independent confirmation. In the warehouse example, the receiving inventory service should already know which domain it intends to recognize and retain the trust material needed to check that claim.

The [identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) also separates key roles. The root anchors the domain, the Network Authority signs operational trust material, operator keys authorize administrative work, and node keys identify individual participants. Keeping those roles separate makes the migration discussion precise: moving an application is not the same operation as replacing its domain root or rotating an authority's signing key.

The public identity route reports both the original authority key and current signing-key information. That distinction matters after a succession. The [route source](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) also advertises the key-history endpoint. A reader should follow the documented history verification rather than treating whichever key appears in a fresh response as trusted merely because it is newer.

Consider two migration outcomes. In the first, the endpoint changes while the required trust fields still match the verified genesis material. The operator can update reachability without inventing a new domain identity. In the second, the replacement server presents the old name with a different root. That is a trust change requiring review, even when the server answers correctly and the application appears healthy.

## Continuity still has operational limits

This mechanism establishes domain continuity; it does not transfer a running process, copy private keys safely or disable the old host. Those are migration responsibilities. The operator must decide how the new workload receives credentials, which old access paths are retired and how to recover if both instances remain active. No identity document answers those deployment questions on its own.

A node's credential also has its own lifecycle. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes certificate signatures, validity, network, revocation state and transport-key binding checks. A stable sovereign identifier does not make a stale or revoked node credential acceptable, and a valid node credential does not decide whether a particular inventory operation is allowed.

The receiving service remains the authority for its resource. It must consume the verified identity and apply its own access rules before returning inventory data. The reference peer packages are [internal and maintained for fixes without new features](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html); this article makes no claim of universal workload mobility across runtimes.

For the inventory rollout, a useful acceptance record would therefore identify the expected sovereign, the verified root, the new endpoint and the credential the new node presents. The receiving operator can review those items independently of the application's functional test. A successful stock lookup demonstrates that a request worked; it does not replace the trust checks that made the request acceptable.

## Check it yourself

Use a disposable authority you operate, an independently trusted copy of its root public key and the [documented identity verification procedure](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html). Fetch `/sovereign.json` and `/genesis`, verify the root signature and compare the four required trust fields.

Inspect an endpoint-only change separately from a root mismatch. The first should preserve the verified domain anchor. The second must trigger review rather than automatic acceptance of the familiar name. Keep private keys out of public test artifacts and record which root the consumer expected. This documented procedure was not executed in this review.

## Further reading

- [Sovereign identity and verification requirements](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html)
- [Membership and peer security](https://docs.genesismesh.org/concepts/security-model.html)
- [Scope of the internal peer packages](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html)

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/) | [Public demo](https://mesh.genesismesh.org/) | [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
