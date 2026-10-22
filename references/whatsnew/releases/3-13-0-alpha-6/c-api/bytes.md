# Python 3.13.0 alpha 6 / c api / bytes

[gh-87193](https://github.com/python/cpython/issues/87193): [`_PyBytes_Resize()`](https://docs.python.org/3.14/c-api/bytes.html#c._PyBytes_Resize) may now be invoked on bytes objects whose reference count exceeds 1, the 1-byte bytes objects included. In that situation it builds a fresh bytes object and tears down the old one whenever its reference count is greater than 1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
