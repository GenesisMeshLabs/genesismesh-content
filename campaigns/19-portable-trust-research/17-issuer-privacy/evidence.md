# Evidence review: idea 17

Scope: Beta Merkle capability membership, exact exposed fields and unsalted hashes; no IRAC/issuer hiding, anonymity, ZK, freshness or anti-replay guarantee.

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

On 2026-11-05 the author reopened the IRAC paper abstract, selective-disclosure guide and pinned model/implementation pages. The actual model is narrower than guide marketing: agreement_id, issuer_sovereign_id, capability count and time are visible; the proof names the prover. Unsalted SHA-256 capability leaves do not supply strong hiding for guessable dictionaries. Independent reviewer confirmed unchanged core main and latest v1.9.1 release. The article does not assert issuer hiding, zero knowledge, general anonymity, fresh authorization or replay prevention from membership alone.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

A contractor needs to show a dataset service that it has permission to read a particular collection. The contractor would prefer not to reveal every capability in its agreement. It also wants to avoid exposing which organization issued its credentials. In this illustrative case, those are two different privacy requirements, and meeting one does not establish the other.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

The [IRAC research](https://arxiv.org/abs/2512.20234) examines issuer-hiding credentials: revealing the issuer can expose sensitive context about a holder even when the holder's own identity is hidden. Genesis Mesh does not claim to implement IRAC. Its selective-disclosure example provides a narrower starting point for examining what an actual capability proof reveals.

Evidence: https://arxiv.org/abs/2512.20234

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

The dataset service needs evidence about the requested capability, plus the trust and policy context required to accept it. Giving the service an entire agreement may expose unrelated capabilities. The [selective-disclosure walkthrough](https://docs.genesismesh.org/examples/selective-disclosure.html) demonstrates a Merkle commitment to a capability set, followed by a proof that one capability belongs to that set.

Evidence: https://docs.genesismesh.org/examples/selective-disclosure.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

A Merkle tree connects hashes of individual values to one root hash. The holder presents the selected capability and the hashes needed to reconstruct its path to that root. The verifier can check membership without receiving the complete list of capability strings. That reduces what must be sent in the interaction; it does not automatically conceal every fact about the agreement or its participants.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

The concrete Genesis Mesh artifacts are `CapabilityCommitment` and `CapabilityMembershipProof`. The [model definitions](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) are important here because a privacy review must inspect the serialized fields, not rely only on a diagram showing a hidden list.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C08

The commitment includes the Merkle root and capability count, but also the agreement identifier, issuer sovereign identifier and timestamp. The proof includes the revealed capability, leaf hash, path and prover identifier. These are visible metadata. Calling the output "selective disclosure" does not make the issuer anonymous or hide the existence of the underlying agreement.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) builds the commitment from the agreed capability set and signs it with the issuer's key. In the contractor example, the issuer is the party whose commitment the service is willing to accept. Selecting that issuer and its verification key is a trust decision made by the receiving operator.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

The holder keeps the agreement locally and constructs a proof for the requested capability. The service checks the commitment signature and the relationship between the revealed capability, its leaf hash, the proof path and the signed root. A changed capability cannot simply be substituted into an otherwise unchanged proof and treated as verified.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

The [selective-disclosure gate](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) also checks that the commitment's agreement identifier and revealed capability match the request context. This matters because a valid membership proof is about a particular committed set. It is not a universal credential for any agreement or any request that uses a similar-looking capability label.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C13

After verification, the dataset service still decides whether to execute the requested read. The resource, current relationship and operation parameters remain part of that decision. The proof does not contact every authority involved or establish that a previously acceptable permission remains current. A cryptographically valid membership result and a present authorization result answer different questions.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

For the contractor's first requirement, the mechanism can avoid transmitting the full capability list. For its second requirement, the visible `issuer_sovereign_id` directly defeats a claim that the issuer is hidden. The agreement and prover identifiers can also help a recipient correlate presentations. The [serialized model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py) makes those boundaries inspectable.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

There is a further limit in the leaf construction. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py) hashes capability strings without a salt. When possible capability names come from a small, predictable dictionary, an observer can hash candidate names and compare them with exposed hashes. The exact inference depends on the tree and visible path, but an unsalted hash is not a strong secrecy promise for a guessable value.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C17

The right claim is therefore selective transmission of capability information, with visible metadata and possible inference. This is not formal zero-knowledge proof, issuer-hiding authentication or general anonymity. A membership proof alone also does not provide freshness or replay prevention. The relevant disclosure commands and public functions are classified as [beta](https://docs.genesismesh.org/reference/public-contract.html).

Evidence: https://docs.genesismesh.org/reference/public-contract.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

For an operator designing a privacy-sensitive service, the practical exercise is to write down what each recipient can see. Include identifiers, counts, timestamps, repeated presentations and the recipient's existing knowledge. If concealing the issuing organization is essential, this implementation does not satisfy that requirement merely because it omits the other capability strings.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C20

Use a disposable [development installation](https://docs.genesismesh.org/installation.html), the example agreement and synthetic issuer/prover keys. Follow the local walkthrough:

Evidence: https://docs.genesismesh.org/installation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C21

```text
python docs/examples/assets/scripts/selective-disclosure-demo.py --no-gif
```

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Documented procedure, not executed.

### C22

Inspect both `commitment.json` and `proof.json` before evaluating the privacy claim. The documented valid proof should verify; changing the revealed capability without changing its matching leaf produces `leaf_hash_mismatch`. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py) provide source coverage for verification failures. Compare visible identifiers with the information your service actually needs. Neither the example nor tests were executed in this review.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2512.20234
- https://docs.genesismesh.org/examples/selective-disclosure.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/selective_disclosure.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/selective_disclosure.py
- https://docs.genesismesh.org/reference/public-contract.html
- https://docs.genesismesh.org/installation.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_selective_disclosure.py
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
