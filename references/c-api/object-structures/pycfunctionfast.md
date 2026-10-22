# type PyCFunctionFast

type PyCFunctionFast

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

The function type behind Python callables written in C that use the signature `METH_FASTCALL`. Here is the function signature:

```c
PyObject *PyCFunctionFast(PyObject *self,
                          PyObject *const *args,
                          Py_ssize_t nargs);

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Previous source contract](pycfunctionwithkeywords.md) · [Following source contract](pycfunctionfastwithkeywords.md)
