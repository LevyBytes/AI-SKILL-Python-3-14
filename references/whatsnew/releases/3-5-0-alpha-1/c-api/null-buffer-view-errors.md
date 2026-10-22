# Python 3.5.0 alpha 1 / c api / null buffer view errors

[bpo-14203](https://bugs.python.org/issue?@action=redirect&bpo=14203): Dropped the outdated handling of view==NULL across PyBuffer_FillInfo(), bytearray_getbuffer(), bytesiobuf_getbuffer() and array_buffer_getbuf(). Each of these now signals BufferError in that situation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
