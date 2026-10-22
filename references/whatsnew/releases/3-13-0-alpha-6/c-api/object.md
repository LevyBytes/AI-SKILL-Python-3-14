# Python 3.13.0 alpha 6 / c api / object

[gh-115754](https://github.com/python/cpython/issues/115754): Introduce [`Py_GetConstant()`](https://docs.python.org/3.14/c-api/object.html#c.Py_GetConstant) plus [`Py_GetConstantBorrowed()`](https://docs.python.org/3.14/c-api/object.html#c.Py_GetConstantBorrowed) for fetching constants. As an example, `Py_GetConstant(Py_CONSTANT_ZERO)` gives back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the constant zero. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
