# coroutine objects C API: `PyCoroObject`, `PyCoro_Type`, `PyCoro_CheckExact()`, `PyCoro_New()`

type PyCoroObject

The C structure used for coroutine objects.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCoro_Type

The type object corresponding to coroutine objects.

 int PyCoro_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Report true when the type of *ob* is `PyCoro_Type`; here *ob* may not be `NULL`. The call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCoro_New([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *frame, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname)

*Return value: New reference.*

Build a fresh coroutine object from the *frame* object and return it, assigning *name* to `__name__` and *qualname* to `__qualname__`. This call takes ownership of a reference to *frame*. The *frame* argument may not be `NULL`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](coroutine-objects.md) · [Following source contract](../curses-c-api/import-curses-to-pycursessetuptermcalled.md)
