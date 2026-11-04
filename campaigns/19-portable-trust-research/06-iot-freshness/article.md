# Offline IoT trust has a freshness budget

**Portable Trust · Part 6 of 6**

*A disconnected device needs an explicit limit on how old its authority information may become.*

Consider an illustrative outage: an edge controller has a valid credential and a cached grant, but no connection to its authority. Its next request could read a sensor or change a physical resource. A valid signature cannot tell the device about a revocation issued after the last connection.

Before an outage, the operator needs to specify which actions may proceed, for how long and on what evidence. Credential validity, grant expiry and revocation freshness answer different parts of that question.

## What runs on the device

The [Genesis Mesh edge-agent runbook](https://docs.genesismesh.org/operations/edge-agent.html) documents an edge agent that runs on a node. It enrolls with a one-time invite and keeps separate node and executor keys on the device. Local services ask it about a requested action; the services still perform the external change.

While connected, the agent asks the Network Authority, the operator's service that signs trust decisions, for a decision scoped to its node. When current authority cannot be obtained, a pre-issued grant can cover a bounded request. The [grant runbook](https://docs.genesismesh.org/operations/grants.html) defines the bearer, capabilities, validity interval, parameter envelope and maximum uses. Signed time tokens and chained use records support later verification. Grants and their evidence prerequisites require operator configuration and are off by default; the grant routes are beta.

The edge agent holds a snapshot of revocation information. Its documented default maximum age is one day, with a normal synchronization interval of 60 seconds and a clock assumption within roughly five minutes of the authority. These are implementation defaults and assumptions, not a safety certification or a recommended budget for every device. Snapshot freshness derives from its signed times, rather than treating a download time as proof that the information was newly issued.

When the snapshot is stale, the agent stops using grants. That is a concrete freshness boundary worth testing. It also means the operator must inspect the exceptional route before claiming that every action stops there.

## Break-glass is a separate decision

The edge agent has its own failure classification, so a controller's fallback behavior must not be assumed to apply to it. An NA 429 or 5xx response is treated as throttled or failing, allowing a covering grant but not break-glass. There is a specific exception: a proxy's 502, 503, 504 or 520–527 page without the NA's JSON error body is classified as unreachable, alongside connection, DNS, TLS and timeout failures. A suitable grant may cover the gap. An explicit deny cannot be overridden by a grant or break-glass.

When the authority is actually unreachable and no usable grant covers the action, a caller's justification may permit exceptional execution under the documented rules. Requests that fall outside a matching grant's scope remain refused. A hard requirement to stop on stale authority must therefore be checked at the precise local action boundary, including the exceptional route, rather than inferred from grant expiry alone.

The edge agent records activity in a durable outbox for later submission. Revoking a node at the authority also ends the associated authority that the runbook describes, including its grants and executor registration. The disconnected device learns the new state at its next synchronization. Refusing its later evidence cannot stop a physical effect it already produced while offline.

## Put the research beside the implementation

[Connectivity-Aware Hybrid Access Control for Low-Power IoT Devices](https://d2j16w31g89z0j.cloudfront.net/site/icoin2026/abs/P1-27.pdf) explores connectivity states and TTL-based freshness on an ESP32-class design. Its evaluation is qualitative, with quantitative performance work left for later. This is research context, not a Genesis Mesh hardware benchmark.

A safe simulator can vary the last signed snapshot, expire a grant, exhaust its use budget, replay old revocation information and change the local clock. Record whether each request waits, proceeds under a grant or uses break-glass. Reconnect and inspect the authority's later verdict separately from the effect.

These tests are proposed here, not reported hardware results. Real physical systems need independent safety engineering and protections. The trust layer can help make the authority budget explicit; it cannot decide which physical action is safe or deliver revocation information across a disconnected link.

## Check it yourself

Follow the linked edge-agent runbook's documented enrollment and local-service setup in a simulator. Enable `EVIDENCE_STORE=on` and `EVIDENCE_OUT_OF_BAND=on`, plus `EVIDENCE_GRANTS=on` for grants, all off by default. Pin the NA genesis root key and use HTTPS as documented. Use the guide's grant and evidence prerequisites and record the configured snapshot-age limit, grant envelope and use budget. Exercise the documented connected, grant and exceptional paths separately: explicit deny, NA 429/5xx, unreachable authority and stale signed snapshot are different cases. Include an out-of-envelope request with a justification and verify that the request is still refused.

This is a documented procedure with proposed simulator cases, not executed in this review. Reconnect and inspect evidence admission separately from the simulator's action log. No physical actuator or production resource is required to examine these trust boundaries.

**Builds on our video** [Edge Infrastructure Needs Portable Identity](https://www.youtube.com/watch?v=J7OpYQy3ZkU)

**Go deeper:**

[The edge agent](https://docs.genesismesh.org/operations/edge-agent.html)

**Related:** [Pre-issued grants and offline use](https://docs.genesismesh.org/operations/grants.html)

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
