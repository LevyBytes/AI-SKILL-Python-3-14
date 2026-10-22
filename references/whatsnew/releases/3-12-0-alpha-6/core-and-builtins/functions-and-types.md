# Python 3.12.0 alpha 6 / core and builtins / functions and types

[gh-102250](https://github.com/python/cpython/issues/102250): Repaired a segfault that showed up when the interpreter invokes a `__bool__` method that raises.

[gh-101696](https://github.com/python/cpython/issues/101696): For static types, invalidate the type version tag inside `_PyStaticType_Dealloc`, heading off a defect where a false cache hit might crash the interpreter. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
