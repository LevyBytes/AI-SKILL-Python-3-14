# Python 3.10.0 alpha 6 / security / types

[bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990): The [`types.FunctionType`](https://docs.python.org/3.14/library/types.html#types.FunctionType) constructor now inherits whatever the current builtins are if the *globals* dictionary lacks a `"__builtins__"` key, in place of falling back to `{"None": None}` as builtins — matching how the [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) and [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) functions behave. Declaring a function via `def function(...): ...` in Python is unaffected; this syntax cannot override globals, and it too inherits the current builtins. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
