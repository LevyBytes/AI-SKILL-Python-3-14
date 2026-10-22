# Python 3.5.4 release candidate 1 / c api / functions and types

[bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867): The Function PySlice_GetIndicesEx() becomes a macro when Py_LIMITED_API holds a value between 0x03050400 and 0x03060000 (exclusive) or 0x03060100 and above.

[bpo-29083](https://bugs.python.org/issue?@action=redirect&bpo=29083): Correct the declarations of several public API functions. PyArg_VaParse() and PyArg_VaParseTupleAndKeywords() had been missing from the limited API. PyArg_ValidateKeywordArguments(), PyArg_UnpackTuple(), and Py_BuildValue() were absent from the limited API for versions below 3.3 whenever PY_SSIZE_T_CLEAN is defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
