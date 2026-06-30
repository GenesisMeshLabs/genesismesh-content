Data governance policies describe who can access what, under what conditions, and for what purpose.

The harder question is whether an access event was actually authorized at the moment it happened, by an authority allowed to grant it.

Genesis Mesh treats a data access event as a trust decision. A DataUsage disclosure record carries the purpose, policy reference, issuer, timestamp, and signature.

That artifact can be retained, presented to an auditor, and verified without reconstructing the decision from logs.

Genesis Mesh is not a data catalog, lineage tracker, or translation layer. It makes the authorization context auditable.
