# typing — ABCs and Protocols for working with I/O

### ABCs and Protocols for working with I/O

 *class *typing.IO[*AnyStr*]

 *class *typing.TextIO

 *class *typing.BinaryIO

The generic class `IO[AnyStr]` together with its subclasses `TextIO(IO[str])` and `BinaryIO(IO[bytes])` model the types of I/O streams like the one [`open()`](https://docs.python.org/3.14/library/functions.html#open) returns. Be aware that these are not protocols, and the interface they expose is rather broad.

[Subject index](INDEX.md) · [Previous](typing-supportsround-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Required continuation of the source contract](typing-io-typing-textio-and-typing-binaryio-interfaces.md)
