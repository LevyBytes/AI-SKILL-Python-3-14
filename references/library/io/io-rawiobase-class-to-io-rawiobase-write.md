# io / I/O Base Classes: `io.RawIOBase`, `read()`, `readall()`, `readinto()`, `write()`

*class *io.RawIOBase

Base class for raw binary streams. It inherits from `IOBase`.

Raw binary streams generally grant low-level access to an underlying OS device or API, making no effort to wrap it in high-level primitives (that work is handled further up the chain, within buffered binary streams and text streams, both covered later on this page).

Beyond those it gets from `IOBase`, `RawIOBase` adds the following methods:

 read(*size=-1*, */*)

Read as many as *size* bytes from the object and return them. For convenience, when *size* is left out or set to -1, every byte through EOF is returned.

It tries to make just one system call, but it retries when interrupted provided the signal handler raises no exception (the reasoning is laid out in [**PEP 475**](https://peps.python.org/pep-0475/)). As a result, fewer than *size* bytes can come back if the operating system call yields fewer than *size* bytes.

When 0 bytes come back and *size* wasn't 0, that signals end of file. Should the object be in non-blocking mode with no bytes on hand, `None` is returned.

The default implementation defers to `readall()` and `readinto()`.

 readall()

Read every byte from the stream through EOF and return it, making as many calls to the stream as needed.

Getting back `0` bytes means end of file has been reached. Where the object runs in non-blocking mode and the underlying `read()` hands back `None` to signal that no bytes are on hand, `None` is what comes back.

 readinto(*b*, */*)

Read bytes into the pre-allocated, writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b*, and return how many bytes were read. *b* could be a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), for example.

Getting back `0` while `len(b)` is not `0` means end of file has been reached. Where the object runs in non-blocking mode with no bytes on hand, `None` is what comes back.

 write(*b*, */*)

Write the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *b* given to the underlying raw stream, and return how many bytes were written. That count may fall below the byte length of *b*, hinging on the particulars of the underlying raw stream, and most of all if it is in non-blocking mode. `None` comes back if the raw stream is configured not to block and not even one byte could be written to it without delay. After this method returns, the caller is free to release or mutate *b*, so the implementation should touch *b* only while the method runs.

Warning

This function offers no guarantee that all the bytes get written or that an exception is thrown. Callers can supply that behavior by examining the return value and, where it falls below the length of *b*, looping with further write calls until every unwritten byte has been written. Higher-level I/O objects such as Binary I/O and Text I/O take care of retrying for you.

[Subject index](INDEX.md) · [Previous](io-iobase-del.md) · [Continue](io-bufferediobase-class-to-io-bufferediobase-read.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: I/O Base Classes](io-iobase-class.md)
