# Python 3.10.0 alpha 1 / c api / refcounting

[bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573): Turn the [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) and [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) macros into static inline functions. Using them as an l-value no longer works; instead call [`Py_SET_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_SET_REFCNT) and [`Py_SET_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_SIZE) to assign an object's reference count and size. The break in backward compatibility is deliberate, readying the C API for an opaque [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) structure.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
