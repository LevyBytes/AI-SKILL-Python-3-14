# multiprocessing: `multiprocessing.ProcessError`, `multiprocessing.BufferTooShort`, `multiprocessing.AuthenticationError`, `multiprocessing.TimeoutError`

*exception *multiprocessing.ProcessError

The parent class from which every `multiprocessing` exception derives.

 *exception *multiprocessing.BufferTooShort

The exception that `Connection.recv_bytes_into()` raises whenever the buffer object handed in is too small to hold the message being read.

When `e` is a `BufferTooShort` instance, `e.args[0]` yields the message as a byte string.

 *exception *multiprocessing.AuthenticationError

The exception raised upon an authentication error.

 *exception *multiprocessing.TimeoutError

The exception raised by timeout-bearing methods once the timeout runs out.

[Subject index](INDEX.md) · [Previous](process-interrupt-terminate-kill-and-close.md) · [Continue](multiprocessing-pipe.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: `Process` and exceptions](multiprocessing-process-class.md)
