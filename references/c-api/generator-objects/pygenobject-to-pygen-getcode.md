# generator objects C API: `PyGenObject`, `PyGen_Type`, `PyGen_Check()`, `PyGen_CheckExact()`, `PyGen_New()`, `PyGen_NewWithQualName()`, `PyGen_GetCode()`

type PyGenObject

The C structure that backs generator objects.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyGen_Type

The type object that stands for generator objects.

 int PyGen_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields true when *ob* is a generator object; *ob* may not be `NULL`. This function always succeeds.

 int PyGen_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields true when *ob*'s type is exactly `PyGen_Type`; *ob* may not be `NULL`. This function always succeeds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyGen_New([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *frame)

*Return value: New reference.*

Build and hand back a fresh generator object built atop the *frame* object. This function steals a reference to *frame*. The argument may not be `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyGen_NewWithQualName([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *frame, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname)

*Return value: New reference.*

Build and hand back a fresh generator object built atop the *frame* object, its `__name__` and `__qualname__` set to *name* and *qualname*. This function steals a reference to *frame*. The *frame* argument may not be `NULL`.

 [PyCodeObject](https://docs.python.org/3.14/c-api/code.html#c.PyCodeObject) *PyGen_GetCode(PyGenObject *gen)

Hand back a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the code object that *gen* wraps. This function always succeeds.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](generator-objects.md) · [Following source contract](pyasyncgen-type-to-pyasyncgen-checkexact.md)
