# Python 3.8.0 alpha 4 / build / build and platforms

[bpo-36707](https://bugs.python.org/issue?@action=redirect&bpo=36707): The `m` flag is no longer appended to SOABI (sys.implementation.cache_tag) by `./configure --with-pymalloc`. Whether pymalloc is on or off has no bearing on the ABI.

[bpo-36635](https://bugs.python.org/issue?@action=redirect&bpo=36635): The `PyAPI_FUNC(type)`, `PyAPI_DATA(type)` and `PyMODINIT_FUNC` macros in `pyport.h` now behave differently once `Py_BUILD_CORE_MODULE` is defined. To build a C extension as a dynamic library that reaches Python internals, `Py_BUILD_CORE_MODULE` must now be defined: this exports the `PyInit_*xxx*()` function among the DLL exports on Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
