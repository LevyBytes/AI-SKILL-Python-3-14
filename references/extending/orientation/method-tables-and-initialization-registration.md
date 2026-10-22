# The Module’s Method Table and Initialization Function — PyMethodDef, PyArg_ParseTuple, PyObject, PyArg_ParseTupleAndKeywords, PyModuleDef, PyInit_name, PyMODINIT_FUNC, PyInit_spam, PyModuleDef_Init, PyImport_Inittab, PyImport_AppendInittab

### 1.4. The Module’s Method Table and Initialization Function

I said earlier I would demonstrate how `spam_system()` gets invoked from Python programs. To begin, we must record its name and address inside a “method table”:

```c
static PyMethodDef spam_methods[] = {
    ...
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    ...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

```

Take note of the third field (`METH_VARARGS`). That flag informs the interpreter which calling convention applies to the C function. Under normal circumstances it should always be `METH_VARARGS` or `METH_VARARGS | METH_KEYWORDS`; a value of `0` indicates that an outdated form of [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) is in play.

With `METH_VARARGS` alone, the function should anticipate the Python-level parameters arriving as a tuple suitable for parsing through [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple); further details on that function appear below.

You may switch on the [`METH_KEYWORDS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_KEYWORDS) bit in the third field when keyword arguments are to reach the function. Then the C function should take a third `PyObject *` parameter, which will be a dictionary of keywords. Parse the arguments to such a function with [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords).

The module definition structure has to point at the method table:

```c
static struct PyModuleDef spam_module = {
    ...
    .m_methods = spam_methods,
    ...
};

```

That structure, in its turn, has to be delivered to the interpreter through the module’s initialization function. The initialization function has to bear the name `PyInit_name()`, with *name* standing for the module’s name, and it should be the sole non-`static` item declared in the module file:

```c
PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModuleDef_Init(&spam_module);
}

```

Be aware that [`PyMODINIT_FUNC`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyMODINIT_FUNC) gives the function a `PyObject *` return type, supplies whatever special linkage declarations the platform calls for, and under C++ marks the function as `extern "C"`.

The first time any interpreter imports its module `spam`, `PyInit_spam()` runs. (Remarks on embedding Python follow below.) [`PyModuleDef_Init()`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyModuleDef_Init) has to return a pointer to the module definition, so the import machinery is able to build the module and place it into `sys.modules`.

While embedding Python, the `PyInit_spam()` function won’t run on its own unless the [`PyImport_Inittab`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_Inittab) table contains an entry for it. Register the module in the initialization table with [`PyImport_AppendInittab()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_AppendInittab), and if you like follow that with an import of the module:

[Subject index](INDEX.md) · [Previous source section](argument-parsing-and-return-value-example.md) · [Next source section](module-embedding-and-interpreter-support.md)
