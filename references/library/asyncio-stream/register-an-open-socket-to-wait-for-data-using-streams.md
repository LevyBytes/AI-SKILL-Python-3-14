# Register an open socket to wait for data using streams

### Register an open socket to wait for data using streams

A coroutine that holds off until a socket gets data, built on the `open_connection()` function:

```python
import asyncio
import socket

async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()

    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    await writer.wait_closed()

    # Close the second socket
    wsock.close()

asyncio.run(wait_for_data())

```

See also

The [register an open socket to wait for data using a protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-create-connection) example relies on a low-level protocol together with the [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) method.

The [watch a file descriptor for read events](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-example-watch-fd) example turns to the low-level [`loop.add_reader()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.add_reader) method to keep an eye on a file descriptor.

[Subject index](INDEX.md) · [Previous](get-http-headers.md)
