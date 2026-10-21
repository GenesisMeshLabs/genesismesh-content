# The Rules Can't Live in One Head

For most of its life, Genesis Mesh held to a handful of rules. A fix comes with a test. A skipped test is not a passed test. One layer of the code never reaches into another. A public interface does not change without warning. Some were written down and some were enforced, but mostly they held because one maintainer applied them on every change.

That works until the project grows.

In a trust layer, a broken rule is rarely loud. A verifier that quietly accepts a record it should refuse looks exactly like one that works. The same is true of the project around it: a test that silently did not run looks exactly like one that passed.

So the project's repositories, the core, the gateway and four SDKs, were assessed against one question: could they take several times the features and several times the contributors without regressions slipping through? The safety net was strong. What would not scale was its dependence on one memory. The rules had to move out of a head and into the checks every change must pass.

Every repository merges through a merge queue, which tests each change again on top of everything ahead of it before it lands. In the jobs meant to run them, tests that need a live authority or a real database fail rather than skip. A pull request titled as a fix that changes code but no test is stopped unless the maintainer waives it.

Some rules now move in one direction only. The architecture rules say which layers of the code may depend on which. The violations that existed when the rules arrived sit on a list that can shrink but never grow, the way a building code lets old wiring stay until it is replaced but allows no new wiring that fails it. Coverage of the trust, model and service code has a floor; the check fails below it and says when it can be raised. The public interfaces of the TypeScript and .NET SDKs and the gateway are compared with their last release, and a deliberate break has to be labeled and come with upgrade instructions. Property tests throw generated input at the strict JSON parsers that every signature rests on.

The reasoning is written down too. Published decision records say how releases work, what each SDK is for and how the verifiers stay independent. One, on how a verifier will treat a record kind it has never seen, is decided but not yet built. An operator can read what the project has committed to; a contributor can read why.

Now no single person has to remember the rules, and no single reviewer has to catch everything.

None of this appears in a feature list. It appears later, as the regression that never shipped.
