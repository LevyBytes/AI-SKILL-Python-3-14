# int PyModule_AddObject(PyObject *module, const char *name, PyObject *value)

int PyModule_AddObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Resembles `PyModule_AddObjectRef()`, except it steals a reference to *value* on success (that is, when it returns `0`).

The newer `PyModule_Add()` or `PyModule_AddObjectRef()` functions are the recommended choice, since misusing the `PyModule_AddObject()` function makes reference leaks easy to introduce.

Note
Where other reference-stealing functions differ, `PyModule_AddObject()` gives up its hold on *value* **on success** alone.

What this implies is that you have to inspect its return value, and on error the caller is responsible for running [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) over *value* by hand.

A usage example:

```c
PyObject *obj = PyBytes_FromString(value);
if (PyModule_AddObject(module, "spam", obj) < 0) {
    // If 'obj' is not NULL and PyModule_AddObject() failed,
    // 'obj' strong reference must be deleted with Py_XDECREF().
    // If 'obj' is NULL, Py_XDECREF() does nothing.
    Py_XDECREF(obj);
    goto error;
}
// PyModule_AddObject() stole a reference to obj:
// Py_XDECREF(obj) is not needed here.

```

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymodule-addobjectref-to-pymodule-add.md) · [Previous source contract](pymodule-addintconstant.md)
