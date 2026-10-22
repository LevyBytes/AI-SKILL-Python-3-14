# Python 3.13.0 alpha 1 / c api / removed

[gh-105145](https://github.com/python/cpython/issues/105145): The following older functions for configuring the Python initialization, which Python 3.11 deprecated, are removed:

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

Victor Stinner wrote the patch.

[gh-106023](https://github.com/python/cpython/issues/106023): The private `_PyObject_FastCall()` function is removed; reach instead for `PyObject_Vectorcall()`, available since Python 3.8 ([**PEP 590**](https://peps.python.org/pep-0590/)). Victor Stinner wrote the patch.

[gh-106084](https://github.com/python/cpython/issues/106084): The dated aliases pointing at calling functions, kept around for backward compatibility with the Python 3.8 provisional API, are removed:

  - `_PyObject_CallMethodNoArgs()`: use `PyObject_CallMethodNoArgs()`

  - `_PyObject_CallMethodOneArg()`: use `PyObject_CallMethodOneArg()`

  - `_PyObject_CallOneArg()`: use `PyObject_CallOneArg()`

  - `_PyObject_FastCallDict()`: use `PyObject_VectorcallDict()`

  - `_PyObject_Vectorcall()`: use `PyObject_Vectorcall()`

  - `_PyObject_VectorcallMethod()`: use `PyObject_VectorcallMethod()`

  - `_PyVectorcall_Function()`: use `PyVectorcall_Function()`

Updating your code is just a matter of stripping the underscore prefix. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
