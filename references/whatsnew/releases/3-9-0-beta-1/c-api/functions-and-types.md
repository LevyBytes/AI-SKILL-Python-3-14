# Python 3.9.0 beta 1 / c api / functions and types

[bpo-39465](https://bugs.python.org/issue?@action=redirect&bpo=39465): Drop the `_PyUnicode_ClearStaticStrings()` function out of the C API.

[bpo-38787](https://bugs.python.org/issue?@action=redirect&bpo=38787): A PyCFunction_CheckExact() macro was added for precise type checks, given that subtypes of PyCFunction are now permitted, together with PyCMethod_CheckExact() plus PyCMethod_Check() covering the fresh PyCMethod subtype.

[bpo-40545](https://bugs.python.org/issue?@action=redirect&bpo=40545): Annotate `_PyErr_GetTopmostException()` using `PyAPI_FUNC()` so the function gets exported correctly within the C API. A private (`_Py`) prefix still applies to the function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
