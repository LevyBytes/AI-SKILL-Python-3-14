# Python 3.14.0 alpha 6 / core and builtins / stdtypes

[gh-129107](https://github.com/python/cpython/issues/129107): Two further [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) functions have been corrected for [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading).

[gh-129107](https://github.com/python/cpython/issues/129107): The [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) iterator is now safe under [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading).

[gh-129349](https://github.com/python/cpython/issues/129349): Both [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) and [`bytearray.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.fromhex) now take ASCII [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) along with [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

[gh-129107](https://github.com/python/cpython/issues/129107): The [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) is now safe under [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
