# typing — typing.IO, typing.TextIO and typing.BinaryIO interfaces

For situations where only the `read()` method or only the `write()` method is used, the protocols [`io.Reader`](https://docs.python.org/3.14/library/io.html#io.Reader) and [`io.Writer`](https://docs.python.org/3.14/library/io.html#io.Writer) provide a lighter-weight way to annotate the respective arguments:

```python
def read_and_write(reader: Reader[str], writer: Writer[bytes]):
    data = reader.read()
    writer.write(data.encode())

```

When you need to loop over the lines coming from an input stream, [`collections.abc.Iterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable) is another option worth reaching for:

```python
def read_config(stream: Iterable[str]):
    for line in stream:
        ...

```

[Subject index](INDEX.md) · [Continue](typing-cast-to-typing-assert-never.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.IO, typing.TextIO and typing.BinaryIO interfaces](typing-textio-class-to-typing-binaryio-class.md) · [Preceding source contract and version conditions](typing-textio-class-to-typing-binaryio-class.md)
