# What's New In Python 3.11 / C API Changes / Deprecated

### Deprecated

- The following functions for configuring Python's initialization are now deprecated:

  - `PySys_AddWarnOptionUnicode()`

  - `PySys_AddWarnOption()`

  - `PySys_AddXOption()`

  - `PySys_HasWarnOptions()`

  - `PySys_SetArgvEx()`

  - `PySys_SetArgv()`

  - `PySys_SetPath()`

  - `Py_SetPath()`

  - `Py_SetProgramName()`

  - `Py_SetPythonHome()`

  - `Py_SetStandardStreamEncoding()`

  - `_Py_SetProgramFullPath()`

Switch over to the new [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) API from the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) ([**PEP 587**](https://peps.python.org/pep-0587/)). (Contributed by Victor Stinner in [gh-88279](https://github.com/python/cpython/issues/88279).)

- The `ob_shash` member of [`PyBytesObject`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytesObject) is now deprecated; reach for [`PyObject_Hash()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Hash) in its place. (Contributed by Inada Naoki in [bpo-46864](https://bugs.python.org/issue?@action=redirect&bpo=46864).)

[Subject index](INDEX.md) · [Previous source section](thread-state-frame-access-migration.md) · [Next source section](c-api-changes-pending-removal-in-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
