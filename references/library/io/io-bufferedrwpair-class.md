# io: `io.BufferedRWPair`

*class *io.BufferedRWPair(*reader*, *writer*, *buffer_size=DEFAULT_BUFFER_SIZE*, */*)

A buffered binary stream offering more abstract access to a pair of non seekable `RawIOBase` raw binary streams—one of them readable and the other writeable. It derives from `BufferedIOBase`.

*reader* and *writer* are `RawIOBase` objects that are, respectively, readable and writeable. Should *buffer_size* be left out, it falls back to `DEFAULT_BUFFER_SIZE`.

`BufferedRWPair` realizes every one of `BufferedIOBase`'s methods apart from `detach()`, which raises `UnsupportedOperation`.

Warning

`BufferedRWPair` makes no effort to coordinate accesses to its backing raw streams. Avoid handing it one and the same object for both reader and writer; turn to `BufferedRandom` for that.

[Subject index](INDEX.md) · [Previous](io-bufferedrandom-class.md) · [Continue](io-textiobase-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Buffered Streams](io-bytesio-class.md)
