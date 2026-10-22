# int PyBuffer_FillInfo(Py_buffer *view, PyObject *exporter, void *buf, Py_ssize_t len, int readonly, int flags)

int PyBuffer_FillInfo(Py_buffer *view, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exporter, void *buf, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len, int readonly, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Service buffer requests on behalf of an exporter that wishes to expose *buf* of size *len*, its writability determined by *readonly*. *buf* is treated as a sequence of unsigned bytes.

The *flags* argument signals the request type. This function always populates *view* as directed by flags, except where *buf* has been marked read-only while `PyBUF_WRITABLE` is set within *flags*.

When it succeeds, assign `view->obj` a new reference to *exporter* and return 0. Otherwise, raise [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError), assign `NULL` to `view->obj`, and return `-1`;

When this function runs inside a [getbufferproc](https://docs.python.org/3.14/c-api/typeobj.html#buffer-structs), point *exporter* at the exporting object (this is mandatory) and relay *flags* without any modification. Otherwise, *exporter* MUST be `NULL`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyobject-checkbuffer-to-pybuffer-fillcontiguousstrides.md)
