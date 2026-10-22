# Python 3.14.0 alpha 1 / c api / functions

[gh-120389](https://github.com/python/cpython/issues/120389): Introduce new functions that convert C `<stdint.h>` numbers to and from Python [`int`](https://docs.python.org/3.14/library/functions.html#int):

  - [`PyLong_FromInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt32)

  - [`PyLong_FromUInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt32)

  - [`PyLong_FromInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt64)

  - [`PyLong_FromUInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt64)

  - [`PyLong_AsInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt32)

  - [`PyLong_AsUInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsUInt32)

  - [`PyLong_AsInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt64)

  - [`PyLong_AsUInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsUInt64)

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
