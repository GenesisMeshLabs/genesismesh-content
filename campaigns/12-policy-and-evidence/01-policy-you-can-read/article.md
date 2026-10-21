# Policy You Can Read

A payments team decides that a vendor's transfers may not exceed ten thousand and may only run on weekdays during set hours. In most systems that rule becomes a line of code the auditor never sees. A year later an auditor holds a decision that allowed a large evening transfer and asks: which rule allowed this, and which version of it? Nothing in the decision can answer.

That is the gap between a signed decision and an explainable one.

A signature proves who decided. It does not prove what they decided by.

Genesis Mesh treats rules as signed, versioned documents. A boundary policy states which requests it covers and which gates they must pass. A gate is one named check: a value under a maximum, a region on an allowlist, a request inside a time window. The operator publishes the policy to its Network Authority, the service each operator runs to hold its keys and sign its trust decisions. The authority versions the policy, signs it and keeps every version.

Nothing in a policy runs code. Gates are fixed implementations the authority registers when it starts; a policy can only choose among them and set their limits. That keeps rules reviewable by people who do not write software, and keeps a policy from becoming a way in.

A decision made under policy names its rules. The signed decision carries a digest, a fingerprint, of the exact policy versions that applied, the order the gates ran in and the outcome of each. Anyone holding those policies can check that the decision was made under them, and a substituted policy fails verification. The decision shows which rules were applied, not that none was left out.

Publishing a policy does not switch it on. A new rule can run in observe mode first, recording what it would have refused without refusing anything, and rolling back restores the previous version's exact signed bytes. Making policy mandatory, so that every decision goes through policy evaluation, is the operator's choice, and a global policy is what covers every request.

When something is wrong, the answer is a signed deny. An unverifiable policy, an unknown gate, an enforcing gate that fails or lacks its fact: each produces a denial with a stable reason, never a silent pass.

Policy can also rest on membership. A vendor admitted to a sovereign holds an attestation, a signed statement of its roles and claims. A request can be evaluated against it directly, and the decision binds the attestation it relied on. Revoke the membership and every later request made on it is denied; a decision already issued lasts only its short validity, five minutes by default.

The operator still decides what the rules say. Genesis Mesh makes them something others can read, check and hold the operator to.
