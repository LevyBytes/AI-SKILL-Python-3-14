# Python 3.13.0 alpha 1 / c api / long

[gh-108014](https://github.com/python/cpython/issues/108014): The new [`PyLong_AsInt()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt) function resembles [`PyLong_AsLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLong) but deposits its result in a C int rather than a C long. It previously existed as the private `_PyLong_AsInt()` (carrying an underscore prefix). Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
