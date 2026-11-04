# Identity should survive a network move

An inventory agent moves from a laptop to an edge machine, then to the cloud. In this illustrative case, its operator wants a new address without silently creating a new trust relationship.

The proposed [Agent Identity URI Scheme](https://arxiv.org/abs/2601.14567) studies this separation; Genesis Mesh does not claim to implement its `agent://` scheme.

## Keep the trust anchor separate

In Genesis Mesh, a sovereign is an independently administered trust domain. Its Network Authority is the operator's service for membership credentials and trust material. The [identity specification](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) gives the domain a stable `sovereign_id`; its `endpoint` is only a reachability hint.

The important artifact is the root-signed genesis block. A consumer starts with a trusted root key, verifies genesis, and compares the required trust fields returned by `GET /sovereign.json` with it. That identity document is unsigned: its descriptive fields cannot replace the cryptographic anchor. The [public route](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/public.py) exposes both documents.

An address change therefore need not change the domain's identity. A root-key mismatch is different: it requires operator review, not silent acceptance because the name or URL looks familiar. The receiving system still decides whether a verified identity may access its resources.

This is domain continuity, not automatic workload or private-key migration. The operator must secure key provisioning and retire old access paths. A node key and certificate are separate from the sovereign's root; the reference peer packages remain [internal, maintained for fixes without new features](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html).

## Check it yourself

Use an authority you operate, its independently trusted root key and the [documented identity procedure](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html). Fetch `/sovereign.json` and `/genesis`, verify genesis and compare the required trust fields.

An endpoint-only change should preserve the anchor. A changed root must trigger review, even if `sovereign_id` is unchanged. This documented procedure was not executed in this review.

[Website](https://genesismesh.org/) | [Documentation](https://docs.genesismesh.org/rfcs/rfc-001-sovereign-identity.html) | [Public console](https://mesh.genesismesh.org/) | [Source](https://github.com/GenesisMeshLabs/genesismesh)
