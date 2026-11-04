# Can an agent keep its limits when it crosses systems?

A planner asks a tool to read a report. The tool delegates to an agent, which calls an HTTP service. In this illustrative workflow, successful delivery says nothing about whether each receiver enforces the original permission.

The [Agent Identity Protocol paper](https://arxiv.org/abs/2603.24775) studies delegation across MCP, A2A and HTTP; it does not establish Genesis Mesh compatibility with that protocol.

Genesis Mesh's [beta invocation-token workflow](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) provides an inspectable building block. An issuer starts with an `AgreementRecord` or delegated scope and signs an `InvocationToken` naming a bearer, capabilities, expiry and optional budget and constraints. Issuance refuses capabilities outside the supplied scope. [Implementation](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L108-L199)

For our report request, the receiver calls `verify_invocation_token` with trusted issuer keys, the requested capability, bearer identity and verification time. A wrong bearer, expired token or ungranted capability fails. The receiver must authenticate that identity, validate the authorization basis and map the actual operation to the checked capability; copying an asserted bearer name is insufficient.

Limits must survive the adapter too. The [verifier](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L257-L311) counts caller-supplied use records, so a budget is not a shared replay counter. The integration must coordinate trustworthy use state. The API does not verify the whole linked use-record chain.

The supported `peer_sovereign:` constraint checks the bearer, not a general URL or service audience; unknown constraints are refused. Additional resource and audience binding remains integration work. [Constraint checks](https://github.com/GenesisMeshLabs/genesismesh/blob/a54b2d81f205c9b0203158f846f7ad44dc677063/genesis_mesh/trust/invocation_token.py#L207-L250)

The consuming service owns execution. Transporting a token does not authorize it to broaden the action.

## Check it yourself

From an installed source checkout, use the [token walkthrough](https://docs.genesismesh.org/examples/invocation-bound-tokens.html) and its example agreement and keys:

```text
python docs/examples/assets/scripts/invocation-bound-tokens-demo.py --no-gif
```

Expect acceptance for the intended bearer and capability; repeat with a wrong bearer or ungranted capability and inspect the refusal. Check the budget using explicit use records. This documented example was not executed in this review.


[Genesis Mesh](https://genesismesh.org/) · [Public demo](https://mesh.genesismesh.org/) · [Source repository](https://github.com/GenesisMeshLabs/genesismesh)
