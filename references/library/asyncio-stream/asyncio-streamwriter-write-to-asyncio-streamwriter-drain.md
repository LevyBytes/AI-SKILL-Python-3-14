# StreamWriter: `write()`, `writelines()`, `close()`, `can_write_eof()`, `write_eof()`, `get_extra_info()`, `drain()`

`write(*data*)`

This method tries to push the *data* straight onto the underlying socket. When that doesn't go through, the data waits in an internal write buffer until it can leave.

The *data* buffer ought to be a bytes, bytearray, or C-contiguous one-dimensional memoryview object.

Pair this method with the `drain()` method:

```python
stream.write(data)
await stream.drain()

```

 `writelines(*data*)`

This method pushes a list (or any iterable) of bytes straight onto the underlying socket. When that doesn't go through, the data waits in an internal write buffer until it can leave.

Pair this method with the `drain()` method:

```python
stream.writelines(lines)
await stream.drain()

```

 close()

This method shuts the stream together with the underlying socket.

Although not required, this method is best paired with the `wait_closed()` method:

```python
stream.close()
await stream.wait_closed()

```

 can_write_eof()

Return `True` when the underlying transport offers the `write_eof()` method, and `False` if it does not.

 write_eof()

Shut the write side of the stream once the buffered write data has been flushed.

 transport

Hand back the underlying asyncio transport.

 `get_extra_info(*name*, *default=None*)`

Reach optional transport information; consult [`BaseTransport.get_extra_info()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info) for specifics.

 `*async *drain()`

Hold off until resuming writes to the stream is appropriate. Example:

```python
writer.write(data)
await writer.drain()

```

It serves as a flow-control method that works against the underlying IO write buffer. Once the buffer's size hits the high watermark, *drain()* blocks until the buffer has been drained back down to the low watermark and writes may resume. With nothing to wait on, `drain()` comes back right away.

[Subject index](INDEX.md) · [Previous](asyncio-streamwriter-class.md) · [Continue](stream-writer-tls-and-close-lifecycle.md) · [Owning module, declaration or section: asyncio.StreamWriter](asyncio-streamwriter-class.md) · [Owning module, declaration or section: StreamWriter](asyncio-streamwriter-class.md)
