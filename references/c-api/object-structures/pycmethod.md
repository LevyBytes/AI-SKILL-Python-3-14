# type PyCMethod

type PyCMethod

The function type behind Python callables written in C that use the signature METH_METHOD | METH_FASTCALL | METH_KEYWORDS. Here is the function signature:

```c
PyObject *PyCMethod(PyObject *self,
                    PyTypeObject *defining_class,
                    PyObject *const *args,
                    Py_ssize_t nargs,
                    PyObject *kwnames)

```

Added in version 3.9.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Previous source contract](pycfunctionfastwithkeywords.md) · [Following source contract](pymethoddef-to-ml-doc.md)
