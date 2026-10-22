# Python 3.7.0 alpha 1 / c api / functions and types

[bpo-6532](https://bugs.python.org/issue?@action=redirect&bpo=6532): For PyThread_start_new_thread() and PyThread_get_thread_ident(), the result type ? plus the id parameter of PyThreadState_SetAsyncExc() ? moved from ?long? over to ?unsigned long?.

[bpo-29083](https://bugs.python.org/issue?@action=redirect&bpo=29083): Repaired the declaration of several public API functions. The limited API had been missing PyArg_VaParse() and PyArg_VaParseTupleAndKeywords(). And PyArg_ValidateKeywordArguments(), PyArg_UnpackTuple(), and Py_BuildValue() were absent from the limited API in versions below 3.3 whenever PY_SSIZE_T_CLEAN is defined.

[bpo-28761](https://bugs.python.org/issue?@action=redirect&bpo=28761): Across the PyMemberDef, PyGetSetDef, PyStructSequence_Field, PyStructSequence_Desc, and wrapperbase structures, the name and doc fields now carry type `const char *` instead of `char *`.

[bpo-28426](https://bugs.python.org/issue?@action=redirect&bpo=28426): The undocumented PyUnicode_AsEncodedObject(), PyUnicode_AsDecodedObject(), PyUnicode_AsDecodedUnicode(), and PyUnicode_AsEncodedUnicode() functions are now deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
