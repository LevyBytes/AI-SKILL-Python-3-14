# Asynchronous Generator Objects

### Asynchronous Generator Objects

See also

[**PEP 525**](https://peps.python.org/pep-0525/)

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyAsyncGen_Type

The type object that stands for asynchronous generator objects. Over in the Python layer this surfaces as [`types.AsyncGeneratorType`](https://docs.python.org/3.14/library/types.html#types.AsyncGeneratorType).

Added in version 3.6.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyAsyncGen_New([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *frame, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname)

Build a fresh asynchronous generator around *frame*, its `__name__` and `__qualname__` set to *name* and *qualname*. This function steals *frame*, which may not be `NULL`.

When it succeeds, the function hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the new asynchronous generator. When it fails, it returns `NULL` with an exception set.

Added in version 3.6.

 int PyAsyncGen_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yields true when *op* is an asynchronous generator object, and false otherwise. This function always succeeds.

Added in version 3.6.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](generator-objects.md) · [Previous source contract](pygenobject-to-pygen-getcode.md) · [Following source contract](pyasyncgenasend-checkexact.md)
