# Federation without surrendering local control

**Portable Trust · Part 3 of 6**

*Accepting a partner's membership claims should leave the receiving operator's own authority intact.*

Consider an illustrative collaboration: a research organization wants to admit collaborators from a partner institution. The partner can identify its researchers. The receiving organization still decides which projects those researchers may access, and whether any of them may administer a workspace.

Genesis Mesh makes that relationship explicit through signed recognition. Each sovereign operates a Network Authority, the service that holds its signing keys and issues its trust records. Recognition lets one authority accept specified claims from another without giving the other its keys or control over local policy.

## What the treaty contributes

The [recognition-treaty walkthrough](https://docs.genesismesh.org/examples/recognition-treaties.html) documents a direct, scoped and revocable recognition relationship. A treaty is a signed statement about the foreign authority and the roles accepted across that boundary, with validity limits. It is something a verifier can inspect, rather than an informal agreement to trust everything a partner sends.

Consider a researcher whose membership is valid at Organization A. Organization B still needs an applicable recognition relationship and an accepted role before treating that membership as trusted. The application at B must then apply the permission for the particular workspace and action. Membership, recognition and local permission can change independently.

This also gives withdrawal more than one meaning. A can revoke its member's attestation. B can withdraw its recognition of A. B can narrow what a recognized researcher may do without changing either membership or recognition. An integration that tests only admission misses these separate controls.

The [cross-sovereign revocation walkthrough](https://docs.genesismesh.org/examples/cross-sovereign-revocation.html) distinguishes recognition from the foreign membership-revocation feed. A valid treaty does not make a revoked foreign membership valid. Receiving the relevant signed feed is part of learning that change. No claim of immediate global propagation follows from the existence of the signature.

## What the verifier checks

The [treaty implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/treaty.py) checks the expected issuer and subject, local revocation, status, validity and signatures. It turns the treaty's subject public keys, allowed roles and accepted statuses into a recognition policy. These fields make the scope operational: the receiving verifier is not merely matching the partner's display name.

The signed revocation-feed verifier also rejects a sequence at or below the minimum sequence supplied to it. That makes the caller's retained sequence state important. A fresh download of an old signed feed is still old information. The operator must preserve and use the relevant freshness and sequence state rather than assuming the signature alone prevents rollback.

The [recognition example](https://docs.genesismesh.org/examples/recognition-treaties.html) is direct rather than transitive. If B recognizes C, A does not thereby accept C under its treaty with B. An integration must identify the actual issuer, the applicable signed relationship and the receiver's own acceptance scope. This keeps a partnership from silently becoming permission for every organization connected to the partner.

For our researchers, capture the membership attestation and recognition treaty as separate inputs. A local workspace role belongs to a third decision. When a request is refused, those records help distinguish an expired membership, an ended recognition relationship and a local project restriction. The application must still authenticate the requester and enforce the operation at the point where it can access the workspace. This is the proposed integration boundary, not a built-in research-workspace adapter.

## What has actually been demonstrated

The [independent-sovereigns walkthrough](https://docs.genesismesh.org/examples/independent-sovereigns.html) documents a maintainer-operated two-cloud proof. Separate authorities use separate keys and infrastructure. That is evidence for the mechanism and for that recorded configuration, not an independent production deployment or a current live measurement.

The [project vision](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/VISION.md) distinguishes this from a separate external operator establishing its own sovereign and a real recognition relationship. Independent key material and independent organizational ownership are different claims. The former can be demonstrated by one team; the latter needs another operator.

## A useful comparison, with a clear limit

[Federating Trust Perimeters](https://arxiv.org/abs/2609.06595) examines cross-organizational machine trust with proposed extensions around SPIRE, including token exchange, remote attestation and distributed-ledger governance. It raises a related question about cooperation between domains. Genesis Mesh should not be described as implementing that paper's architecture, ledger or SPIRE extensions.

A useful next operator proof would choose one real shared permission, then exercise each withdrawal separately: foreign membership revocation, local recognition withdrawal and local permission reduction. Capture the signed inputs, the receiver's last refresh, the result and the application's response. Include a disconnected receiver so the evidence shows the actual freshness limit.

The [Connect vision](https://claude.ai/artifact/ParjPaubYJkVdkWcaCx4pt) proposes a concrete next proof: a user asks a genuinely independent owner to permit one document read, approved for the exact document, version, action and expiry, with verifiable evidence. It explicitly leaves cross-owner phone approval and production federation unbuilt or unproven. That everyday experience is Connect's role; Genesis Mesh provides trust mechanisms underneath. A recorded two-cloud treaty demonstration does not complete that product proof.

## Check it yourself

Follow the linked recognition-treaty walkthrough using its documented local setup and separately held authority keys. Inspect the issuer, subject, accepted roles and validity before verifying the treaty. Repeat with the walkthrough's negative/tampering case, then trace the foreign membership-revocation feed separately. Compare these artifacts with the historical independent-sovereigns example rather than assuming its recorded output describes the current hosted service.

This is a documented example, not executed in this review. The expected distinction is a verified applicable treaty versus a rejected invalid treaty; a valid treaty must not erase a member's revocation or supply application permission on its own.

## Further reading

- [Recognition treaties](https://docs.genesismesh.org/examples/recognition-treaties.html): direct scope, accepted roles and local withdrawal.
- [Cross-sovereign revocation](https://docs.genesismesh.org/examples/cross-sovereign-revocation.html): importing an issuer's withdrawal without ending the whole relationship.
- [Independent-sovereigns proof](https://docs.genesismesh.org/examples/independent-sovereigns.html): the recorded two-cloud demonstration and its limits.

Explore the [website](https://genesismesh.org/), [documentation](https://docs.genesismesh.org/), [public trust console](https://mesh.genesismesh.org/) and [source repository](https://github.com/GenesisMeshLabs/genesismesh). Start by naming one real partner claim and the local action it may support.
