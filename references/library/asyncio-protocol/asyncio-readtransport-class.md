# asyncio.protocol: `asyncio.ReadTransport`

*class *asyncio.ReadTransport(*BaseTransport*)

A base transport for read-only connections.

The [`loop.connect_read_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe) event loop method hands back instances of the *ReadTransport* class, and subprocess-related methods such as [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) rely on them too.

[Subject index](INDEX.md) · [Previous](asyncio-writetransport-class.md) · [Continue](asyncio-transport-class.md) · [Owning module, declaration or section: Transports Hierarchy](asyncio-basetransport-class.md)
