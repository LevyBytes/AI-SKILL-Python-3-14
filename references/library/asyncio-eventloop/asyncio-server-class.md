# asyncio.eventloop: `asyncio.Server`

### Server objects

The functions `loop.create_server()`, `loop.create_unix_server()`, [`start_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_server), and [`start_unix_server()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.start_unix_server) are what create Server objects.

Do not instantiate the `Server` class directly.

 *class *asyncio.Server

*Server* objects act as asynchronous context managers. Used within an `async with` statement, the Server object is guaranteed to be closed and to have stopped taking new connections by the time that `async with` statement finishes:

```python
srv = await loop.create_server(...)

async with srv:
    # some code

# At this point, srv is closed and no longer accepts new connections.

```

Changed in version 3.7: Starting with Python 3.7, the Server object behaves as an asynchronous context manager.

Changed in version 3.11: This class was exposed publicly as `asyncio.Server` in Python 3.9.11, 3.10.3 and 3.11.

[Subject index](INDEX.md) · [Previous](asyncio-timerhandle-class-to-asyncio-timerhandle-when.md) · [Continue](asyncio-server-close-to-asyncio-server-wait-closed.md)
