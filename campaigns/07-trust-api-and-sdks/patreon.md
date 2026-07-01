# Trust API and SDKs

https://www.youtube.com/watch?v=E2UQRM7c3Vo

The best protocol in the world doesn't get adopted if integrating it requires hand-rolling cryptographic signing before you can make your first call. This video is about how Genesis Mesh closes that gap.

**The objective behind this video**

We've watched developers encounter Ed25519 signing requirements and quietly move on to something simpler. And we understand why: the failure mode is brutal. Get one byte wrong in the canonical body ? a space, a sort order, a missing header ? and the signature fails with an authorization error that tells you nothing about where it diverged. The implementation cost isn't the algorithm; it's the exactness. Every byte matters, and there's no local feedback loop when you're wrong.

The Genesis Mesh Trust API exists because the protocol operations need to be reachable from real software without that implementation tax. Every meaningful operation is an HTTP endpoint: issuing an agreement, submitting an attestation, recording a boundary decision, querying consensus, logging a data-usage disclosure, building trust evidence. The SDKs in TypeScript, Go, and .NET handle request signing automatically ? you pass a key once at construction and every subsequent admin request is correctly signed.

The objective of this video is to show what "developer experience" means for a trust protocol specifically. It's not about simplifying the primitives ? it's about making sure the implementation is correct so the caller doesn't have to think about it. The harder work is understanding which primitive to use and when. The SDKs ensure that's the only hard work.

Website: https://genesismesh.connectorzzz.com
GitHub: https://github.com/GenesisMeshLabs
