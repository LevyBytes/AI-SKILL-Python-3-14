# Python 3.12.0 alpha 1 / c api / arg

[gh-94930](https://github.com/python/cpython/issues/94930): Fixes the `SystemError` that [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) raised when `#` appeared in `(...)` yet `PY_SSIZE_T_CLEAN` had not been defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
