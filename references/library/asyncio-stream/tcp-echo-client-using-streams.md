# TCP echo client using streams

### Examples

### TCP echo client using streams

A TCP echo client built on the `asyncio.open_connection()` function:

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

See also

The [TCP echo client protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol) example leans on the low-level [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) method.

[Subject index](INDEX.md) · [Continue](tcp-echo-server-using-streams.md)
