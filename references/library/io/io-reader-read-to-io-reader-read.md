# io.Reader: `read()`

read()

 read(*size*, */*)

Read data off the input stream and hand it back. When *size* is given, it ought to be an integer, and at most *size* items (bytes/characters) get read.

For example:

```python
def read_it(reader: Reader[str]):
    data = reader.read(11)
    assert isinstance(data, str)

```

[Subject index](INDEX.md) · [Previous](static-typing.md) · [Continue](io-writer-write.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.Reader](static-typing.md) · [Owning module, declaration or section: Static Typing](static-typing.md)
