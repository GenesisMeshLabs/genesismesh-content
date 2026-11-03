# A Signed Release Can Still Be Malicious

A release is signed.

The build passed through the real pipeline. The package came from the expected publisher. The signature is valid.

Would you trust it?

On 21 October 2026, LiteLLM published a compromised version of its package through its own release pipeline. According to its [investigation](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain), the attack began months earlier with an administrative key accidentally committed to a public repository. The file was removed, but the key remained valid.

An attacker later used it to access an agent platform, extract a GitHub token associated with an organization owner, and move through the release environment. The malicious release was built, signed and published by the legitimate pipeline.

The signature did not fail. It confirmed that the release passed through a system the attacker had already gained the authority to use.

That distinction matters, especially as we give agents access to more tools.

An agent that can create a pull request does not need an organization owner’s credential. A release workflow that can sign an artifact should not automatically have the authority to change the rules that decide what gets signed. And removing a leaked secret from a file is not the same as revoking it.

The questions I keep coming back to are simple:

- What is this identity allowed to do?
- Which exact resource and action does that permission cover?
- Who can change or override the policy?
- What happens when the credential is exposed?
- Can the same compromised administrator also change the evidence?

This is the kind of problem we are exploring with Genesis Mesh: portable policy decisions, scoped authority, revocation and evidence that can be checked separately from the system that performed the action.

But I want to be clear about the limit. A signed record does not prove that a decision was wise, that the signer was uncompromised, or that an artifact is safe. A policy boundary only helps where it is actually enforced. And evidence must be protected from the same attacker who controls the system being audited.

Genesis Mesh would not have magically patched the LiteLLM pipeline or guaranteed that this attack failed. The practical goal is narrower: make authority explicit, reduce how much a stolen credential can do, and make important actions easier to verify.

A valid signature tells you something happened under a key.

The next question is whether that key should have been able to make it happen.
