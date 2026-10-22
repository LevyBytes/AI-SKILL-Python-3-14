# io / I/O Base Classes: `io.BufferedIOBase`, `detach()`, `read()`

*class *io.BufferedIOBase

Base class for binary streams that provide buffering of some form. Its parent is `IOBase`.

What chiefly sets it apart from `RawIOBase` is that the methods `read()`, `readinto()` and `write()` will each strive (respectively) to read as much input as was asked for or to put out every byte of supplied data.

On top of that, when the underlying raw stream is in non-blocking mode and the system reports would block, `write()` will raise [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) carrying [`BlockingIOError.characters_written`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError.characters_written), and `read()` will give back the data read up to that point or `None` when none is available.

What's more, the `read()` method lacks a default implementation that falls back to `readinto()`.

A typical `BufferedIOBase` implementation should not subclass a `RawIOBase` implementation; instead it should wrap one, in the manner of `BufferedWriter` and `BufferedReader`.

On top of what `IOBase` offers, `BufferedIOBase` supplies or overrides the following data attributes and methods:

 raw

The underlying raw stream (a `RawIOBase` instance) that `BufferedIOBase` works with. This isn't part of the `BufferedIOBase` API, and certain implementations may not have it.

 detach()

Detach the underlying raw stream from the buffer and return it.

Once the raw stream has been detached, the buffer is left unusable.

Certain buffers, `BytesIO` among them, have no notion of a single raw stream to hand back from this method. They raise `UnsupportedOperation`.

Added in version 3.1.

 read(*size=-1*, */*)

Read and return as many as *size* bytes. When the argument is left out, `None`, or negative, read as much as you can.

The bytes returned may number fewer than requested. When the stream already sits at EOF, an empty [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object comes back. More than a single read can occur, and calls may be retried upon hitting certain errors — see [`os.read()`](https://docs.python.org/3.14/library/os.html#os.read) and [**PEP 475**](https://peps.python.org/pep-0475/) for the details. Returning fewer than size bytes carries no implication that EOF is near.

While reading as much as possible, the default implementation turns to `raw.readall` where it exists (which should implement `RawIOBase.readall()`); otherwise it reads in a loop until read yields `None`, an empty [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), or a non-retryable error. For most streams that point is EOF, though non-blocking streams may see further data become available.

Note

[Subject index](INDEX.md) · [Previous](io-rawiobase-class-to-io-rawiobase-write.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: I/O Base Classes](io-iobase-class.md) · [Required continuation of the source contract](io-bufferediobase-read1-to-io-bufferediobase-write.md)
