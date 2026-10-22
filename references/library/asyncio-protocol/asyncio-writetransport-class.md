# asyncio.protocol: `asyncio.WriteTransport`

*class *asyncio.WriteTransport(*BaseTransport*)

A base transport for write-only connections.

The [`loop.connect_write_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe) event loop method hands back instances of the *WriteTransport* class, and subprocess-related methods such as [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) rely on them too.

[Subject index](INDEX.md) · [Previous](asyncio-basetransport-class.md) · [Continue](asyncio-readtransport-class.md) · [Owning module, declaration or section: Transports Hierarchy](asyncio-basetransport-class.md)
