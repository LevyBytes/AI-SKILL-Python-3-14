# asyncio.protocol: `SubprocessProtocol.process_exited()`

*fd* is the integer file descriptor that got closed.

 SubprocessProtocol.process_exited()

Invoked once the child process has terminated.

It may run ahead of the `pipe_data_received()` and `pipe_connection_lost()` methods.

[Subject index](INDEX.md) · [Continue](tcp-echo-server.md) · [Owning module, declaration or section: Subprocess Protocols](subprocess-protocol-pipe-callbacks.md) · [Owning module, declaration or section: SubprocessProtocol.pipe_connection_lost](subprocess-protocol-pipe-callbacks.md) · [Preceding source contract and version conditions](subprocess-protocol-pipe-callbacks.md)
