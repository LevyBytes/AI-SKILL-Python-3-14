# Python 3.8.0 alpha 1 / c api / refcounting

[bpo-35059](https://bugs.python.org/issue?@action=redirect&bpo=35059): These C macros became static inline functions instead: [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF), [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF), [`Py_XINCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XINCREF), [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF), [`PyObject_INIT()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_INIT), [`PyObject_INIT_VAR()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_INIT_VAR).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
