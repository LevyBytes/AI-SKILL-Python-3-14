# type PyCFunctionFastWithKeywords

type PyCFunctionFastWithKeywords

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

The function type behind Python callables written in C that use the signature METH_FASTCALL | METH_KEYWORDS. Here is the function signature:

```c
PyObject *PyCFunctionFastWithKeywords(PyObject *self,
                                      PyObject *const *args,
                                      Py_ssize_t nargs,
                                      PyObject *kwnames);

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Previous source contract](pycfunctionfast.md) · [Following source contract](pycmethod.md)
