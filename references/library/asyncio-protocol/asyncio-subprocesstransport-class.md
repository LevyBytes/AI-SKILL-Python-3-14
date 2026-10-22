# asyncio.protocol: `asyncio.SubprocessTransport`

*class *asyncio.SubprocessTransport(*BaseTransport*)

An abstraction standing in for the link between a parent process and the child OS process it spawned.

The event loop methods [`loop.subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell) and [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) hand back instances of the *SubprocessTransport* class.

[Subject index](INDEX.md) · [Previous](asyncio-datagramtransport-class.md) · [Continue](basetransport-close-to-basetransport-is-closing.md) · [Owning module, declaration or section: Transports Hierarchy](asyncio-basetransport-class.md)
