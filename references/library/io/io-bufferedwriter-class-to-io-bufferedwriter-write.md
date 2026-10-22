# io / Buffered Streams: `io.BufferedWriter`, `flush()`, `write()`

*class *io.BufferedWriter(*raw*, *buffer_size=DEFAULT_BUFFER_SIZE*)

A buffered binary stream offering more abstract access to a writeable, non seekable `RawIOBase` raw binary stream. It derives from `BufferedIOBase`.

When writing to this object, the data ordinarily lands in an internal buffer first. That buffer gets flushed out to the backing `RawIOBase` object in several situations, such as:

- when the buffer no longer has room for all the pending data;

- when `flush()` is invoked;

- when a `seek()` is asked for (in the case of `BufferedRandom` objects);

- when the `BufferedWriter` object is closed or destroyed.

The constructor builds a `BufferedWriter` around the supplied writeable *raw* stream. When *buffer_size* is not provided, it falls back to `DEFAULT_BUFFER_SIZE`.

Beyond the methods from `BufferedIOBase` and `IOBase`, `BufferedWriter` adds or overrides these:

 flush()

Push the bytes sitting in the buffer out into the raw stream. A [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) should be raised whenever the raw stream blocks.

 write(*b*, */*)

Write out the [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), *b*, and report how many bytes were written. Under non-blocking mode, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) carrying [`BlockingIOError.characters_written`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError.characters_written) is raised when the buffer has to be flushed out yet the raw stream blocks.

[Subject index](INDEX.md) · [Previous](io-bufferedreader-class-to-io-bufferedreader-read1.md) · [Continue](io-bufferedrandom-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Buffered Streams](io-bytesio-class.md)
