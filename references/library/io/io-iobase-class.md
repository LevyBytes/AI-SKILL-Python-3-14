# io: `io.IOBase`

### I/O Base Classes

 *class *io.IOBase

The abstract base class for all I/O classes.

This class supplies empty abstract implementations of many methods that subclasses may selectively override; those defaults stand for a file that cannot be read, written, or seeked.

Although `IOBase` declares neither `read()` nor `write()` (since their signatures differ), implementations and clients ought to regard those methods as part of the interface. On top of that, an implementation may throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) (or `UnsupportedOperation`) once an operation it lacks support for gets invoked.

The fundamental type for binary data read from or written to a file is [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Method arguments may also be other [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Text I/O classes operate on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) data.

Bear in mind that invoking any method — even an inquiry — on a closed stream has undefined behavior. In that situation, implementations may raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Both `IOBase` and its subclasses honor the iterator protocol, so iterating over an `IOBase` object yields the stream's lines one by one. Precisely what counts as a line varies a little depending on whether the stream is a binary one (yielding bytes) or a text one (yielding character strings). See `readline()` below.

`IOBase` doubles as a context manager and thus supports the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. In the example that follows, *file* gets closed once the suite of the `with` statement completes — even should an exception arise:

```python
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')

```

The data attributes and methods that `IOBase` offers are these:

[Subject index](INDEX.md) · [Previous](class-hierarchy.md) · [Continue](io-iobase-close-to-io-iobase-writelines.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
