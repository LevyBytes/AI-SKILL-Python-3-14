# Python 3.14.0 alpha 7 / core and builtins / long

[gh-129149](https://github.com/python/cpython/issues/129149): Introduces a quick path covering small plus mid-range integers across [`PyLong_FromInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt32), [`PyLong_FromUInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt32), [`PyLong_FromInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt64) and [`PyLong_FromUInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt64). Chris Eibl supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
