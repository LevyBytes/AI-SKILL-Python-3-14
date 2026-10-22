# Streams: `asyncio.open_connection()`

# Asyncio Stream

### Streams

**Source code:** [Lib/asyncio/streams.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/streams.py)

---

For dealing with network connections, streams offer high-level primitives that are ready for async/await. They let you send and receive data while steering clear of callbacks and of the low-level protocols and transports.

What follows is a TCP echo client built on top of asyncio streams:

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))

```

Have a look as well at the Examples section further down.

Stream Functions

To build and operate on streams, you can reach for the top-level asyncio functions listed here:

 `*async *asyncio.open_connection(*host=None*, *port=None*, ***, *limit=None*, *ssl=None*, *family=0*, *proto=0*, *flags=0*, *sock=None*, *local_addr=None*, *server_hostname=None*, *ssl_handshake_timeout=None*, *ssl_shutdown_timeout=None*, *happy_eyeballs_delay=None*, *interleave=None*)`

Open a network connection and give back a `(reader, writer)` object pair.

Those returned *reader* and *writer* objects are instances of the `StreamReader` and `StreamWriter` classes.

The buffer size cap applied by the returned `StreamReader` instance is set by *limit*. Absent any value, that *limit* defaults to 64 KiB.

Every remaining argument is forwarded as-is to [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection).

Note

Passing the *sock* argument hands ownership of the socket over to the `StreamWriter` that gets created. Closing the socket is done by calling its `close()` method.

Changed in version 3.7: Added the *ssl_handshake_timeout* parameter.

Changed in version 3.8: Added the *happy_eyeballs_delay* and *interleave* parameters.

Changed in version 3.10: Removed the *loop* parameter.

Changed in version 3.11: Added the *ssl_shutdown_timeout* parameter.

[Subject index](INDEX.md) · [Continue](asyncio-start-server-to-asyncio-start-unix-server.md)
