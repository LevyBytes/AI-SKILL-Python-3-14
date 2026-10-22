# Python 3.11.0 beta 1 / c api / refcounting

[gh-91768](https://github.com/python/cpython/issues/91768): The argument type for the [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT), [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE), [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE), and [`Py_IS_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IS_TYPE) functions is now `PyObject*` rather than `const PyObject*`. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
