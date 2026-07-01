# Integration Without Authority Transfer

https://www.youtube.com/watch?v=Sj1-k7y5jhg

Enterprise integration usually requires someone to accept the other party's authority over part of their own infrastructure. This video is about why that's the wrong design ? and what the alternative looks like.

**The objective behind this video**

When two enterprises integrate, the commercial agreement is usually straightforward: scope, terms, exit conditions, liability. What's less often examined is what the technical integration actually requires one or both parties to accept. Typically, one organization's access control, credential lifecycle, and revocation decisions become entangled with the other's infrastructure ? or both become dependent on a third-party broker. The commercial relationship can be exited by signing a document. The trust infrastructure is much harder to unwind.

We built this video to show that the standard integration patterns impose an authority transfer that isn't actually required by the cooperation itself. Two enterprises can cooperate under explicit, bilateral recognition without either one becoming an authority over the other's identity system. Each issues a signed recognition treaty defining exactly what it recognizes in the other ? scope, capabilities, validity period. Cross-boundary requests carry signed evidence checked against that treaty. If one side revokes, the other detects it on next verification. Neither party's operations become dependent on the other's infrastructure being available.

The broader objective is to model the technical integration on the same terms as the commercial one: explicit, bounded, with a clear exit path that either party can exercise unilaterally. A recognition treaty in Genesis Mesh is the technical analog of a contract. That's not a metaphor ? it's a design principle. Integration should not require authority transfer. It should require agreement.

Website: https://genesismesh.connectorzzz.com
GitHub: https://github.com/GenesisMeshLabs
