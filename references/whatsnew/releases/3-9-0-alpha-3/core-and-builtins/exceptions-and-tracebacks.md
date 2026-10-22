# Python 3.9.0 alpha 3 / core and builtins / exceptions and tracebacks

[bpo-39048](https://bugs.python.org/issue?@action=redirect&bpo=39048): Sharpen the error message shown when wrong types reach `async with` statements, by consulting the `__aenter__()` special method ahead of the `__aexit__()` special method while entering an asynchronous context manager. Géry Ogam authored the patch.

[bpo-39114](https://bugs.python.org/issue?@action=redirect&bpo=39114): Trace functions reported the wrong executing line while tracing exception handlers that bind a name; this is now fixed. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
