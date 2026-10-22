# io: Reader and Writer typing protocols

### Static Typing

Use the protocols below to annotate the arguments of functions and methods doing straightforward stream reading or writing. They carry the [`@typing.runtime_checkable`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) decorator.

 *class *io.Reader[*T*]

A generic protocol for reading from a file or another input stream. `T` is most often [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), but it may be whatever type is read off the stream.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](io-incrementalnewlinedecoder-class.md) · [Continue](io-reader-read-to-io-reader-read.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
