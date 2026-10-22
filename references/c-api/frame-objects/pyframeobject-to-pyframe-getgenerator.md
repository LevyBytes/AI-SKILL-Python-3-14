# frame objects C API: `PyFrameObject`, `PyFrame_Type`, `PyFrame_New()`, `PyFrame_Check()`, `PyFrame_GetBack()`, `PyFrame_GetBuiltins()`, `PyFrame_GetCode()`, `PyFrame_GetGenerator()`

## Frame objects

### Frame objects

 type PyFrameObject

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) (as an opaque struct).*

The C structure underlying the objects that describe frame objects.

This structure exposes no public members.

Changed in version 3.11: This structure's members were taken out of the public C API. Consult the [What’s New entry](https://docs.python.org/3.14/whatsnew/3.11.html#pyframeobject-3-11-hiding) for the particulars.

To obtain a frame object, reach for the [`PyEval_GetFrame()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetFrame) and [`PyThreadState_GetFrame()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetFrame) functions.

Have a look as well at [Reflection](https://docs.python.org/3.14/c-api/reflection.html#reflection).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyFrame_Type

The type that frame objects carry. Over in the Python layer it is the very same object as [`types.FrameType`](https://docs.python.org/3.14/library/types.html#types.FrameType).

Changed in version 3.11: Formerly, reaching this type meant first including `<frameobject.h>`.

 PyFrameObject *PyFrame_New([PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *tstate, [PyCodeObject](https://docs.python.org/3.14/c-api/code.html#c.PyCodeObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *locals)

Build a fresh frame object. On success this function hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to that new frame object, and on failure it hands back `NULL` with an exception set.

 int PyFrame_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Hand back non-zero whenever *obj* is a frame object.

Changed in version 3.11: Formerly, reaching this function meant first including `<frameobject.h>`.

 PyFrameObject *PyFrame_GetBack(PyFrameObject *frame)

*Return value: New reference.*

Obtain the outer frame sitting just beyond *frame*.

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), or `NULL` should *frame* have no outer frame. No exceptions get raised here.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetBuiltins(PyFrameObject *frame)

*Return value: New reference.*

Obtain the [`f_builtins`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_builtins) attribute of *frame*.

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference). What comes back is never `NULL`.

Added in version 3.11.

 [PyCodeObject](https://docs.python.org/3.14/c-api/code.html#c.PyCodeObject) *PyFrame_GetCode(PyFrameObject *frame)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Obtain the code belonging to *frame*.

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

What comes back (the frame code) is never `NULL`.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFrame_GetGenerator(PyFrameObject *frame)

*Return value: New reference.*

Obtain whichever generator, coroutine, or async generator owns this frame, or `NULL` where no generator owns it. It raises no exception, even when the returned value is `NULL`.

Hand back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), or else `NULL`.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source contract](../floating-point-objects/pyfloat-unpack2-to-pyfloat-unpack8.md) · [Following source contract](pyframe-getglobals-to-pyframe-getlinenumber.md)
