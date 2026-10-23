# Extending Embedded Python - PyObject, PyArg_ParseTuple, PyLong_FromLong, PyMethodDef, PyModuleDef, PyModuleDef_HEAD_INIT, PyInit_emb, PyModuleDef_Init, Py_Initialize, PyImport_AppendInittab

### 1.4. Extending Embedded Python

So far the embedded Python interpreter has been unable to reach any functionality belonging to the application itself. The Python API makes this possible by extending the embedded interpreter — in other words, you augment the embedded interpreter with routines that the application hands over. It may sound involved, but it really is not. For a moment, set aside the fact that the application launches the Python interpreter. Picture the application instead as a collection of subroutines, and write some glue code that opens those routines up to Python, exactly as you would for an ordinary Python extension. To illustrate:

```c
static int numargs=0;

/* Return the number of arguments of the application command line */
static PyObject*
emb_numargs(PyObject *self, PyObject *args)
{
    if(!PyArg_ParseTuple(args, ":numargs"))
        return NULL;
    return PyLong_FromLong(numargs);
}

static PyMethodDef emb_module_methods[] = {
    {"numargs", emb_numargs, METH_VARARGS,
     "Return the number of arguments received by the process."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef emb_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "emb",
    .m_size = 0,
    .m_methods = emb_module_methods,
};

static PyObject*
PyInit_emb(void)
{
    return PyModuleDef_Init(&emb_module);
}

```

Drop the code shown above immediately ahead of the `main()` function. On top of that, put the two statements below in front of the [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) call:

```c
numargs = argc;
PyImport_AppendInittab("emb", &PyInit_emb);

```

That pair of lines sets up the `numargs` variable and exposes the `emb.numargs()` function to the embedded Python interpreter. Once these extensions are in place, the Python script is free to do things such as

```python
import emb
print("Number of arguments", emb.numargs())

```

Within a genuine application, these methods would surface an application API to Python.

[Subject index](INDEX.md) · [Previous source section](pure-embedding-and-pyobject-callobject.md) · [Next source section](embedding-python-in-c.md)
