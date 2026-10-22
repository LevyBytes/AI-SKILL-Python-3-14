# Exception Classes

### Exception Classes

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_NewException(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *base, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This utility function builds a brand-new exception class and hands it back. The *name* argument has to be the name of the new exception, given as a C string in the shape `module.classname`. The *base* and *dict* arguments are usually `NULL`. The result is a class object that descends from [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) (reachable in C as `PyExc_Exception`).

The new class gets its [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute set to the leading portion (everything up to the final dot) of the *name* argument, while the class name becomes the trailing portion (everything after the final dot). You can supply the *base* argument to name alternate base classes; it may be a single class or a tuple of classes. You can supply the *dict* argument to provide a dictionary of class variables and methods.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_NewExceptionWithDoc(const char *name, const char *doc, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *base, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dict)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The same as `PyErr_NewException()`, only the new exception class can readily be supplied a docstring: when *doc* is non-`NULL`, it serves as the docstring for the exception class.

Added in version 3.2.

 int PyExceptionClass_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Hand back non-zero when *ob* is an exception class, and zero otherwise. This function always succeeds.

 const char *PyExceptionClass_Name([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Hand back the [`tp_name`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_name) of the exception class *ob*.

[Subject index](INDEX.md) · [Previous source contract](pyerr-checksignals-to-pysignal-setwakeupfd.md) · [Following source contract](pyexceptioninstance-check-to-pyunstable-exc-prepreraisestar.md)
