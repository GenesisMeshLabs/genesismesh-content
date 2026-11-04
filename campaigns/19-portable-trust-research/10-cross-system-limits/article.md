# Can an agent keep its limits when it crosses systems?

A planner asks a tool to read a report. The tool delegates to another agent, which calls an HTTP service. The messages arrive successfully. Did the original permission survive the journey?

In this illustrative workflow, the transport changes three times. The important boundary is at each consumer: which authority does it recognize, what action is permitted, and what prevents a request from being reused beyond its intended scope?

The [Agent Identity Protocol paper](https://arxiv.org/abs/2603.24775) explores delegation across MCP, A2A and HTTP. Its proposal is useful research context. It is not evidence that every integration carrying a token implements the same checks, nor that Genesis Mesh is wire-compatible with that protocol.

## Inspect what crosses the boundary

Genesis Mesh has a [documented beta invocation-token workflow](https://docs.genesismesh.org/examples/invocation-bound-tokens.html). An issuer starts with an `AgreementRecord`, or a delegated scope, and creates a signed `InvocationToken` naming its bearer and capabilities. The token also carries its agreement identifier, expiry and optional invocation budget and constraints.

The Python functions are `issue_invocation_token` and `verify_invocation_token`; the CLI exposes the corresponding `trust token` commands. In the [inspected implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L108-L199), issuance refuses capabilities absent from the supplied source scope.

For our report example, an issuer can grant `reports.read` to one named agent. At the receiving boundary, verification takes trusted issuer keys, the requested capability, the bearer's identity and a verification time. A token for a different bearer or capability fails. Changing JSON fields without a valid new signature does not expand the grant. [Verification and tests](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/tests/test_invocation_tokens.py#L203-L304)

Those checks are concrete. They are not a complete cross-protocol integration. The consumer must authenticate the caller, select trusted issuer keys, validate the underlying authorization basis and map the requested operation to the capability it verifies. Copying a bearer name from an untrusted request is not proof that the caller controls that identity.

## A budget needs trustworthy use state

A token's maximum-use field does not create a shared counter across services. The inspected verifier counts the `use_records` supplied by its caller; when no records are supplied, the count is zero. The integration must retain and coordinate the relevant state if it intends to enforce a shared budget. [Token verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311)

The workflow can produce signed `InvocationUseRecord` objects linked by digests. The documented API does not verify that whole use chain for you. Do not turn a linked record format into a claim of global replay prevention.

Scope has similar limits. The current constraint vocabulary includes `not_before:` and `peer_sovereign:`; the latter checks the bearer identity. It is not a general URL, merchant or HTTP-audience binding. Unrecognized constraints are refused by the verifier. A receiving adapter must enforce the additional resource and audience semantics its application needs. [Constraint implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L207-L250)

## Keep the boundary local

Genesis Mesh is portable trust infrastructure for independently operated systems. Carrying evidence lets another operator inspect a request's basis; it does not require that operator to accept it.

For the planner-to-tool-to-service journey, write down the consumer's checks at each hop. Identify who can mint a new token, where scope is narrowed, where use state is kept, and where the side effect occurs. Any missing adapter is still engineering work, even if the message transport is standardized.

## Check it yourself

Use the [invocation-token walkthrough](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) with a source checkout and the example agreement and signing keys. Run its documented local demo:

```text
python docs/examples/assets/scripts/invocation-bound-tokens-demo.py --no-gif
```

Verify a permitted capability for the intended bearer, then repeat with the wrong bearer or a capability outside the grant. Inspect the refusal codes and the budget example with explicit use records. This is a documented example, not executed in this review.

The useful test is not merely whether a token reaches the next service. It is whether that service enforces the intended limit with trustworthy inputs.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
