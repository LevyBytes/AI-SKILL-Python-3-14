# Python 3.9.0 alpha 2 / core and builtins / sys

[bpo-39008](https://bugs.python.org/issue?@action=redirect&bpo=39008): [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) now insists on `Py_ssize_t` for the size arguments of its format string, no matter whether `PY_SSIZE_T_CLEAN` had been defined when included.

[bpo-38920](https://bugs.python.org/issue?@action=redirect&bpo=38920): Audit hooks were added for the moments when [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) and [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) run.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
