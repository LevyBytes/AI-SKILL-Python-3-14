# Providing finer control over data attributes - Custom_init, PyObject, PyArg_ParseTupleAndKeywords, Py_INCREF, Py_DECREF, Py_XDECREF, tp_dealloc, tp_new

```c
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
    CustomObject *self = (CustomObject *) op;
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_DECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_DECREF(tmp);
    }
    return 0;
}

```

These revisions let us guarantee the `first` and `last` members are never `NULL`, so nearly everywhere the `NULL` checks become unnecessary. As a result, the bulk of the [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) calls can become [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) calls. The sole spot where this swap is impossible is the `tp_dealloc` implementation, because there the members might have failed to initialize back in `tp_new`.

As we did earlier, we also rename both the module initialization function and the module name used inside it, and an additional entry is appended to the `setup.py` file.

[Subject index](INDEX.md) · [Previous source section](providing-finer-control-over-data-attributes-and-tp-init.md) · [Next source section](supporting-cyclic-garbage-collection.md) · [Owning section and setup](providing-finer-control-over-data-attributes.md)
