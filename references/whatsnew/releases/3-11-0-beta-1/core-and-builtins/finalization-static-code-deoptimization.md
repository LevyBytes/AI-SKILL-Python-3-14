# Python 3.11.0 beta 1 / core and builtins / during py finalize deoptimize statically allocated code objects ensuring any

[gh-92031](https://github.com/python/cpython/issues/92031): During `Py_FINALIZE()`, deoptimize the statically allocated code objects, ensuring that any later `_PyCode_Quicken` calls begin from unquickened code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
