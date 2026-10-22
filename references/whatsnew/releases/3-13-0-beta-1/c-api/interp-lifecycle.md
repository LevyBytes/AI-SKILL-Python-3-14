# Python 3.13.0 beta 1 / c api / interp lifecycle

[gh-117987](https://github.com/python/cpython/issues/117987): Bring back the functions that had been dropped during Python 3.13 alpha 1:

  - [`Py_SetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_SetPythonHome)

  - [`Py_SetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_SetProgramName)

  - [`PySys_SetArgvEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.PySys_SetArgvEx)

  - [`PySys_SetArgv()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.PySys_SetArgv)

Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
