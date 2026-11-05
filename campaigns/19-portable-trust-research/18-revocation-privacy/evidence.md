# Evidence review: idea 18

Scope: NA certificate CRL data, published revocation and local-state limits; no CRSet integration, private query or issuer-activity privacy.

## Evidence snapshot and release status

Review date: 2026-11-04. Core source inspected at a54b2d81f205c9b0203158f846f7ad44dc677063. GitHub v1.9.1 is published; the independent reviewer resolved its annotated tag to this exact commit and confirmed PyPI genesis-mesh 1.9.1 publication. Source version, published package and live deployment are different observations. No package, binary, test, script or demo was executed during this article review.

The independently checked release/train metadata is in ../source-release-snapshot.json and ../source-review.md. The older standard's dated 1.8.1 matrix is historical, not the availability matrix used here.

## Surface inventory

| Surface | Current snapshot / availability | Relevance and boundary |
| --- | --- | --- |
| NA and Python reference / CLI | Core a54b2d81f205c9b0203158f846f7ad44dc677063; v1.9.1 GitHub/PyPI verified | The concrete reference flows and tests cited below. Source inspection, not live execution. |
| TypeScript SDK | 8154ca7ac459ffbcd22d35900ca72f8093165bfc; v1.9.1 GitHub/npm verified | A governed client per current SDK matrix. No TypeScript parity or operation-specific behavior is asserted in this article. |
| Rust SDK | b67c248717d5d99aca6f4dad320692f3f6c07c69; v1.9.1 GitHub assets/Git dependency, beta | No transfer of Python/example behavior to Rust is claimed. Not on crates.io. |
| .NET SDK | 241d99b7508b378ce7c613dfc0baeed7cc5df56c; v1.9.1 GitHub/NuGet verified | Governed client since 1.9.0 per current matrix. Old guide prose saying only TypeScript/Rust is stale; no parity assertion here. |
| Go SDK | ade949888eacd0ccc16126941427e1211f82aec8; v1.9.1 GitHub tag verified | Thin client/offline verifier per matrix; no governed-client parity claim. |
| Gateway | 2e6486ee6a6481adca1be3b9dae70a4ef32036f9; v1.9.1 GitHub binaries, beta | Separate implementation; not the Python peer runtime or NA decision service. No gateway behavior inferred here. |
| Edge | Rust repo v1.9.1 release assets, beta | Only relevant where propagation comparison mentions documented next-sync timing. No uniform fallback, clock, or revocation behavior claimed across clients. |
| PHP | Independent reviewer found source 0.56.0, no release/tag, Packagist 404 | Not a claimed released surface or demonstrated flow in this article. |
| Demos / conformance | Source procedures and tests; not executed | Test source means test-covered, not passed here. No performance, interoperability or hosted security result asserted. |

Current matrix: https://docs.genesismesh.org/sdk/index.html and pinned source https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/docs/sdk/index.md. Registry observations were made by the independent source reviewer and are recorded in the common review, not inferred from matching version strings.

## Public access and examples

Canonical documentation pages were reached through the live documentation navigation, opened and compared with their relevant source content on 2026-11-04. Whole-page links are used; no guessed anchors. Root anonymously inspected https://genesismesh.org/ and https://mesh.genesismesh.org/. The website displayed 1.8.1, the console displayed 1.9.0 and Operational/Ready, while the source releases are 1.9.1. These are page-availability observations only. No article claims a hosted scenario succeeded. These anonymous page observations were recorded by the publication reviewer on 2026-11-04.

Reader procedures require a disposable source checkout and the development dependencies in the installation guide. Source-based test commands select actual inspected test files. Local demo commands are copied from the linked documentation. All are explicitly marked not executed. Failure outcomes are documented or asserted in inspected test source; they are not new runtime results.

## Expanded revision verification - 2026-11-05

On 2026-11-05 the author reopened CRSet's primary abstract, the revocation runbook, security model and pinned CRL model. The retained CRL route/test sources were re-inspected: revocation adds an entry and blocks heartbeat/renewal; quiet/expired CRL refresh increases the sequence with unchanged revocation entries. Independent reviewer confirmed unchanged core main and latest v1.9.1 release. Privacy consequences are identified as metadata inferences, not measurements. CRSet and private non-revocation proofs are research context, not claimed Genesis Mesh features.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

A contractor leaves a project, and the operator revokes its access certificate. That is the right security action. But suppose an outside observer watches the organization's revocation data over time. Even without a person's name, changing identifiers, reasons and timestamps may reveal patterns of activity. This illustrative case asks two questions: will the revoked credential be refused, and what does publishing that refusal reveal?

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

