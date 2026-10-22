# Python 3.6.4 release candidate 1 / core and builtins / collections and iteration

[bpo-32176](https://bugs.python.org/issue?@action=redirect&bpo=32176): Rather than depending on the caller to set it right, co_flags.CO_NOFREE is now always assigned correctly by the code object constructor from freevars and cellvars. This guarantees it gets cleared automatically once extra cell references are injected into a modified code object and function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
