# type PyCFunction

### Implementing functions and methods

 type PyCFunction

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The function type behind most Python callables written in C. A function of this kind accepts two PyObject* arguments and gives back a single value of the same type. A `NULL` return means an exception must already have been raised. A non-`NULL` return is read as the value the function yields when surfaced in Python. The function is required to return a new reference.

Here is the function signature:

```c
PyObject *PyCFunction(PyObject *self,
                      PyObject *args);

```

[Subject index](INDEX.md) · [Previous source contract](py-type-to-pyvarobject-head-init.md) · [Following source contract](pycfunctionwithkeywords.md)
