# multiprocessing / Connection Objects: `multiprocessing.connection.Connection`, `send()`

### Connection Objects

Connection objects let you send and receive picklable objects or strings. Think of them as message-oriented connected sockets.

Connection objects normally come from `Pipe` — see also Listeners and Clients.

 *class *multiprocessing.connection.Connection

 send(*obj*)

Send an object to the far end of the connection, where it should be read using `recv()`.

The object has to be picklable. Pickles that are very large (roughly 32 MiB+, though it hinges on the OS) may raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

[Subject index](INDEX.md) · [Previous](process-executable-and-start-method-configuration.md) · [Continue](process-connection-receive-and-byte-send.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
