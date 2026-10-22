# Python 3.11.0 alpha 4 / core and builtins / collections and iteration

[bpo-44525](https://bugs.python.org/issue?@action=redirect&bpo=44525): Apply specialization to the CALL_FUNCTION instruction for one-argument calls into builtin types. This makes `range(x)`, `list(x)`, and notably `type(obj)` faster.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
