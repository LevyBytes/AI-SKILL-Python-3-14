# Python 3.9.0 alpha 1 / c api / functions and types

[bpo-37633](https://bugs.python.org/issue?@action=redirect&bpo=37633): Export once more a handful of function compatibility wrappers covering macros found in `pythonrun.h`.

[bpo-15088](https://bugs.python.org/issue?@action=redirect&bpo=15088): The C function `PyGen_NeedsFinalizing` is gone. Following the [**PEP 442**](https://peps.python.org/pep-0442/) implementation, nothing inside CPython documented, tested, or relied on it. Joannah Nanjekye wrote the patch. (Patch by Joannah Nanjekye)

[bpo-37879](https://bugs.python.org/issue?@action=redirect&bpo=37879): Adjust subtype_dealloc so it holds back the type decref whenever the base type happens to be a C heap type

[bpo-35381](https://bugs.python.org/issue?@action=redirect&bpo=35381): The posixmodule.c statically allocated types `DirEntryType` and `ScandirIteratorType` were migrated over to heap-allocated types.

[bpo-37207](https://bugs.python.org/issue?@action=redirect&bpo=37207): `type` objects now take part in the vectorcall protocol: point `tp_vectorcall` at a vectorcall function and it replaces `tp_new` and `tp_init` when the class itself is called.

[bpo-37483](https://bugs.python.org/issue?@action=redirect&bpo=37483): Introduce the new `_PyObject_CallOneArg` function, which calls an object using a single positional argument.

[bpo-37337](https://bugs.python.org/issue?@action=redirect&bpo=37337): Supply quick method-calling functions: `_PyObject_VectorcallMethod()`, `_PyObject_CallMethodNoArgs()` and `_PyObject_CallMethodOneArg()`.

[bpo-37221](https://bugs.python.org/issue?@action=redirect&bpo=37221): The fresh function `PyCode_NewWithPosOnlyArgs()` builds code objects much like `PyCode_New()` does, but adds an extra *posonlyargcount* parameter that states how many positonal-only arguments there are.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
