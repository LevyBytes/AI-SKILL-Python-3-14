# Tracebacks

### Tracebacks

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyTraceBack_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object backing traceback objects. On the Python side it surfaces as [`types.TracebackType`](https://docs.python.org/3.14/library/types.html#types.TracebackType).

 int PyTraceBack_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yields true when *op* is a traceback object and false otherwise. Subtypes are not taken into consideration by this function.

 int PyTraceBack_Here([PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *f)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Swap out the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute of the active exception, putting in a fresh traceback that has *f* placed ahead of the chain already there.

Invoking this when no exception is set leads to undefined behavior.

On success it hands back `0`; on failure it hands back `-1` while leaving an exception set.

 int PyTraceBack_Print([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *tb, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *f)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Emit the traceback *tb* to the file *f*.

On success it hands back `0`; on failure it hands back `-1` while leaving an exception set.

[Subject index](INDEX.md) · [Previous source contract](warning-types.md)
