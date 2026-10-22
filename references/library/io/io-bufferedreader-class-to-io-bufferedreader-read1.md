# io / Buffered Streams: `io.BufferedReader`, `peek()`, `read()`, `read1()`

*class *io.BufferedReader(*raw*, *buffer_size=DEFAULT_BUFFER_SIZE*)

A buffered binary stream offering more abstract access to a readable, non seekable `RawIOBase` raw binary stream. It derives from `BufferedIOBase`.

While reading from this object, more data than requested may be pulled from the backing raw stream and stored in an internal buffer. Later reads can then be served straight from that buffered data.

The constructor builds a `BufferedReader` around the supplied readable *raw* stream and *buffer_size*. Leaving *buffer_size* out makes it fall back to `DEFAULT_BUFFER_SIZE`.

Beyond the methods from `BufferedIOBase` and `IOBase`, `BufferedReader` adds or overrides these:

 peek(*size=0*, */*)

Hand back bytes from the stream without moving the position. How many bytes come back may fall short of or exceed the request. Should the backing raw stream be non-blocking and the operation would otherwise block, empty bytes are returned.

 read(*size=-1*, */*)

For `BufferedReader`, this behaves identically to `io.BufferedIOBase.read()`

 read1(*size=-1*, */*)

For `BufferedReader`, this behaves identically to `io.BufferedIOBase.read1()`

Changed in version 3.7: The *size* argument is now optional.

[Subject index](INDEX.md) · [Previous](io-bytesio-getbuffer-to-io-bytesio-readinto1.md) · [Continue](io-bufferedwriter-class-to-io-bufferedwriter-write.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Buffered Streams](io-bytesio-class.md)
