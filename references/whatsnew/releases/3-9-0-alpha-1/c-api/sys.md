# Python 3.9.0 alpha 1 / c api / sys

[bpo-38234](https://bugs.python.org/issue?@action=redirect&bpo=38234): `Py_SetPath()` now points [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) at the program full path ([`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath)) in place of the program name ([`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
