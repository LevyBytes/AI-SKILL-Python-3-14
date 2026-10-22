# Python 3.12.0 alpha 4 / core and builtins / resolve case where incomplete frames might briefly become visible

[gh-100126](https://github.com/python/cpython/issues/100126): Resolve a case where “incomplete” frames might briefly become visible to C code while neighboring frames were being torn down, potentially corrupting the interpreter or crashing it hard while finalizers run.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
