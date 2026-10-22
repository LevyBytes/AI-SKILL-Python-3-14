# Streaming Protocols

### Streaming Protocols

Factories that produce streaming protocols are accepted by event methods such as [`loop.create_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_server), [`loop.create_unix_server()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_server), [`loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection), [`loop.create_unix_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection), [`loop.connect_accepted_socket()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket), [`loop.connect_read_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe), and [`loop.connect_write_pipe()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe).

 Protocol.data_received(*data*)

Called when some data is received. Here *data* is a bytes object, never empty, that carries the arriving data.

How the transport handles the data, whether buffered, chunked, or reassembled, varies by transport. As a rule, don't lean on particular semantics; keep your parsing broad and adaptable instead. That said, the order in which data arrives is always preserved.

While a connection stays open, this method may fire any number of times.

By contrast, `protocol.eof_received()` fires no more than once. After `eof_received()` has fired, `data_received()` fires no further.

 Protocol.eof_received()

Invoked once the peer indicates no further data is coming (say, through a `transport.write_eof()` call, when that peer is likewise on asyncio).

A false value returned here (including `None`) makes the transport close itself. A true value returned here, on the other hand, leaves the close decision up to the protocol in use. Because the default implementation hands back `None`, it closes the connection by implication.

Certain transports, SSL among them, lack support for half-closed connections; for those, returning true from this method causes the connection to be closed.

State machine:

```none
start -> connection_made
    [-> data_received]*
    [-> eof_received]?
-> connection_lost -> end

```

[Subject index](INDEX.md) · [Previous](baseprotocol-connection-made-to-baseprotocol-resume-writing.md) · [Continue](bufferedprotocol-get-buffer-to-bufferedprotocol-eof-received.md)
