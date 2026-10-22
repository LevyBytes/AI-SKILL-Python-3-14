# `tp_traverse` in Python 3.8 and lower

#### `tp_traverse` in Python 3.8 and lower

The need to visit the type within `tp_traverse` arrived in Python 3.9. Should you support Python 3.8 and earlier, the traverse function must *not* visit the type, so it has to be more involved:

```c
static int my_traverse(PyObject *self, visitproc visit, void *arg)
{
    if (Py_Version >= 0x03090000) {
        Py_VISIT(Py_TYPE(self));
    }
    return 0;
}

```

Regrettably, [`Py_Version`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_Version) showed up only in Python 3.11. In its place, use:

- [`PY_VERSION_HEX`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.PY_VERSION_HEX), provided you are not on the stable ABI, or

- [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info) (by way of [`PySys_GetObject()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_GetObject) and [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple)).

[Subject index](INDEX.md) · [Previous source context](garbage-collection-protocol.md) · [Following source context](delegating-tp-traverse.md)
