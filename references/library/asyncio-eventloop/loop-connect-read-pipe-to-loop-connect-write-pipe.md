# Working with pipes

### Working with pipes

 *async *loop.connect_read_pipe(*protocol_factory*, *pipe*)

Register the read end of *pipe* in the event loop.

*protocol_factory* must be a callable returning an [asyncio protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

*pipe* is a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-object).

Hand back a `(transport, protocol)` pair in which *transport* honors the [`ReadTransport`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.ReadTransport) interface while *protocol* names an object that the *protocol_factory* instantiated.

With `SelectorEventLoop` event loop, the *pipe* is set to non-blocking mode.

 *async *loop.connect_write_pipe(*protocol_factory*, *pipe*)

Register the write end of *pipe* in the event loop.

*protocol_factory* must be a callable returning an [asyncio protocol](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-protocol) implementation.

*pipe* is [file-like object](https://docs.python.org/3.14/glossary.html#term-file-object).

Hand back a `(transport, protocol)` pair in which *transport* honors the [`WriteTransport`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport) interface while *protocol* names an object that the *protocol_factory* instantiated.

With `SelectorEventLoop` event loop, the *pipe* is set to non-blocking mode.

Note

`SelectorEventLoop` does not support the above methods on Windows. Use `ProactorEventLoop` instead for Windows.

See also

The `loop.subprocess_exec()` and `loop.subprocess_shell()` methods.

[Subject index](INDEX.md) · [Previous](loop-getaddrinfo-to-loop-getnameinfo.md) · [Continue](loop-add-signal-handler.md)
