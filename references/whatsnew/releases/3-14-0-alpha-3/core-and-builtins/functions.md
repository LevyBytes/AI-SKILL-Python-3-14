# Python 3.14.0 alpha 3 / core and builtins / functions

[gh-113841](https://github.com/python/cpython/issues/113841): Address a potential undefined-behavior divide-by-zero inside [`complex`](https://docs.python.org/3.14/library/functions.html#complex)’s [`_Py_c_pow()`](https://docs.python.org/3.14/c-api/complex.html#c._Py_c_pow).

[gh-126868](https://github.com/python/cpython/issues/126868): Speed up [`int`](https://docs.python.org/3.14/library/functions.html#int) by giving compact ints a freelist.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
