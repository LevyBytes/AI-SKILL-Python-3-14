# asyncio.protocol: `asyncio.Transport`

*class *asyncio.Transport(*WriteTransport*, *ReadTransport*)

Interface representing a bidirectional transport, such as a TCP connection.

Rather than constructing a transport on their own, the user calls a helper function and supplies a protocol factory along with whatever else is needed to build both the transport and the protocol.

Event loop methods such as [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection), [`loop.create_unix_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection), [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server), [`loop.sendfile()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.sendfile), and the like return or make use of *Transport* class instances.

[Subject index](INDEX.md) · [Previous](asyncio-readtransport-class.md) · [Continue](asyncio-datagramtransport-class.md) · [Owning module, declaration or section: Transports Hierarchy](asyncio-basetransport-class.md)
