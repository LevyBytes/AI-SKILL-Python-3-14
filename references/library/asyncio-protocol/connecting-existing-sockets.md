# Connecting Existing Sockets

### Connecting Existing Sockets

Block until a socket gets data by pairing the [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) method with a protocol:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/asyncio-protocol.html#connecting-existing-sockets).

See also

To register an FD, the [watch a file descriptor for read events](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-watch-fd) example calls the low-level [`loop.add_reader()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_reader) method.

Inside a coroutine, the [register an open socket to wait for data using streams](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-example-create-connection-streams) example relies on high-level streams produced by the [`open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection) function.

[Subject index](INDEX.md) · [Previous](udp-echo-client.md) · [Continue](loop-subprocess-exec-and-subprocessprotocol.md)
