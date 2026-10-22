# Macros

### Macros

Favoring speed over safety, the following macros skip any pointer validation.

 char *PyByteArray_AS_STRING([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytearray)

* Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Behaves like `PyByteArray_AsString()`, just with the error checks omitted.

Note

Changing the bytearray concurrently while the char array it returned is being read is unsafe across threads.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyByteArray_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytearray)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

The same as `PyByteArray_Size()`, except that error checking is dropped.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pybytearrayobject-to-pybytearray-type.md) · [Previous source contract](pybytearray-fromobject-to-pybytearray-resize.md) · [Following source contract](../bytes-objects/bytes-objects.md)
