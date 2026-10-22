# Python 3.9.0 alpha 5 / core and builtins / asyncio

[bpo-39965](https://bugs.python.org/issue?@action=redirect&bpo=39965): Properly raise `SyntaxError` whenever *await* appears inside a non-async function while `PyCF_ALLOW_TOP_LEVEL_AWAIT` is set (as it is in the asyncio REPL). Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
