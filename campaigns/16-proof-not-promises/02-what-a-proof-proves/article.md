# What a Proof Proves

The prover needed six steps to show that one of our published claims was false.

A test checks the cases someone thought to write down. An attacker replays, reorders, drops and splices messages, and the flaw that matters usually sits in an ordering nobody pictured. A formal model describes a protocol precisely enough for a tool to reason about every possible run of it. Genesis Mesh writes its models for Tamarin, a prover that plays out those runs against an attacker who controls the network. For each stated property it either proves it, finds a run that breaks it, or never reaches an answer. Cryptography is treated as perfect; what gets tested is the logic.

The project keeps two models. One describes the pipeline from agreement to decision to execution as it was designed in an early revision, and proves that in that design every decision rests on an agreement both parties acted on. The other describes an anomaly check each sovereign runs over evidence it processed itself about a counterparty. It stays with the operator who runs it, never shared, ranked or combined with anyone else's.

The counterexample came from the second model. Its first version claimed that every sudden drop would eventually raise an anomaly. Rather than adjust the model until the proof went through, we compared it with the code. The code agreed with the prover: with fewer than ten prior updates, or no variance in past ones, the implementation raises nothing. The claim was false for the software as well as the model, so it was removed rather than repaired. The rewritten model, which follows the code line by line, proves seven properties, among them that an update the statistics flag raises its anomaly in that same step. Whether the statistics notice a slow, deliberate drift is outside the model. One property exists only to prove the limitation: a short or flat history can hide a drop.

The harder lesson is how long the false claim stood. For more than a dozen releases the documentation called it machine-checked, though no job ran the prover and the proof tests skipped quietly without it, and a skipped test looks like a passing one.

A proof that never runs is only a claim.

So a skipped proof now fails the job. Both models are proved after every merge to main and on pull requests that touch them, though they do not gate every merge. A proof holds for its model, not for every line of the implementation. The pipeline model is not evidence about today's code until it is updated, and no model yet covers revocation feeds, treaties or trust bundles, which rest on tests and shared conformance vectors.

Claims about trust should be checkable, including the ones that turned out to be false.
