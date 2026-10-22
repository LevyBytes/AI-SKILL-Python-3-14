# Python 3.13.0 alpha 1 / c api / arg

[gh-104922](https://github.com/python/cpython/issues/104922): `PY_SSIZE_T_CLEAN` is no longer needed for `'#'` formats within APIs such as [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue). For `'#'` those routines always rely on `Py_ssize_t`, whether or not `PY_SSIZE_T_CLEAN` is set.

[bpo-40309](https://bugs.python.org/issue?@action=redirect&bpo=40309): Handle trailing spaces correctly when they precede a closing parenthesis inside [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) format strings.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
