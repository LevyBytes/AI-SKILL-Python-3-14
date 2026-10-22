# Python 3.14.0 alpha 5 / core and builtins / long

[gh-129149](https://github.com/python/cpython/issues/129149): Add a fast path for medium-size integers within [`PyLong_FromUnsignedLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUnsignedLong), [`PyLong_FromUnsignedLongLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUnsignedLongLong) and [`PyLong_FromSize_t()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromSize_t).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
