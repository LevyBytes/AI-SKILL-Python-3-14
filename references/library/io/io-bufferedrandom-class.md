# io: `io.BufferedRandom`

*class *io.BufferedRandom(*raw*, *buffer_size=DEFAULT_BUFFER_SIZE*)

A buffered binary stream that realizes the `BufferedIOBase` interfaces, offering more abstract access to a seekable `RawIOBase` raw binary stream.

The constructor builds a reader and a writer around a seekable raw stream passed as the first argument. Should *buffer_size* be left out, it falls back to `DEFAULT_BUFFER_SIZE`.

Everything `BufferedReader` or `BufferedWriter` can do, `BufferedRandom` can do as well. On top of that, `seek()` and `tell()` are guaranteed to be present.

[Subject index](INDEX.md) · [Previous](io-bufferedwriter-class-to-io-bufferedwriter-write.md) · [Continue](io-bufferedrwpair-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Buffered Streams](io-bytesio-class.md)
