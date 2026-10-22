# Python 3.14.3 final / library / array

[gh-142555](https://github.com/python/cpython/issues/142555): [`array`](https://docs.python.org/3.14/library/array.html#module-array): a crash in `a[i] = v`, happening when turning *i* into an index by way of [`i.__index__`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) or [`i.__float__`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) mutates the array, is now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
