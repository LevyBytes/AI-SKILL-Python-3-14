# type PyCFunctionWithKeywords

type PyCFunctionWithKeywords

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The function type behind Python callables written in C that use the signature METH_VARARGS | METH_KEYWORDS. Here is the function signature:

```c
PyObject *PyCFunctionWithKeywords(PyObject *self,
                                  PyObject *args,
                                  PyObject *kwargs);

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Following source contract](pycfunctionfast.md)
