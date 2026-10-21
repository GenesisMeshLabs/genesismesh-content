# A Front Door, Not an Authority

A regional operator runs forty internal services. Before any of them acts, it needs one answer: is this certificate still good? Each could ask the Network Authority, the service each operator runs to hold its keys and sign its trust decisions, directly. Then each needs the authority's keys pinned, its signed revocation list fetched and checked for freshness, the signature rules implemented exactly, and a network path to the authority itself. Forty copies of the same verification. Forty chances to get freshness wrong. Forty services that can reach the system that issues trust, when most of them should not.

A relying service needs answers from the authority, not access to it.

The Genesis Mesh gateway is the front door for those services. It verifies, scopes and forwards, and never becomes an authority itself. It never holds the authority's signing key and mints no credentials outside a local development mode. The only authority key it may hold is a read-only one, for listing a network's public members. Whatever it tells a relying service rests on signatures the authority made.

Verification happens in one place. The gateway checks certificates against authority keys the operator pinned and a signed revocation list it refreshes every minute, and callers cannot swap in their own. If refreshes fail, it answers from the last verified list until that list's signed validity runs out, then reports itself not ready. Its answer, trusted or not with reasons, is evidence; the relying service still binds the identity to its own session and makes the decision.

Access is scoped. Each client receives explicit permissions per network and per group of services, and the gateway forwards only operations in a reviewed catalog. The gateway's own build checks that catalog against the authority's source on every change, so the front door cannot drift from the house behind it. Through it, relying services can also run governed actions without direct access to the authority. A client's gateway credential is never forwarded, so it cannot become an authority credential.

Where operators want them, the gateway adds mutual TLS, identities from their existing sign-in provider, and audit events held until the operator's collector acknowledges them.

Operators also get a console in the browser. When an action needs an operator signature, the browser computes it; the signing key never reaches the gateway and is not stored. The console has one limit: it trusts the gateway that serves it. If you do not control that gateway, sign with an SDK, from keys and metadata you verified yourself.

Which certificates count, which policies apply, which revocations hold: those stay with the sovereign that owns them. The gateway carries trust to forty services without putting a second authority in the middle.

Verification can be shared. Authority cannot.
