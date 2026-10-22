# Python 3.12.0 alpha 1 / c api / code

[gh-94936](https://github.com/python/cpython/issues/94936): Added [`PyCode_GetVarnames()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetVarnames), [`PyCode_GetCellvars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetCellvars) and [`PyCode_GetFreevars()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_GetFreevars), which expose `co_varnames`, `co_cellvars` and `co_freevars` respectively through the C API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
