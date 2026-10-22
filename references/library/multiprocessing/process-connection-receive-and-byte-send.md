# multiprocessing / Connection Objects: `recv()`, `fileno()`, `close()`, `poll()`, `send_bytes()`

recv()

Give back an object that the far end of the connection sent via `send()`. Blocks until something arrives to receive. Raises [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError) when nothing remains to receive and the far end has closed.

 fileno()

Give back the file descriptor or handle the connection uses.

 close()

Close the connection.

This runs automatically once the connection is garbage collected.

 poll([*timeout*])

Report whether any data is on hand to be read.

When *timeout* is not given, it returns at once. When *timeout* is a number, it sets the longest time in seconds to block. When *timeout* is `None`, an infinite timeout applies.

Be aware that several connection objects can be polled together by using `multiprocessing.connection.wait()`.

 send_bytes(*buf*[, *offset*[, *size*]])

Send byte data from a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) as a complete message.

[Subject index](INDEX.md) · [Previous](multiprocessing-connection-connection-class-to-send.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.connection.Connection; send](multiprocessing-connection-connection-class-to-send.md) · [Owning module, declaration or section: Connection Objects](multiprocessing-connection-connection-class-to-send.md) · [Required continuation of the source contract](connection-byte-receive-methods.md)
