# asyncio.protocol: `SubprocessProtocol.pipe_data_received()`, `SubprocessProtocol.pipe_connection_lost()`

### Subprocess Protocols

The protocol factories handed to the [`loop.subprocess_exec()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec) and [`loop.subprocess_shell()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell) methods are what should build Subprocess Protocol instances.

 SubprocessProtocol.pipe_data_received(*fd*, *data*)

Invoked whenever the child process emits data on its stdout or stderr pipe.

*fd* is the integer file descriptor of the pipe.

*data* is a non-empty bytes object containing the received data.

 SubprocessProtocol.pipe_connection_lost(*fd*, *exc*)

Invoked once one of the pipes used to talk with the child process gets closed.

[Subject index](INDEX.md) · [Previous](datagram-protocol-receive-and-error-callbacks.md) · [Required continuation of the source contract](subprocessprotocol-process-exited.md)
