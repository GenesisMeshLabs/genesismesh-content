# Finding Our Own Flaws First

Three routes took the caller's word for an agreement, reading it from the request without checking its signatures. Anyone holding a routine operator key could present an agreement nobody had signed and get back a signed decision from the Network Authority, the service each operator runs to hold its keys and sign its trust decisions: a yes for any capability no policy covered.

We found it ourselves, reviewing released code before building the next stage on it. The same review found that a request could name its own parties. A second review, of the fix itself, found the same pattern in the consensus routes.

The fix changed the default. The authority trusts an agreement only if two different parties signed it with keys from state it signed itself: its own key, or a key in an active recognition treaty it issued. Nothing in the request can add a trusted key. A switch to keep the old behavior was drafted, then removed, because refusing forged input is the fix. The published security advisory states its limit: it stops fabricated agreements, but an operator key can still decide under a genuine agreement or attestation it presents, because operator keys are not yet bound to a sovereign.

External testing found a different gap. An operator's signature did not cover the whole administrative request. It now binds the method, path, query and public key of the authority it is addressed to, so no other route or authority will accept it. The older, looser form is refused.

Every project has flaws. What matters is who finds them first.

So before each stage ships, two automated reviewers go over it, a critic that measures what the code does and a skeptic that challenges the design, and once they also went back over what had already shipped. They back nearly every finding with a probe, and the maintainer decides each one. They have caught a review that could hold a remediation open forever, an emergency decision its own requester could approve, and a failed enrollment that left a usable key behind. Each fix carries a regression test, a test that fails on the flawed code and passes on the fix, kept so the flaw cannot quietly return. Some questions stay open, and the record says which.

Each fix is in the public changelog and release history, and the security policy lists what Genesis Mesh does not defend against beside what it does.

Software that never reports a flaw has not stopped having them. It has stopped looking, or stopped telling. An operator deciding whether to depend on Genesis Mesh should be able to see what was found, when, and how it was closed.

Trust is earned by the record of what was fixed, not by the claim that nothing was broken.
