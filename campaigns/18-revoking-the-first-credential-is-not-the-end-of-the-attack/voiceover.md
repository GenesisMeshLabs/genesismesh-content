# Revoking the First Credential Is Not the End of the Attack

When a credential is compromised, the natural response is to revoke it.

But what if the attacker has already used it to create another one?

In its 21 October 2026 investigation, Microsoft described a campaign in which attackers used an agentic AI framework to accelerate activity following a ConnectWise supply-chain compromise. Microsoft observed application abuse and follow-on activity through Microsoft Graph, including application credential changes and attempts to modify privileges.

The important lesson is not that AI invented a new category of attack. It is that familiar actions can now happen faster and in parallel.

An attacker can use one compromised application to discover another. They can add credentials, change permissions and establish routes back in. By the time the original application is disabled, the authority created through it may still exist elsewhere.

That changes the incident-response question from “Did we revoke the original credential?” to:

What did it access while it was valid?
Did it create or change another credential?
Did it grant new permissions or establish a new identity?
Are active sessions still valid?
Have all relevant enforcement points received the revocation?
Can we verify that the next request is actually denied?

Also, a successful authentication does not by itself prove that data was stolen. Microsoft makes that distinction in its report, and an investigation should preserve it.

Genesis Mesh is being built around the idea that authority should have a clear scope and a lifecycle. A decision should identify the actor, action and resource. A grant should have limits. Revocation needs to reach the place where the action is enforced. And the resulting decision and reported execution should be available as evidence.

None of this is a universal kill switch. It only covers systems connected to the boundary and depends on how they handle stale policy, offline operation, existing sessions and downstream credentials. Those details need to be tested, not assumed.

For teams responding to a real incident, the immediate work remains to follow the affected vendor’s containment guidance, inspect sign-ins and application changes, revoke compromised credentials, and investigate what they were used to do.

Revocation is not just an instruction to stop trusting one key. It is the work of finding where that key’s authority has already travelled.
