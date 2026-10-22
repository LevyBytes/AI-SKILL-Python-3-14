# Python 3.14.0 beta 1 / library / numeric behavior

[gh-132987](https://github.com/python/cpython/issues/132987): A large number of builtin and extension functions that take an unsigned integer parameter will now consult [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) whenever it exists.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
