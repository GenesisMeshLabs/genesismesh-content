# Evidence review: idea 16

Scope: Reference peer identity and current-use vouching horizon; no prompt-injection benchmark, universal agent protocol support or automatic authorization.

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

On 2026-11-05 the author reopened the primary identity-credentials research abstract, security model, dormant-packages decision and installation guide. Retained pinned RuntimePeerIdentity code was re-inspected for certificate parsing, network/time/CRL checks, NA verification with a current-time argument, Noise key binding and roles derived from the certificate. The pinned vouching-horizon test link was reopened. Independent reviewer confirmed unchanged core main and latest v1.9.1 release. No claim of a DID/VC implementation or semantic/model safety is made.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

An assistant requests an internal dataset and introduces itself as the trusted finance agent. It uses the right project name, explains the urgency and claims that an administrator approved the request. In this illustrative case, the receiving service needs a way to establish identity that does not depend on how convincing the conversation sounds.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

Research on [AI agents with decentralized identifiers and verifiable credentials](https://arxiv.org/abs/2511.02841) explores this problem and reports limitations when a language model alone controls security procedures. That does not establish a Genesis Mesh DID or credential integration. The relevant reference mechanism here is certificate validation performed by runtime code, with the resource owner's authorization decision kept separate.

Evidence: https://arxiv.org/abs/2511.02841

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

Genesis Mesh organizes trust around independently administered sovereign domains. A Network Authority is the operator's service for admitting members and issuing signed trust material. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes admission using a valid invite token and a request signature proving possession of the node's key. Roles come from the invite policy rather than the caller's self-description.

Evidence: https://docs.genesismesh.org/concepts/security-model.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

The resulting join certificate binds the node's public key to the network and assigned roles. For the dataset service, this changes the evidence available at the connection boundary. The assistant may say "finance," but the receiving runtime has a signed artifact to inspect. The service does not have to treat the text of the conversation as an administrative instruction.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

A certificate is still a claim made by a particular authority. The consumer needs the intended network's trust material and must verify the authority's signature. It also needs to distinguish a signed artifact from an artifact it is willing to use now. The [security model](https://docs.genesismesh.org/concepts/security-model.html) lists both validity and revocation checks alongside signature verification.

Evidence: https://docs.genesismesh.org/concepts/security-model.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C09

The inspected [peer identity implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py) parses the certificate and checks its network name, validity window and known revocation state. It verifies the authority signature using the node's trust machinery. Failure raises an error rather than returning an authenticated peer.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

It then checks whether the certificate's Ed25519 public key corresponds to the Noise static key used by the connection. This binding matters because merely copying someone else's public certificate into a message should not establish possession of that identity's key. The certificate and the cryptographic connection must refer to the same node.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

The same [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py) handles peer announcements. It verifies the announcement against the certificate and returns roles from that certificate. It does not return a privileged role merely because the announcement or conversational payload requests one. The receiving application should use that validated result, not reinterpret a persuasive role claim as equivalent evidence.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

In the dataset scenario, a request with the wrong network certificate, a known revoked certificate or a mismatched connection key should not become an authenticated finance peer. An agent can still send prose explaining why the check should be waived; that prose does not satisfy the inspected validation function's inputs.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C14

Key succession creates a subtler case. A certificate may have been signed correctly by the authority key valid at issuance. That historical fact can remain relevant to an audit even after the runtime stops accepting it for a new session.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

The [vouching-horizon tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_node_vouching_horizon.py) examine that distinction: historical verification can succeed while current validation refuses a credential whose signing key no longer vouches for it now. The peer validator supplies the present time to the authority verification path rather than asking only whether the signature was once valid.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_node_vouching_horizon.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

For the operator, the response is a credential-lifecycle decision. A participant may need a certificate backed by the current authority key. Treating every old signature as permanent admission would erase the difference between a historical record and a live identity. Conversely, refusing a live session does not require pretending that an authentic old record never existed.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

A correctly authenticated node may request an operation outside its role or relationship. The receiving service must decide whether this identity may read this dataset with these parameters, then enforce that decision at the execution boundary. The [security model](https://docs.genesismesh.org/concepts/security-model.html) describes membership checks; it does not turn membership into unrestricted access.

Evidence: https://docs.genesismesh.org/concepts/security-model.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C19

There are also limits to what this validation can observe. A stolen, still-accepted private key can let an attacker authenticate as its holder. A verifier cannot apply a revocation it has not learned. A model that has a separate path to dataset credentials can bypass an identity-aware application entirely. These are reasons to review key custody, freshness and execution paths alongside the certificate checks.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C20

This article concerns the reference peer runtime. Its packages are [internal and maintained for fixes without new features](https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html). It is not a claim that every agent framework invokes this validator, or that authenticated agents reason correctly, resist prompt injection or produce safe answers.

Evidence: https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C22

Use a disposable source checkout and the dependencies in the [development installation guide](https://docs.genesismesh.org/installation.html). The source-based reader check is:

Evidence: https://docs.genesismesh.org/installation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C23

```text
python -m pytest genesis_mesh/tests/test_node_vouching_horizon.py -v
```

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Documented procedure, not executed.

### C24

Read the test setup before running it. The expected distinction is current refusal beyond the authority's vouching horizon, acceptance of the appropriate current credential, and historical verification of previously signed material. Compare that with the network, revocation and key-binding branches in the [peer validator](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py). These tests were inspected, not executed in this review.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2511.02841
- https://docs.genesismesh.org/concepts/security-model.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/node/peer_identity.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_node_vouching_horizon.py
- https://docs.genesismesh.org/development/decisions/0007-dormant-packages.html
- https://docs.genesismesh.org/installation.html
- https://docs.genesismesh.org/operations/revocation.html
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
