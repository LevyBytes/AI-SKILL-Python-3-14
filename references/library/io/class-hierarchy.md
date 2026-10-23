# io - Class hierarchy

### Class hierarchy

The I/O stream implementation is laid out as a hierarchy of classes. It begins with [abstract base classes](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) (ABCs) that pin down the several stream categories, followed by concrete classes that supply the standard stream implementations.

Note

To ease the writing of concrete stream classes, the abstract base classes additionally supply default implementations for a number of methods. For instance, `BufferedIOBase` ships unoptimized implementations of `readinto()` and `readline()`.

The abstract base class `IOBase` sits at the apex of the I/O hierarchy. It lays out a stream's fundamental interface. Be aware, though, that reading and writing aren't kept separate; an implementation may raise `UnsupportedOperation` whenever it lacks support for a given operation.

`IOBase` is extended by the `RawIOBase` ABC. It handles reading bytes from and writing bytes to a stream. By subclassing `RawIOBase`, `FileIO` exposes an interface to files within the machine's file system.

`IOBase` is also extended by the `BufferedIOBase` ABC. It handles buffering layered over a raw binary stream (`RawIOBase`). The subclasses `BufferedWriter`, `BufferedReader`, and `BufferedRWPair` add buffering to raw binary streams that are, respectively, writable, readable, and both readable and writable. A buffered interface to seekable streams comes from `BufferedRandom`. One more `BufferedIOBase` subclass, `BytesIO`, is a stream of in-memory bytes.

`IOBase` is extended as well by the `TextIOBase` ABC. It handles streams whose bytes stand for text, taking care of encoding to and decoding from strings. Extending `TextIOBase`, `TextIOWrapper` offers a buffered text interface over a buffered raw stream (`BufferedIOBase`). And lastly, `StringIO` is an in-memory text stream.

Argument names fall outside the specification, and only [`open()`](https://docs.python.org/3.14/library/functions.html#open)'s arguments are meant to be passed as keyword arguments.

Here is a table summarizing the ABCs that the `io` module supplies:

| ABC | Inherits | Stub Methods | Mixin Methods and Properties |
| --- | --- | --- | --- |
| `IOBase` |  | `fileno`, `seek`, and `truncate` | `close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable`, and `writelines` |
| `RawIOBase` | `IOBase` | `readinto` and `write` | Inherited `IOBase` methods, `read`, and `readall` |
| `BufferedIOBase` | `IOBase` | `detach`, `read`, `read1`, and `write` | Inherited `IOBase` methods, `readinto`, and `readinto1` |
| `TextIOBase` | `IOBase` | `detach`, `read`, `readline`, and `write` | Inherited `IOBase` methods, `encoding`, `errors`, and `newlines` |

[Subject index](INDEX.md) · [Previous](io-default-buffer-size-to-io-unsupportedoperation.md) · [Continue](io-iobase-class.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
