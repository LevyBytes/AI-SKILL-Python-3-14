# multiprocessing / Connection Objects: `recv_bytes()`, `recv_bytes_into()`

When *offset* is supplied, reading starts at that position within *buf*. When *size* is supplied, exactly that many bytes are read out of *buf*. Buffers that are very large (roughly 32 MiB+, though it hinges on the OS) may raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception

 recv_bytes([*maxlength*])

Give back, as a string, a complete byte-data message that the far end of the connection sent. Blocks until something arrives to receive. Raises [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError) when nothing remains to receive and the far end has closed.

Should *maxlength* be supplied and the message run longer than *maxlength*, then [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised and reading from the connection becomes impossible.

Changed in version 3.3: Formerly this function raised [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), by now an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 recv_bytes_into(*buf*[, *offset*])

Read into *buf* a complete byte-data message that the far end of the connection sent, then give back the message's byte count. Blocks until something arrives to receive. Raises [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError) when nothing remains to receive and the far end was closed.

*buf* has to be a writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). When *offset* is supplied, the message lands in the buffer starting at that position. Offset must be a non-negative integer below the length of *buf* (counted in bytes).

When the buffer falls short, a `BufferTooShort` exception is raised, with the full message reachable as `e.args[0]` where `e` is that exception instance.

Changed in version 3.3: Passing connection objects themselves across processes is now possible via `Connection.send()` and `Connection.recv()`.

Connection objects have also gained context-management-protocol support – see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) returns the connection object, while [`__exit__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__exit__) calls `close()`.

For example:

```pycon
>>> from multiprocessing import Pipe
>>> a, b = Pipe()
>>> a.send([1, 'hello', None])
>>> b.recv()
[1, 'hello', None]
>>> b.send_bytes(b'thank you')
>>> a.recv_bytes()
b'thank you'
>>> import array
>>> arr1 = array.array('i', range(5))
>>> arr2 = array.array('i', [0] * 10)
>>> a.send_bytes(arr1)
>>> count = b.recv_bytes_into(arr2)
>>> assert count == len(arr1) * arr1.itemsize
>>> arr2
array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])

```

Warning

The `Connection.recv()` method unpickles whatever data it gets on its own, and that can pose a security risk unless the process that sent the message is trustworthy.

For that reason, unless the connection object came from `Pipe()`, you ought to use the `recv()` and `send()` methods only once some form of authentication has been done. See Authentication keys.

Warning

When a process is killed midway through reading from or writing to a pipe, the pipe's data is apt to end up corrupted, since it may turn out impossible to know for sure where the message boundaries fall.

[Subject index](INDEX.md) · [Continue](multiprocessing-barrier-class.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.connection.Connection; send](multiprocessing-connection-connection-class-to-send.md) · [Owning module, declaration or section: Connection Objects](multiprocessing-connection-connection-class-to-send.md) · [Owning module, declaration or section: send_bytes](process-connection-receive-and-byte-send.md) · [Preceding source contract and version conditions](process-connection-receive-and-byte-send.md)
