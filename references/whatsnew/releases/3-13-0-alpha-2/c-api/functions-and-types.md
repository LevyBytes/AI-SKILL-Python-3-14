# Python 3.13.0 alpha 2 / c api / functions and types

[gh-112026](https://github.com/python/cpython/issues/112026): Bring back the `_PyDict_GetItemStringWithError()` function, which numpy relies on. Victor Stinner contributed the patch.

[gh-110964](https://github.com/python/cpython/issues/110964): The undocumented private _PyArg functions together with the _PyArg_Parser structure were relocated into the internal C API (`pycore_modsupport.h`). Victor Stinner did the work.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
