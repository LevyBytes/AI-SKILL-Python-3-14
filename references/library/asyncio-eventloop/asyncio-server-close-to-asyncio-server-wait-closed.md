# asyncio.eventloop: `close()`, `close_clients()`, `abort_clients()`, `get_loop()`, `start_serving()`, `serve_forever()`, `is_serving()`, `wait_closed()`

close()

Halt serving: shut the listening sockets and reset the `sockets` attribute to `None`.

Sockets standing for client connections already accepted stay open.

Closing happens asynchronously; await the `wait_closed()` coroutine to block until the server has fully closed (with no remaining active connections).

 close_clients()

Close all existing incoming client connections.

Calls [`close()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.BaseTransport.close) on all associated transports.

To steer clear of races with newly arriving clients, call `close()` ahead of `close_clients()` while shutting the server down.

Added in version 3.13.

 abort_clients()

Tear down all current incoming client connections at once, not pausing for any in-flight operations to finish.

Calls [`abort()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.abort) on all associated transports.

To steer clear of races with newly arriving clients, call `close()` ahead of `abort_clients()` while shutting the server down.

Added in version 3.13.

 get_loop()

Return the event loop associated with the server object.

Added in version 3.7.

 *async *start_serving()

Begin taking connections.

The method is idempotent, so calling it while the server already serves is harmless.

The *start_serving* keyword-only parameter on `loop.create_server()` and [`asyncio.start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server) lets you build a Server object that does not accept connections right away. Then `Server.start_serving()` or `Server.serve_forever()` can be used to get the Server taking connections.

Added in version 3.7.

 *async *serve_forever()

Keep taking connections until the coroutine is cancelled. Cancelling a `serve_forever` task drives the server to close.

You may call this even while the server already accepts connections. At most one `serve_forever` task is allowed for each *Server* object.

Example:

```python
async def client_connected(reader, writer):
    # Communicate with the client with
    # reader/writer streams.  For example:
    await reader.readline()

async def main(host, port):
    srv = await asyncio.start_server(
        client_connected, host, port)
    await srv.serve_forever()

asyncio.run(main('127.0.0.1', 0))

```

Added in version 3.7.

 is_serving()

Return `True` if the server is accepting new connections.

Added in version 3.7.

 *async *wait_closed()

Block until the `close()` method has run to completion and every active connection has wrapped up.

[Subject index](INDEX.md) · [Previous](asyncio-server-class.md) · [Continue](server-objects.md) · [Owning module, declaration or section: asyncio.Server](asyncio-server-class.md) · [Owning module, declaration or section: Server objects](asyncio-server-class.md)
