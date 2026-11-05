# November 5 editorial revision: Federation without surrendering local control

The user requested articles around 900 words, canonical documentation links throughout, and a final Further reading section. This reviewed revision was subsequently saved to the existing Patreon post and verified as recorded below. Source-based review only: no product tests, demonstrations or live actions were executed.

## Current verification and changed claims

Current source/release refresh confirms core main a54b2d81f205c9b0203158f846f7ad44dc677063 and published v1.9.1 unchanged. The existing treaty implementation/feed verification claims retain their inspected source basis. The recognition walkthrough explicitly states scoped direct recognition, not transitive trust. Cross-sovereign revocation documentation shows imported attestation revocation while the treaty remains active, including rejection of stale sequences. The independent-sovereigns page explicitly labels its captured run as a replayed historical transcript; no current deployment or independent organizational ownership is inferred. New research-workspace handling is clearly an illustrative integration, with authentication and final permission retained by the receiver.

Canonical pages were reopened on November 5. No new treaty, attestation or application operation was executed. Patreon synchronization is verified below.

The user-supplied [Connect vision](https://claude.ai/artifact/ParjPaubYJkVdkWcaCx4pt) was read in its rendered public iframe on November 5. It separates Connect as the everyday app from Genesis Mesh as the trust layer, preserves independent owner control, and labels the cross-owner document read with exact phone approval as a proposed first proof. Phone-approval screens, production federation between separate operators and a second independent implementation are not asserted as shipped or proven by these articles. This is product-vision context, not implementation evidence.

Canonical documentation pages opened and checked on 2026-11-05:

- [Recognition treaties](https://docs.genesismesh.org/examples/recognition-treaties.html)
- [Cross-sovereign revocation](https://docs.genesismesh.org/examples/cross-sovereign-revocation.html)
- [Independent-sovereigns proof](https://docs.genesismesh.org/examples/independent-sovereigns.html)

## Exact revised article

The following text binds this claim review to the wording submitted for independent review. It retains the historical evidence inventory below.

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


## Prior source inventory (reviewed November 4)

# Evidence review: Federation without surrendering local control

Reviewed: 2026-11-04. Original campaign idea: 12. Evidence level: current documentation and source inspection, compared with the article’s pinned implementation snapshots. No product tests, examples, live actions or hardware exercises were run for this review.

## Recognition and local permission

A treaty scopes accepted foreign claims. It does not supply the receiving application’s permission for every action or override a foreign membership revocation.

Sources: [source 1](https://docs.genesismesh.org/examples/recognition-treaties.html), [source 2](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/treaty.py).

## Freshness and withdrawal

Treaty verification checks issuer/subject, status, validity, signatures and local revocation. Feed sequencing depends on the caller supplying retained minimum sequence state; a signature alone does not prevent replay of old information.

Sources: [source 1](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/treaty.py).

## Deployment evidence

The two-cloud proof is a documented maintainer-operated historical demonstration. It is not proof of a current live run or independently owned external operators.

Sources: [source 1](https://docs.genesismesh.org/examples/independent-sovereigns.html), [source 2](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/VISION.md).

## Research scope

Federating Trust Perimeters proposes SPIRE-related extensions, including remote attestation, token exchange and ledger governance. The article explicitly declines to claim Genesis Mesh implements that architecture.

Sources: [source 1](https://arxiv.org/abs/2609.06595).

## Release scope and limitations

Current source and release check: 2026-11-04. The core, TypeScript, Go, Rust, .NET and gateway repositories each have a non-draft, non-prerelease GitHub v1.9.1 release. This establishes published source/release artifacts, not the version running at a particular deployment. The current [SDK capability matrix](https://docs.genesismesh.org/sdk/index.html) places TypeScript, Rust and .NET in the governed-client tier; Go remains a verifier plus thin client. Shared version numbers do not imply identical features. No Python standalone-client, PHP parity or universal SDK coverage is inferred.

Some older scope paragraphs in the [grant runbook](https://docs.genesismesh.org/operations/grants.html) and [governed-changes concept](https://docs.genesismesh.org/concepts/governed-changes.html) still describe .NET as lacking governed-client features. For current availability, use the SDK matrix and [.NET 1.9.0 release](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.0). Those paragraphs do not override the newer implementation and release evidence.

The [Rust 1.9.1 security advisory](https://github.com/GenesisMeshLabs/sdk-rust/security/advisories/GHSA-cwf5-mqxw-75hq) fixes direct verification of certain records with missing own timestamps under NA key history. The edge agent and standalone `genesis-mesh-verify` are explicitly unaffected. The analogous [TypeScript fix](https://github.com/GenesisMeshLabs/sdk-typescript/security/advisories/GHSA-rx24-98gh-f8mc) shipped in 1.9.0. Historical pinned source links are evidence snapshots, not installation recommendations.

No material correction identified. Relevant treaty implementation and proof documentation are unchanged at current core. The proposed withdrawal tests remain proposals, not reported results.

## Inspected source revisions

| Repository | Current inspected head | Official release |
|---|---|---|
| genesismesh | `a54b2d81f205c9b0203158f846f7ad44dc677063` | [v1.9.1](https://github.com/GenesisMeshLabs/genesismesh/releases/tag/v1.9.1) |
| sdk-typescript | `8154ca7ac459ffbcd22d35900ca72f8093165bfc` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-typescript/releases/tag/v1.9.1) |
| sdk-go | `ade949888eacd0ccc16126941427e1211f82aec8` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-go/releases/tag/v1.9.1) |
| sdk-rust | `b67c248717d5d99aca6f4dad320692f3f6c07c69` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-rust/releases/tag/v1.9.1) |
| sdk-dotnet | `241d99b7508b378ce7c613dfc0baeed7cc5df56c` | [v1.9.1](https://github.com/GenesisMeshLabs/sdk-dotnet/releases/tag/v1.9.1) |
| gateway | `2e6486ee6a6481adca1be3b9dae70a4ef32036f9` | [v1.9.1](https://github.com/GenesisMeshLabs/gateway/releases/tag/v1.9.1) |

## Patreon synchronization

Verified 2026-11-05: the approved revision was saved to the existing [Patreon post](https://www.patreon.com/GenesisMeshLabs/posts/federation-local-174297216) and reopened. Its rendered body and all 15 links matched the approved source; the cover and public access were preserved. The existing public schedule remains 2026-11-06T09:00:00+01:00 (Europe/Stockholm). LinkedIn remains an unpublished draft.

Approved Markdown SHA-256: `00e3fbc8a300201b8ae7c8c6d99f969b1de02619c11ced5316950c3895e41976`. Rendered-body SHA-256 after collapsing whitespace: `2324389066c74af9fd7af5171cfd6464f57b92568cf4529fc815b0f92d73ee8b`. This is verification of the saved publication copy, not execution of a product example or proof that a scheduled post has been released.
