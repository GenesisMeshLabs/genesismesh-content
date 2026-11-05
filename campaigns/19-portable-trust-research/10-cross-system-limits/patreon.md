# Can an agent keep its limits when it crosses systems?

A planner asks a tool to read a report. The tool delegates to an agent, which calls an HTTP service. The final request arrives successfully, but somewhere along the route “read this report” has become “export every report.”

This illustrative workflow separates delivery from permission. A transport can carry a message correctly while an adapter loses the limits that should govern it. The [Agent Identity Protocol paper](https://arxiv.org/abs/2603.24775) explores verifiable delegation across MCP, A2A and HTTP. Its protocol proposal does not establish Genesis Mesh compatibility with those transports.

The practical question is what each receiver can inspect and what it must enforce itself.

## Carry a bounded invocation artifact

Genesis Mesh's beta [invocation-token workflow](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) provides a building block for this boundary. An issuer can create a signed `InvocationToken` with a bearer, agreement reference, capabilities, expiry and optional usage budget and constraints.

The `issue_invocation_token` function takes the supplied agreement or delegated scope and refuses requested capabilities outside that scope. The [issuance implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L108-L199) shows the containment check.

That check has a specific responsibility. The caller must validate the underlying authorization basis and choose an appropriate token lifetime. Issuing a token from supplied capabilities does not independently prove that the source agreement is authentic, currently valid or sufficient for every downstream operation.

For the report scenario, the issuer should grant the capability the receiving service actually requires for the intended read. The receiver needs a documented mapping from that capability to its endpoint and resource checks. A broad application method name is not a substitute for that mapping.

A valid token can then travel with the request, while the receiving system retains authority over whether and how its own resources are used. That is the useful portability boundary: inspectable evidence crossing systems without pretending that every system has identical execution rules.

## Verify the request at the consuming boundary

The receiver calls `verify_invocation_token` with trusted issuer keys, the requested capability, bearer identity and verification time. A wrong bearer, expired token or ungranted capability fails. The [verification code](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311) makes these checks explicit.

The bearer supplied to that function must come from an authenticated identity. Copying a name asserted by the request does not demonstrate who sent it. The integration also decides which issuer keys it trusts and how the token's agreement reference relates to an acceptable authorization basis.

The consuming service owns execution. If it verifies permission to read one report and then calls an unrestricted export operation, the token did not authorize the expansion. Resource selection and operation binding must remain intact between verification and execution.

The [delegation-chain guide](https://docs.genesismesh.org/examples/delegation-chain.html) describes a related way to inspect a supplied authority path. It is a separate mechanism, not an automatic guarantee that an arbitrary MCP, A2A or HTTP adapter preserves that path.

## Preserve the limits that need state

A token may include `max_invocations`, but the verifier counts caller-supplied use records. It does not provide a shared, durable replay counter across services. If two receivers independently present empty histories, the signed budget alone does not coordinate their decisions.

An integration that needs a global usage limit must coordinate trustworthy use state and handle concurrent requests. The API does not verify the entire linked use-record chain, so merely passing a collection of records should not be described as proof of globally complete consumption.

These are consequences of the [current verifier implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311), not an argument against scoped tokens. A signed limit and reliable accounting solve different parts of the problem. The system needs both when its promise depends on a finite shared budget.

Constraints also need precise interpretation. The supported `peer_sovereign:` constraint checks the bearer; it is not a general service URL or audience binding. Unknown constraints are refused. The [constraint checks](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L207-L250) define the available behavior rather than leaving arbitrary strings for a receiver to interpret optimistically.

## Review the adapter as part of authorization

For the report flow, review what happens to bearer identity, capability, resource selection, expiry and usage state at each handoff. An adapter that drops one of those checks changes the effective authorization boundary even when all messages still arrive.

The beta [process-mediation example](https://docs.genesismesh.org/examples/process-level-mediation.html) illustrates one local consumer of invocation credentials. It should not be generalized into universal transport enforcement. The protected service still needs to reject unchecked calls and keep execution credentials outside paths that bypass the intended checks.

A useful integration test therefore includes both an accepted read and an attempted export using the same credential. Acceptance demonstrates the intended route works. Refusal demonstrates that the receiver has preserved the boundary the token was meant to express.

## Check it yourself

From an installed source checkout, follow the [invocation-token walkthrough](https://docs.genesismesh.org/examples/invocation-bound-tokens.html), using its example agreement and keys:

```text
python docs/examples/assets/scripts/invocation-bound-tokens-demo.py --no-gif
```

Expect acceptance for the intended bearer and capability, and refusal with a wrong bearer or ungranted capability. Check the budget using explicit use records. The source example uses a controlled scenario clock; operational records need suitable current validity.

This documented example was not executed in this review. It demonstrates token checks, not coordinated accounting across deployed services or an end-to-end transport compatibility test.

## Further reading

- [Invocation-bound tokens](https://docs.genesismesh.org/examples/invocation-bound-tokens.html): issuance, verification and use records.
- [Delegation chains](https://docs.genesismesh.org/examples/delegation-chain.html): inspecting the supplied authority path.
- [Process-level mediation](https://docs.genesismesh.org/examples/process-level-mediation.html): one local consumer and its enforcement limits.

[Website](https://genesismesh.org/) · [Documentation](https://docs.genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [GitHub](https://github.com/GenesisMeshLabs/genesismesh)
