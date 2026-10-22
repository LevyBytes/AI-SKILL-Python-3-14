# Python 3.14.0 alpha 3 / core and builtins / code

[gh-127020](https://github.com/python/cpython/issues/127020): On the free threading build, stop a crash that struck whenever [`PyCode_GetCode()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCode), [`PyCode_GetVarnames()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetVarnames), [`PyCode_GetCellvars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCellvars), or [`PyCode_GetFreevars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetFreevars) ran concurrently across threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
