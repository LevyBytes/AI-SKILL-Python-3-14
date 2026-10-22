# Python 3.8.0 beta 1 / c api / exceptions and tracebacks

[bpo-36763](https://bugs.python.org/issue?@action=redirect&bpo=36763): `Py_Main()` now hands back the exitcode instead of invoking `Py_Exit(exitcode)` when it calls `PyErr_Print()` and the active exception type happens to be `SystemExit`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
