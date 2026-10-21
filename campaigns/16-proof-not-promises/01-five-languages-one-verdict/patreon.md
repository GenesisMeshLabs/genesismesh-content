# Five Languages, One Verdict

**Proof, Not Promises · Part 1 of 4**

*We promised that any implementation would reach the same verdict. This is how that promise became a test.*

Our article on protocol interoperability made a promise. A compliance team holding only an issuer's public key could verify a signed record in .NET, months after a Go service produced it. Because the signature covers canonical bytes, any compliant implementation reaches the same answer. That is what makes portable trust portable: whoever receives the record can check it.

When we set out to prove it, we found a gap in our own claim. The SDKs' verify methods called the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, over HTTP. A ".NET verification" was the Python reference checking its own output.

That was not independent verification. It was delegation with extra steps.

So the claim became something a machine checks. Python is the reference. The Go, TypeScript, .NET and Rust SDKs verify signed records locally, from public keys alone, and return the reference's reason codes, so a refusal means the same thing in every language. Go and .NET verify agreements, decisions, data-use records, the authority's key history and a grant's signature; TypeScript and Rust also verify evidence exports, grant uses and the other newer records. Offline verification does not check revocation, which needs the issuer's current state.

Then the implementations judge each other. On every change to the core, a live scenario starts a local authority, has two sovereigns negotiate an agreement, issues decisions under it and has the TypeScript SDK sign requests to use data. Python, Go, TypeScript and .NET judge the results, each artifact by at least two of them, tampered copies included, and the run fails if any two disagree. Rust, the fifth, is held to the same answers through the shared conformance vectors: fixed inputs and expected outputs, copied byte for byte into each SDK that runs them.

The agreement in that scenario carries "Zürich ✓" and the number 1.0 on purpose. The vectors had caught Go and .NET producing different canonical bytes from Python for non-ASCII text and floating-point numbers: a record signed in one language could fail in another. Both were fixed.

A later survey found the five reading some JSON differently: duplicate keys, values that are not numbers, broken Unicode, integers too large for 64 bits. Two verifiers given the same bytes could each see a different record. Every verifier refuses such input, unknown signed fields and non-canonical records, so a record the reference signs gets one verdict everywhere. All five come from one project; the checks prove that the ports agree, byte for byte and reason for reason.

For an independent operator, the point is practical: verify another sovereign's records in your team's language, with no call to the issuer, and get the reference's answer.

Interoperability is one verdict, checked on every change, by implementations that do not take each other's word for it.

**Builds on our video** Why Trust Protocols Need Interoperability: https://www.youtube.com/watch?v=v4ORssb6nLw

**Check it yourself:**

Interoperability: https://docs.genesismesh.org/development/interoperability.html
Canonical form: https://docs.genesismesh.org/reference/canonical-form.html

**Next:** What a Proof Proves

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
