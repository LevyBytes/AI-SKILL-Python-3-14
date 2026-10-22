# Python 3.11.0 alpha 1 / c api / structures

[bpo-44378](https://bugs.python.org/issue?@action=redirect&bpo=44378): To dodge a compiler warning, [`Py_IS_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IS_TYPE) no longer relies on [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE): it stops casting `const PyObject*` into `PyObject*`. Victor Stinner provided the patch.

[bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573): Turn the [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) and [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) macros into static inline functions. From now on the [`Py_SET_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_TYPE) and [`Py_SET_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_SIZE) functions are required for assigning an object's type and size. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
