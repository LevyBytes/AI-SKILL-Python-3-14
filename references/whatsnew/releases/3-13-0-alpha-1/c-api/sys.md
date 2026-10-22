# Python 3.13.0 alpha 1 / c api / sys

[gh-105145](https://github.com/python/cpython/issues/105145): Several older Python initialization functions are deprecated:

  - [`PySys_ResetWarnOptions()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_ResetWarnOptions)

  - [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix)

  - [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath)

  - [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix)

  - [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath)

  - [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName)

  - [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome)

Victor Stinner wrote the patch.

[gh-85283](https://github.com/python/cpython/issues/85283): The new [`PySys_AuditTuple()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AuditTuple) function mirrors [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) except that event arguments arrive as a Python [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) object. Victor Stinner wrote the patch.

[gh-108765](https://github.com/python/cpython/issues/108765): These standard headers are no longer pulled in by `Python.h`: `<time.h>`, `<sys/select.h>` and `<sys/time.h>`. Include them directly when you need them. As an example, `<time.h>` supplies the `clock()` and `gmtime()` functions, `<sys/select.h>` supplies the `select()` function, and `<sys/time.h>` supplies the `futimes()`, `gettimeofday()` and `setitimer()` functions. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
