# io.TextIOBase: `detach()`, `read()`, `readline()`, `seek()`, `tell()`, `write()`

encoding

The name of the encoding applied to turn the stream’s bytes into strings and to turn strings into bytes.

 errors

The error setting belonging to the decoder or encoder.

 newlines

A string, a tuple of strings, or `None`, reporting which newlines have been translated up to now. Whether this is even available hinges on the implementation and on the flags passed to the constructor initially.

 buffer

The backing binary buffer (a `BufferedIOBase` or `RawIOBase` instance) that `TextIOBase` works with. This falls outside the `TextIOBase` API and may be absent from certain implementations.

 detach()

Detach the backing binary buffer from the `TextIOBase` and hand it back.

Once the backing buffer has been detached, the `TextIOBase` enters an unusable state.

Certain `TextIOBase` implementations, `StringIO` being one, may lack the notion of a backing buffer, and calling this method on them will raise `UnsupportedOperation`.

Added in version 3.1.

 read(*size=-1*, */*)

Read and hand back no more than *size* characters from the stream as one [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). When *size* is negative or `None`, reading continues to EOF.

 readline(*size=-1*, */*)

Read up to a newline or EOF and hand back a single [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). When the stream already sits at EOF, an empty string comes back.

When *size* is given, no more than *size* characters get read.

 seek(*offset*, *whence=SEEK_SET*, */*)

Move the stream position to the supplied *offset*. What happens hinges on the *whence* argument, whose default is `SEEK_SET`.

- `SEEK_SET` or `0`: seek relative to the stream’s start (this is the default); *offset* has to be either a number that came from `TextIOBase.tell()` or zero. Supplying any other *offset* gives undefined behaviour.

- `SEEK_CUR` or `1`: “seek” to wherever the position currently is; *offset* has to be zero, which does nothing (every other value is unsupported).

- `SEEK_END` or `2`: seek to the stream’s end; *offset* has to be zero (every other value is unsupported).

Hand back the new absolute position as an opaque number.

Added in version 3.1: The `SEEK_*` constants.

 tell()

Hand back the stream’s current position as an opaque number. Typically this number does not stand for a byte count within the backing binary storage.

 write(*s*, */*)

Write the string *s* into the stream and report how many characters were written.

[Subject index](INDEX.md) · [Previous](io-textiobase-class.md) · [Continue](io-textiowrapper-class-to-io-textiowrapper-reconfigure.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.TextIOBase](io-textiobase-class.md) · [Owning module, declaration or section: Text I/O](io-textiobase-class.md)
