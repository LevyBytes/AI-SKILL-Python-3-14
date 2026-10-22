# io / Static Typing: `write()`

*class *io.Writer[*T*]

A generic protocol for writing to a file or another output stream. `T` is most often [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), but it may be whatever type can be written to the stream.

Added in version 3.14.

 write(*data*, */*)

Write *data* into the output stream and report how many items (bytes/characters) were written.

For example:

```python
def write_binary(writer: Writer[bytes]):
    writer.write(b"Hello world!\n")

```

Consult [ABCs and Protocols for working with I/O](https://docs.python.org/3.14/library/typing.html#typing-io) for further I/O-related protocols and classes usable in static type checking.

[Subject index](INDEX.md) · [Previous](io-reader-read-to-io-reader-read.md) · [Continue](performance.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Static Typing](static-typing.md)
