# releasebufferproc PyBufferProcs.bf_releasebuffer

releasebufferproc PyBufferProcs.bf_releasebuffer

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_bf_releasebuffer` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Here is the signature of this function:

```c
void (PyObject *exporter, Py_buffer *view);

```

Service a request to free the buffer's resources. Where nothing needs freeing, `PyBufferProcs.bf_releasebuffer` is allowed to be `NULL`. Otherwise a typical implementation of this function performs these optional steps:

1.

Decrease an internal counter recording the number of exports.

2.

Should the counter be `0`, release all memory tied to *view*.

**Thread safety:**

Under the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build):

- The export counter decrease in step (1) has to be atomic.

- Cleaning up resources once the counter hits zero must happen atomically, since the final release can race against concurrent releases from other threads and deallocation must occur exactly once.

To track buffer-specific resources, the exporter MUST rely on the [`internal`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer.internal) field. That field is promised to stay constant, whereas a consumer MAY hand over a copy of the original buffer as the *view* argument.

This function MUST NOT decrement `view->obj`, because [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release) handles that automatically (an arrangement handy for breaking reference cycles).

On the consumer side, [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release) is the interface wrapping this function.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pybufferprocs.md) · [Previous source contract](pybufferprocs-bf-getbuffer.md) · [Following source contract](pyasyncmethods-to-pyasyncmethods-am-send.md)
