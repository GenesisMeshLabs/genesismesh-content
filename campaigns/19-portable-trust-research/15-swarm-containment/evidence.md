# Evidence review: idea 15

Scope: Attenuating delegation verification as the main mechanism; minimal guard limitations retained to avoid implying containment or bypass prevention.

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

On 2026-11-05 the author reopened the delegation walkthrough, process-level mediation guide, installation guide, public contract and Delegation Without Trust abstract. Retained pinned delegation.py was inspected again, including root-signature verification, parent-term digest, subset and expiry-ceiling checks, and later-hop delegator continuity. This verifier has no current-time argument and is not a fresh relationship/policy check. Guard memory-budget/no-fetch limits retain the pinned daemon citation to preserve a precise implementation reference. Independent review confirmed unchanged main and latest v1.9.1 release.

The source and release matrix above retains its dated observations; the common source review records the current publication check. No product example, test or live scenario was executed for this revision. The prior concise corrections are retained. This article uses signed records and local authority as its frame, not token economics, a reputation score or a blockchain platform.

## Exact claim ledger for the expanded revision

### C02

A coordinator delegates a dataset-reading task to a specialist. The specialist is compromised and starts asking for writes. Another agent is willing to help. In this illustrative scenario, the danger is not confined to one bad response: authority can spread through apparently routine handoffs unless each receiving system checks what the previous participant was actually allowed to pass on.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C03

[Delegation Without Trust](https://arxiv.org/abs/2609.00267) studies confinement under the assumption that the model itself may be compromised. Its broker results are not a Genesis Mesh security guarantee. The useful question for this article is narrower: what can a receiver verify about a chain of delegated capabilities, and what must still be enforced outside that chain?

Evidence: https://arxiv.org/abs/2609.00267

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C05

Genesis Mesh treats the parties as independently operated trust domains. A signed `AgreementRecord` provides the root of the delegation chain. The [delegation walkthrough](https://docs.genesismesh.org/examples/delegation-chain.html) then creates a `DelegatedAgreementRecord` for each handoff, naming the parent, the delegator, the recipient and the delegated terms.

Evidence: https://docs.genesismesh.org/examples/delegation-chain.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C06

In the dataset example, the coordinator can pass on a reading capability already present in the parent terms. The specialist cannot turn that record into a valid delegation of a writing capability outside the parent's set. This is useful even when the specialist's language model is fully under an attacker's control: the receiving verifier evaluates signed artifacts rather than accepting the specialist's explanation of why it needs more authority.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C07

The [builder and verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) bind each record to its parent terms by digest. The delegator signs, and the recipient adds its signature. The final verification requires valid signatures from the keys supplied for both participants. An attractive task description or a familiar participant name cannot substitute for those keys.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C08

That key mapping is itself part of the receiver's trust configuration. The chain is not a mechanism for deciding which organizations deserve recognition. The verifier must be given the correct keys for the root parties and the relevant keys for each hop; accepting attacker-provided key mappings would change the question being answered.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C10

The [chain verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py) first verifies the root agreement's signatures. It then checks parent identifiers, the parent-terms digest, the capability subset, the expiry ceiling and the delegation signatures. These are concrete relationships among records. A signature alone would not establish that the signer held the authority it was handing onward.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C11

Continuity matters after the first handoff. A root-agreement party may create the first delegation, but a later delegator must be the preceding recipient. The [tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) cover unauthorized later-hop delegators as well as attempts to widen capabilities. That prevents a participant from inserting itself into a path merely because it can sign a new record.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C12

For the compromised specialist, a fabricated writing hop should fail the capability-subset check. Extending the child record beyond the parent's expiry should fail the validity-ceiling check. These failures identify a broken delegation claim before the receiving service considers executing the requested dataset action.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C13

However, an expiry ceiling is not a check that the whole relationship is valid now. The inspected verifier does not take a current-time parameter or fetch current revocation state. A cryptographically consistent chain can still need rejection by the service's current policy. The distinction is visible in the [verification function](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py).

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C15

The dataset service still checks the current relationship, target resource and operation parameters before execution. Capability-set attenuation is not a general policy engine for arbitrary dataset constraints. If a reading capability is too broad for the task, preserving that broad capability through several valid signatures does not make the original scope safer.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C16

The service must also use the verification result. Logging a failed delegation while performing the write would preserve evidence of the failure without containing it. The operator should make the acceptance decision part of the execution path and specify how a denial reaches the caller. This is an integration responsibility, not a property created merely by producing a chain file.

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C17

A separate [process-level guard](https://docs.genesismesh.org/examples/process-level-mediation.html) illustrates another boundary. Its execution path can constrain an agent only when the operator removes direct credentials and alternate routes to tools or subprocesses. Advisory instrumentation does not meet that condition. The guide explicitly separates advisory use from mandatory mediation.

Evidence: https://docs.genesismesh.org/examples/process-level-mediation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C18

The [guard implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py) also has limits: its in-memory invocation budget resets on restart, and it makes no revocation fetches. New token revocations remain unseen, while expiry and other local checks still apply. It is not kernel enforcement or hardware attestation. Delegation and guard CLI commands are [beta](https://docs.genesismesh.org/reference/public-contract.html).

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py; https://docs.genesismesh.org/reference/public-contract.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C20

Use a disposable [development installation](https://docs.genesismesh.org/installation.html), the root agreement, the parties' keys and the recognition-graph exports described by the walkthrough:

Evidence: https://docs.genesismesh.org/installation.html

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

### C21

```text
python docs/examples/assets/scripts/delegation-chain-demo.py --no-gif
```

Evidence: Illustrative scenario, operational inference, or reproduction guidance; assessed with the immediately preceding/following cited mechanism. This paragraph asserts no independent deployment result.

Classification: Documented procedure, not executed.

### C22

Inspect an accepted handoff and an attempt to delegate a capability outside the parent's set. Check the parent digest, both signatures and the keys used to verify them. Read the [delegation tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py) for forged widening and unauthorized later-hop cases. Separately identify where your service checks present validity and resource parameters. The example and tests were not executed in this review.

Evidence: https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py

Classification: Source-based explanation with limits; cited code is implementation evidence, cited tests are source coverage only, and research is not a product guarantee.

## Reader-accessible sources

- https://arxiv.org/abs/2609.00267
- https://docs.genesismesh.org/examples/delegation-chain.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/delegation.py
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_trust_delegation.py
- https://docs.genesismesh.org/examples/process-level-mediation.html
- https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/guard/daemon.py
- https://docs.genesismesh.org/reference/public-contract.html
- https://docs.genesismesh.org/installation.html
- https://genesismesh.org/
- https://docs.genesismesh.org/
- https://mesh.genesismesh.org/
- https://github.com/GenesisMeshLabs/genesismesh

## Review and channel decision

Expanded wording passed independent source-based technical and editorial review. Repository publication was explicitly authorized and remains subject to the final publication checks. This revision makes no Patreon or LinkedIn publication or schedule change. Covers remain unchanged.
