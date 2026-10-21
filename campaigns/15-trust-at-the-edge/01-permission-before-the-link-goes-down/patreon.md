# Permission Before the Link Goes Down

**Trust at the Edge · Part 1 of 2**

*What a device may do while it is cut off should be decided before the link goes down.*

A substation controller rotates the credentials for its local historian, the recorder that logs every reading, each night. One evening a storm takes out the backhaul, and the link to headquarters stays down until the next afternoon. The rotation is due before dawn.

The controller answers to its Network Authority, the service each operator runs to hold its keys and sign its trust decisions, and the authority is out of reach. That leaves two bad options. It can refuse, and leave an old credential in place. Or it can break the glass: make the change on a stated justification and sign a record for the authority to judge later. That keeps the change on the record, but nothing allowed it beforehand.

Our edge article admitted that an offline system keeps trusting its cached state. That told no device what it may do while cut off, and no auditor what it was allowed to do.

The answer is to decide before the link goes down.

Once grants are switched on, a privileged operator can have the authority sign a capability grant while the controller is connected. One executor key, the key the device signs its records with, may use named capabilities for at most 24 hours, within a budget of uses and a closed envelope of parameters. For example: rotate credentials under this device's own resources, up to four times, each new credential valid for seven to thirty days.

The authority checks every policy that applies against the whole envelope, not one sample request. If it cannot show that every request inside would be allowed, because a rule could deny one or depends on a fact nobody knows in advance, there is no grant. A grant never overrides a denial; it moves the decision earlier.

Offline, the controller checks each action against the grant and signs a record of it. This is portable trust carried to a device that is offline. On reconnect the authority checks every use again and admits each in its place in the device's chain, one at a time into the resource's history, so it never forks. A use that breaks the grant is quarantined: the change already happened, and the record shows it was not allowed.

Revoking what a grant rests on, or activating a policy that could deny a request inside it, revokes the grant; the device learns of it when it next fetches the signed revocation feed. Until then it can still act, but only a few uses (ten by default) past the last time the authority vouched for, and retiring its key refuses every use it signs.

When the link returns the next afternoon, the rotation is already on the record, checked against limits set the day before.

Offline action should be permitted in advance and proven on return.

**Builds on our video** Edge Infrastructure Needs Portable Identity: https://www.youtube.com/watch?v=J7OpYQy3ZkU

**Go deeper:**

Pre-issued grants: https://docs.genesismesh.org/operations/grants.html

**Next:** The Device Asks First

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
