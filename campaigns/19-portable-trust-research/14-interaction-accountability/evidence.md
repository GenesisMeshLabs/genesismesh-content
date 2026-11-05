# Evidence review: idea 14

Scope: Reference execution evidence, sequence/digest/signature verification and valid-prefix limitation; beta CLI, no completeness or execution guarantee.

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

On 2026-11-05 the execution-chain walkthrough, governed-changes guide, installation guide and public contract were reopened. The author re-inspected retained pinned execution models and verifier source, including optional expected-capability and decision/freshness parameters and the absence of an expected final count. The independent reviewer confirmed unchanged core main a54b2d81f205c9b0203158f846f7ad44dc677063 and latest release v1.9.1. BlockA2A's abstract was reopened. The article does not repeat the documentation's overbroad deletion-detection claim: an intact prefix can verify.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

An invoice assistant asks another organization's service to retrieve three account records. The request is approved, but the last lookup returns only a partial result. Later, someone reviewing the workflow sees a chat message saying "done." In this illustrative case, that message is too weak to answer who authorized the work, which service performed it and what the service reported.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

The [BlockA2A research](https://arxiv.org/abs/2508.01332) studies verifiable agent interactions and accountability. Its architecture and evaluation are not Genesis Mesh guarantees. The relevant Genesis Mesh mechanism is a signed execution record linked to a decision, with successive records connected so a verifier can inspect their order and integrity.

Evidence: https://arxiv.org/abs/2508.01332

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

Genesis Mesh is a portable trust layer for independently operated systems. Its Network Authority is the operator's service for trust decisions and signed control material. A resource-owning service remains responsible for applying an allowed decision and performing the requested action. The [governed changes guide](https://docs.genesismesh.org/concepts/governed-changes.html) makes a useful distinction: the authority signs a decision, while an executor signs the record of what it did.

Evidence: https://docs.genesismesh.org/concepts/governed-changes.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

For the invoice workflow, a signed `BoundaryDecision` records the authorization outcome. That does not mean the account lookup happened. The service may fail before execution, return incomplete data or encounter a downstream error. An audit needs the decision and the later execution report, because they answer different questions.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

The [execution-chain walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html) starts with an agreement and an allowed decision, then records three executions under that decision. The service signs each `ExecutionEvidence` record. The example deliberately gives the third record a partial outcome, making the difference between permission and completion visible.

Evidence: https://docs.genesismesh.org/examples/execution-evidence-chain.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C08

The [record model](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/execution.py) carries decision, context and agreement identifiers; the executor's sovereign identity; executed capability and parameters; execution time; outcome; sequence number; and the previous evidence digest. These fields let a reviewer inspect a concrete report rather than infer execution from the assistant's description of its intentions.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/execution.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

Each later record includes `prev_evidence_digest`, the digest of the preceding record's canonical body. The executor signs that link as part of the new record. The [implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) therefore gives the verifier something stronger than three independent messages: an ordered sequence whose links can be checked.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

The verifier receives the evidence chain and a mapping from executor identities to trusted public keys. Those keys are an input chosen by the verifying party; a record does not make its own signer trustworthy merely by naming an identity. If the caller supplies an expected capability, the verifier checks that each record names it.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

The [verification routine](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) checks sequences starting at one, digest links and executor signatures. It rejects missing signatures, invalid keys, capability mismatches when that check is requested, and broken links. When a decision with an embedded freshness proof is supplied, it also rejects a reported execution time beyond that proof's validity window. That last check is conditional; callers should not assume it ran without supplying the relevant decision.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C13

In the invoice example, changing the order from records one-two-three to one-three-two produces a gap at the second supplied record. The [walkthrough](https://docs.genesismesh.org/examples/execution-evidence-chain.html) shows the refusal as `sequence_gap`. A reviewer can identify the failed position instead of accepting an undifferentiated "audit complete" result.

Evidence: https://docs.genesismesh.org/examples/execution-evidence-chain.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

The important limit is at the end. The inspected [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py) has no required final record count or independently expected head digest. A valid prefix can therefore verify even if a later record was omitted. Removing a middle record is different from withholding the tail.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

For the invoice reviewer, seeing two valid records cannot prove there were only two executions. The application needs an independent expectation of completion, such as an externally retained final count or checkpoint, and must compare the supplied evidence with that expectation. That is an integration requirement, not a completeness guarantee furnished by this chain verifier.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C17

There is another boundary at the signer. A valid signature attributes a statement to the corresponding key; it does not prove that an outcome string is truthful or that the returned account data is correct. If the executing service lies, the signed record can preserve its claim for investigation, but the claim still needs corroboration. The records also contain parameters and identifiers, so operators should decide what belongs in an exported audit packet.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

For an operator review, keep the original decision, the ordered records and the independently selected verifier keys together. Ask the service owner to explain a partial outcome instead of normalizing it into success. Also document how the reviewer knows the workflow is finished. Those questions make the evidence useful without pretending that cryptographic integrity answers every operational question.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C19

The execution commands are [beta](https://docs.genesismesh.org/reference/public-contract.html). This article describes the inspected reference flow, not automatic instrumentation of every agent framework or a promise that all clients produce equivalent evidence.

Evidence: https://docs.genesismesh.org/reference/public-contract.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C21

Use a disposable [development installation](https://docs.genesismesh.org/installation.html). Follow the walkthrough's agreement, decision and executor-key setup, with the corresponding public key available to the verifier:

Evidence: https://docs.genesismesh.org/installation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C22

```text
python docs/examples/assets/scripts/execution-evidence-chain-demo.py --no-gif
```

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Documented procedure, not executed.

### C23

The documented result is a valid ordered chain, followed by a refusal when records are reordered. Inspect the partial outcome and each signed link. Then examine how the [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py) cover sequence and signature failures, and separately consider the valid-prefix limitation. Neither the example nor these tests were executed in this review.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2508.01332
- https://docs.genesismesh.org/concepts/governed-changes.html
- https://docs.genesismesh.org/examples/execution-evidence-chain.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/models/execution.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/execution.py
- https://docs.genesismesh.org/reference/public-contract.html
- https://docs.genesismesh.org/installation.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_execution.py
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
