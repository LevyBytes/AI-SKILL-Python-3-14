# Python 3.9.0 alpha 5 / c api / sys

[bpo-35370](https://bugs.python.org/issue?@action=redirect&bpo=35370): Whenever [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) fails inside [`PyEval_SetProfile()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfile) or [`PyEval_SetTrace()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTrace), record the failure as an unraisable exception.

[bpo-39882](https://bugs.python.org/issue?@action=redirect&bpo=39882): A macro now stands in for the [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) function; unless the `Py_LIMITED_API` macro is defined, it logs the name of the current function automatically.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
