# Python 3.9.0 alpha 1 / c api / interpreter path initialization arguments

[bpo-38234](https://bugs.python.org/issue?@action=redirect&bpo=38234): Python had been disregarding arguments passed to `Py_SetPath()`, `Py_SetPythonHome()` and `Py_SetProgramName()`; initialization is fixed so those supplied arguments actually apply.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
