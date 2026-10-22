# Python 3.6.1 release candidate 1 / c api / functions and types

[bpo-29083](https://bugs.python.org/issue?@action=redirect&bpo=29083): Corrected how several public API functions are declared. The limited API was missing PyArg_VaParse() and PyArg_VaParseTupleAndKeywords(). For limited API versions below 3.3, PyArg_ValidateKeywordArguments(), PyArg_UnpackTuple() and Py_BuildValue() were unavailable whenever PY_SSIZE_T_CLEAN is defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
