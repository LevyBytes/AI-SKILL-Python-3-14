# TCP echo server using streams

### TCP echo server using streams

A TCP echo server built on the `asyncio.start_server()` function:

```python
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

```

See also

The [TCP echo server protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-tcp-echo-server-protocol) example draws on the [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server) method.

[Subject index](INDEX.md) · [Previous](tcp-echo-client-using-streams.md) · [Continue](get-http-headers.md)
