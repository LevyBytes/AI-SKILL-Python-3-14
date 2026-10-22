# Python 3.10.0 alpha 1 / c api / subinterpreters

[bpo-41936](https://bugs.python.org/issue?@action=redirect&bpo=41936): Dropped the undocumented macros `Py_ALLOW_RECURSION` and `Py_END_ALLOW_RECURSION`, together with the `recursion_critical` field belonging to the [`PyInterpreterState`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) structure.

[bpo-41834](https://bugs.python.org/issue?@action=redirect&bpo=41834): Drop the `_Py_CheckRecursionLimit` variable; `ceval.recursion_limit` of the [`PyInterpreterState`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) structure now takes its place. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
