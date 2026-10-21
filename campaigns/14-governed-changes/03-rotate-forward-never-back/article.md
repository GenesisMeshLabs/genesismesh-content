# Rotate Forward, Never Back

A verdict changes nothing on its own. Late on a Friday, an engineer replaces the shared secret a partner's integration uses to call in, by hand, without asking first. An observer reports it, and the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, judges it: deny, under the policy in force at the time. Now what? Who is told? Is the change undone? Can anyone decide it should stand?

The obvious remedy, disabling the denied version, is the wrong one.

Twenty services may already be reading that secret, and the partner's systems with them. Disabling it turns a policy violation into an outage. Rolling back to the previous version is worse: the engineer may have replaced it because it had leaked.

So Genesis Mesh, once the operator switches remediation on, separates deciding the remedy from carrying it out. The operator's policy says what a denial leads to: undo the change, or only raise an alert, after a grace period. Without that guidance, the default is an alert. The authority tracks every denial until it is settled, and records an audit event when it next finds one overdue. The controller, the program that makes changes for the operator, does the work, tells the person the record names, and logs that notice with the authority.

Undoing a credential that others read means rotating forward, never back. The controller first creates a new version under an ordinary governed decision, so readers move to something legitimate, and only then disables the denied one. Both steps are signed and linked to each other. Where there is no version to rotate forward to, the remedy falls back to an alert.

Sometimes the denied change should stand. Perhaps the engineer was right and the policy was behind. That call is a review, and it takes a second person: the approving key must belong to someone other than whoever asked for the review and whoever the source reports made the change, as the operator maps those names to key holders. The signed requests behind the review travel inside it, so an auditor can check the approval offline, years later. A waiver always has an end, and when it lapses the remedy is due again. A review in progress pauses no deadline.

A change that truly cannot wait has its own route: a separate emergency permission with its own policy, a mandatory review and a limited lifetime for whatever it creates.

The operator's policy decides what happens. The authority signs the verdict and the review, the controller signs the remedy it carried out, so each can be checked later, and anything left undone stays visible as overdue.

A bad change should be undone without breaking what depends on it, and forgiven only by someone who did not make it.
