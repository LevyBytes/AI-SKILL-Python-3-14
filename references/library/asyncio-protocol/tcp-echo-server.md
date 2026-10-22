# TCP Echo Server

### Examples

### TCP Echo Server

Build a TCP echo server with the [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) method, echo back whatever data arrives, then drop the connection:

```python
import asyncio

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        EchoServerProtocol,
        '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())

```

See also

The high-level [`asyncio.start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server) function powers the [TCP echo server using streams](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-tcp-echo-server-streams) example.

[Subject index](INDEX.md) · [Continue](tcp-echo-client.md)
