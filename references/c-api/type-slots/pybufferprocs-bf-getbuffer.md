# getbufferproc PyBufferProcs.bf_getbuffer

getbufferproc PyBufferProcs.bf_getbuffer

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_bf_getbuffer` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Here is the signature of this function:

```c
int (PyObject *exporter, Py_buffer *view, int flags);

```

Service a request asking *exporter* to populate *view* according to *flags*. Apart from point (3), any implementation of this function MUST carry out these steps:

1.

Determine whether the request can be satisfied. When it cannot, raise [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError), assign `view->obj` to `NULL`, and return `-1`.

2.

Fill in the requested fields.

3.

Bump an internal counter tracking the number of exports.

4.

Assign `view->obj` to *exporter* and increment `view->obj`.

5.

Return `0`.

**Thread safety:**

Under the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), implementations are required to guarantee:

- The export counter bump performed in step (3) happens atomically.

- Throughout the lifetime of every export, the underlying buffer data stays valid and pinned to a stable memory location.

- Where objects allow resizing or reallocation (for instance [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)), the export counter is examined atomically ahead of those operations, and [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError) is raised whenever exports remain.

- Calling this function concurrently from several threads is safe.

Consult also [Thread safety for memoryview objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-memoryview) regarding the Python-level thread safety promises that [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects make.

When *exporter* belongs to a chain or tree of buffer providers, two principal approaches are available:

- Re-export: every node of the tree behaves as the exporting object and points `view->obj` at a fresh reference to itself.

- Redirect: the buffer request gets forwarded to the tree's root object. Here `view->obj` becomes a fresh reference to the root object.

Each separate field of *view* gets covered in section [Buffer structure](https://docs.python.org/3.14/c-api/buffer.html#buffer-structure); the rules for how an exporter must respond to particular requests appear in section [Buffer request types](https://docs.python.org/3.14/c-api/buffer.html#buffer-request-types).

Every region of memory referenced within the [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure is owned by the exporter and has to stay valid until no consumers remain. For the consumer, [`format`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.format), [`shape`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.shape), [`strides`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.strides), [`suboffsets`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.suboffsets) and [`internal`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.internal) are read-only.

A convenient route to exposing a plain bytes buffer while handling every request type correctly is [`PyBuffer_FillInfo()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FillInfo).

On the consumer side, [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) is the interface wrapping this function.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pybufferprocs.md) · [Following source contract](pybufferprocs-bf-releasebuffer.md)
