# Python 3.7.0 alpha 3 / core and builtins / functions and types

[bpo-32176](https://bugs.python.org/issue?@action=redirect&bpo=32176): The code object constructor now derives co_flags.CO_NOFREE reliably from freevars and cellvars, instead of relying on the caller to supply the right value. As a result, the flag clears itself automatically whenever extra cell references get injected into an altered code object and function.

[bpo-31781](https://bugs.python.org/issue?@action=redirect&bpo=31781): Stops crashes from happening when methods are invoked on an uninitialized `zipimport.zipimporter` object. Oren Milman contributed the patch.

[bpo-30399](https://bugs.python.org/issue?@action=redirect&bpo=30399): A standard repr() of a BaseException carrying a single argument no longer leaves a redundant trailing comma behind.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
