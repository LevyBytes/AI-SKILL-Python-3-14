# Python 3.11.0 alpha 1 / c api / init config

[bpo-44113](https://bugs.python.org/issue?@action=redirect&bpo=44113): Mark these functions for configuring the Python initialization as deprecated:

  - `PySys_AddWarnOptionUnicode()`

  - `PySys_AddWarnOption()`

  - `PySys_AddXOption()`

  - `PySys_HasWarnOptions()`

  - `Py_SetPath()`

  - `Py_SetProgramName()`

  - `Py_SetPythonHome()`

  - `Py_SetStandardStreamEncoding()`

  - `_Py_SetProgramFullPath()`

Adopt the new [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) API belonging to the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) in their place ([**PEP 587**](https://peps.python.org/pep-0587/)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
