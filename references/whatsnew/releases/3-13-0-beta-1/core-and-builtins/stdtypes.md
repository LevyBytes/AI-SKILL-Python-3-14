# Python 3.13.0 beta 1 / core and builtins / stdtypes

[gh-117431](https://github.com/python/cpython/issues/117431): Raise the performance of the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) methods below by converting them to the [`METH_FASTCALL`](https://docs.python.org/3.14/c-api/structures.html#c.METH_FASTCALL) calling convention:

  - `count()`

  - `find()`

  - `index()`

  - `rfind()`

  - `rindex()`

[gh-117709](https://github.com/python/cpython/issues/117709): Accelerate calls to [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) carrying a positional-only argument by adopting the [**PEP 590**](https://peps.python.org/pep-0590/) `vectorcall` calling convention. Erlend Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
