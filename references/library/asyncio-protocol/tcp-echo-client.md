# TCP Echo Client

### TCP Echo Client

A TCP echo client built on the [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) method, which sends data and then waits for the connection to close:

```python
import asyncio

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())

```

See also

The high-level [`asyncio.open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection) function powers the [TCP echo client using streams](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-tcp-echo-client-streams) example.

[Subject index](INDEX.md) · [Previous](tcp-echo-server.md) · [Continue](udp-echo-server.md)