[CRSet research](https://arxiv.org/abs/2501.17089) studies private, non-interactive credential revocation, including the risk that revocation activity exposes information about an issuer. Genesis Mesh does not claim to implement CRSet. Its signed certificate revocation list provides a concrete way to examine the difference between authentic revocation information and private revocation information.

Evidence: https://arxiv.org/abs/2501.17089

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

A Genesis Mesh Network Authority is the operator's service for membership credentials and trust material. The [revocation runbook](https://docs.genesismesh.org/operations/revocation.html) describes an operator-authenticated `POST /admin/revoke` request. It requires a privileged operator key; possession of the certificate being revoked is not administrative authority to change the domain's revocation state.

Evidence: https://docs.genesismesh.org/operations/revocation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

The operator identifies the certificate and gives a reason. The authority marks the certificate revoked, produces a new certificate revocation list, increments its sequence and signs it. The active list is available through `GET /crl`. The [route implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/crl.py) serializes the active signed CRL for readers.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/crl.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

The authority then refuses heartbeat and renewal requests using the revoked certificate. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) exercise both refusal paths and check that the certificate identifier appears in the CRL. This is an inspectable local consequence of the operator's decision, not merely a note in an incident document.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C08

Other participants need the relevant state before they can enforce that withdrawal. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes peer certificate checks against known revocation state. A participant using an older copy cannot learn a new withdrawal from a signature alone. Authenticity and freshness are different properties of the information it has.

Evidence: https://docs.genesismesh.org/concepts/security-model.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

The [CRL model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) exposes the list identifier, sequence, issue time, next-update time and issuer. Each revoked-certificate entry contains a certificate identifier, revocation time, reason and issuer. The authority's signature lets a consumer check the signed content. It does not encrypt those fields.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

For the departing contractor, the certificate identifier need not contain a human-readable name to be linkable. A recipient may already have seen that identifier during a previous interaction. Matching the later CRL entry to that earlier observation can reveal that the same credential was withdrawn. This is an inference from visible metadata, not a claim that every observer can identify every holder.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

The reason field can add context. The [runbook](https://docs.genesismesh.org/operations/revocation.html) distinguishes reasons such as key compromise and cessation of operation. Operators should select an accurate reason because these choices have operational meaning; the privacy question is what recipients can infer from the reason and its timing. Replacing a meaningful reason with an inaccurate one is not a sound privacy mechanism.

Evidence: https://docs.genesismesh.org/operations/revocation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C13

Counting sequence changes also needs care. The [refresh test](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py) shows a quiet authority republishing an expiring CRL with a higher sequence and unchanged revocation entries. A new sequence therefore does not necessarily mean another certificate was revoked. Comparing the actual entries supports a more precise observation than treating every refresh as new organizational activity.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

Downloading a signed list can support local verification of the information already obtained. It does not erase the contents of that list, prevent recipients from retaining earlier copies or hide information that an observer can correlate with another source. The [CRL representation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py) remains explicit about the revoked entries.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

That makes the operator's privacy review different from the signature review. A valid signature answers who signed these bytes and whether they were altered. It does not answer whether the bytes reveal more than the recipient needs. Likewise, an accurate timestamp can be useful for investigation while also contributing to an activity pattern.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C17

The receiving service still owns its admission and resource decisions. It should verify the relevant trust material, apply the state it knows and avoid presenting an old copy as evidence of fresh permission. A disconnected verifier cannot promise immediate knowledge of a new revocation. These operational limits remain even if the certificate identifier looks opaque.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

CRSet addresses a separate design objective around issuer activity. Its research results should prompt explicit requirements, not an assumption that a signed Genesis Mesh CRL has the same privacy properties. If a deployment requires private non-revocation proofs or concealed revocation activity, that requirement remains unmet by the inspected CRL mechanism.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C19

For the contractor's operator, a practical review would keep the authorized withdrawal, the resulting signed list and the observed refusal together. It would also inventory who can retrieve or retain that list. This separates evidence that access was withdrawn from the broader privacy question of what outsiders learn. Both deserve review, and neither should be inferred from the other.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C21

Use a disposable [development installation](https://docs.genesismesh.org/installation.html) with synthetic identities. Read and run the source-based CRL checks:

Evidence: https://docs.genesismesh.org/installation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C22

```text
python -m pytest genesis_mesh/tests/test_na_crl.py -v
```

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Documented procedure, not executed.

### C23

Inspect the CRL before and after the fixture revokes a certificate. Expected results include the new entry and refused heartbeat and renewal. Then inspect the quiet-refresh test: its sequence increases while the entries remain equal. Compare what a verifier needs with every field a recipient can see. These tests were inspected, not executed in this review.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2501.17089
- https://docs.genesismesh.org/operations/revocation.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/na_service/routes/crl.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_na_crl.py
- https://docs.genesismesh.org/concepts/security-model.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/revocation.py
- https://docs.genesismesh.org/installation.html
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
