# Python 3.13.0 alpha 6 / core and builtins / stdtypes

[gh-117431](https://github.com/python/cpython/issues/117431): Boost how fast the following [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) methods run by moving them onto the [`METH_FASTCALL`](https://docs.python.org/3.14/c-api/structures.html#c.METH_FASTCALL) calling convention:

  - `endswith()`

  - `startswith()`

[gh-117431](https://github.com/python/cpython/issues/117431): Boost how fast the following [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) methods run by moving them onto the [`METH_FASTCALL`](https://docs.python.org/3.14/c-api/structures.html#c.METH_FASTCALL) calling convention:

  - [`count()`](https://docs.python.org/3.14/library/stdtypes.html#str.count)

  - [`endswith()`](https://docs.python.org/3.14/library/stdtypes.html#str.endswith)

  - [`find()`](https://docs.python.org/3.14/library/stdtypes.html#str.find)

  - [`index()`](https://docs.python.org/3.14/library/stdtypes.html#str.index)

  - [`rfind()`](https://docs.python.org/3.14/library/stdtypes.html#str.rfind)

  - [`rindex()`](https://docs.python.org/3.14/library/stdtypes.html#str.rindex)

  - [`startswith()`](https://docs.python.org/3.14/library/stdtypes.html#str.startswith)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
