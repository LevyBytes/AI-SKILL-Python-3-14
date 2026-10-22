# Python 3.14.4 final / core and builtins / functions and types

[gh-146227](https://github.com/python/cpython/issues/146227): Corrects an incorrect type within `_Py_atomic_load_uint16` belonging to the C11 atomics backend (`pyatomic_std.h`); it had performed a 32-bit atomic load rather than a 16-bit one. Mohammed Zuhaib discovered this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
