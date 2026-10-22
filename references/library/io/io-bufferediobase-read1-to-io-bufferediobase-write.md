# io.BufferedIOBase: `read1()`, `readinto()`, `readinto1()`, `write()`

If the backing raw stream operates in non-blocking mode, an implementation is free to either signal [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) or hand back `None` when nothing is ready to read. The `io` implementations choose to return `None`.

 read1(*size=-1*, */*)

Fetch and hand back as many as *size* bytes by invoking `readinto()`, which is permitted to retry should [`EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR) occur, in accordance with [**PEP 475**](https://peps.python.org/pep-0475/). Should *size* be `-1` or left unspecified, the implementation picks some value for *size* on its own.

Note

If the backing raw stream operates in non-blocking mode, an implementation is free to either signal [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) or hand back `None` when nothing is ready to read. The `io` implementations choose to return `None`.

 readinto(*b*, */*)

Pull bytes into a writable, already-allocated [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b*, then report how many bytes were read. As an illustration, *b* could be a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

As with `read()`, the underlying raw stream may receive several reads, except where that stream happens to be interactive.

When the backing raw stream sits in non blocking-mode and currently holds no available data, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) gets raised.

 readinto1(*b*, */*)

Pull bytes into a writable, already-allocated [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b*, limited to a single invocation of the backing raw stream’s `read()` (or `readinto()`) method. Report how many bytes were read.

When the backing raw stream sits in non blocking-mode and currently holds no available data, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) gets raised.

Added in version 3.5.

 write(*b*, */*)

Write out the supplied [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), *b*, and report how many bytes were written (this always matches the byte length of *b*, because any failed write triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError)). Whether those bytes go straight to the backing stream or sit in a buffer for the sake of throughput and latency depends on the particular implementation.

Under non-blocking mode, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) is raised whenever the data had to reach the raw stream yet the stream couldn’t take all of it without blocking.

Once this method has returned, the caller is free to free or alter *b*, so the implementation ought to touch *b* solely while the call is running.

[Subject index](INDEX.md) · [Continue](io-fileio-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.BufferedIOBase](io-bufferediobase-class-to-io-bufferediobase-read.md) · [Owning module, declaration or section: I/O Base Classes](io-iobase-class.md) · [Owning module, declaration or section: read](io-bufferediobase-class-to-io-bufferediobase-read.md) · [Preceding source contract and version conditions](io-bufferediobase-class-to-io-bufferediobase-read.md)
