# Pickle buffer objects

## Pickle buffer objects

### Pickle buffer objects

Added in version 3.8.

For out-of-band data transfer through the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module, a [`pickle.PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer) object encloses a [buffer-providing object](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyPickleBuffer_Type

Standing for the Python pickle buffer type, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is one and the same as [`pickle.PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer) over in the Python layer.

 int PyPickleBuffer_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yield true when *op* is a pickle buffer instance. The call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyPickleBuffer_FromObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Build a pickle buffer out of the object *obj*.

Where *obj* lacks support for the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), the call fails.

When it works, a fresh pickle buffer instance comes back; when it doesn't, an exception is set and `NULL` is returned.

This parallels invoking [`pickle.PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer) on *obj* from Python.

 const [Py_buffer](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) *PyPickleBuffer_GetBuffer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *picklebuf)

Obtain a pointer to the [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) underneath that the pickle buffer encloses.

That pointer stays good for as long as *picklebuf* remains alive and unreleased. Whoever holds it must neither alter nor free the [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) handed back. Where the pickle buffer has already been released, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

When it works, a pointer to the buffer view is returned; when it doesn't, an exception is set and `NULL` comes back.

 int PyPickleBuffer_Release([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *picklebuf)

Let go of the buffer underneath that the pickle buffer is holding.

A `0` comes back on success; on failure an exception is set and `-1` is returned.

This parallels invoking [`pickle.PickleBuffer.release()`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer.release) from Python.

[Subject index](INDEX.md) · [Previous source contract](../support-for-perf-maps/pyunstable-perfmapstate-init-to-pyunstable-perfmapstate-fini.md) · [Following source contract](../profiling-and-tracing/pytrace-call-to-pyeval-settrace.md)
