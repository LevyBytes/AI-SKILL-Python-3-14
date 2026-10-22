# asyncio.eventloop: `loop.add_signal_handler()`

### Unix signals

 loop.add_signal_handler(*signum*, *callback*, **args*)

Install *callback* to handle the *signum* signal, forwarding *args* along as positional arguments.

[Subject index](INDEX.md) · [Previous](loop-connect-read-pipe-to-loop-connect-write-pipe.md) · [Required continuation of the source contract](loop-remove-signal-handler.md)
