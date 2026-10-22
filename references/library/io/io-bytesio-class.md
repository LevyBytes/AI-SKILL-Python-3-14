# io: `io.BytesIO`

### Buffered Streams

Compared with raw I/O, buffered I/O streams expose a more abstract interface to an I/O device.

 *class *io.BytesIO(*initial_bytes=b''*)

A binary stream backed by an in-memory bytes buffer. It derives from `BufferedIOBase`. Calling the `close()` method throws the buffer away.

The optional *initial_bytes* argument is a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) holding the starting data.

Beyond the methods from `BufferedIOBase` and `IOBase`, `BytesIO` adds or overrides these:

[Subject index](INDEX.md) · [Previous](raw-file-i-o.md) · [Continue](io-bytesio-getbuffer-to-io-bytesio-readinto1.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
