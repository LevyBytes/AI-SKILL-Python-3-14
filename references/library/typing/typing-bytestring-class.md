# typing: `typing.ByteString`

*class *typing.ByteString(*Sequence[int]*)

Deprecated alias to [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString).

To check at runtime whether `obj` satisfies the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. For annotation purposes, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or write a union spelling out exactly the types your code accepts (for instance, `bytes | bytearray | memoryview`).

The original idea behind `ByteString` was an abstract class acting as a common supertype above both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Because the ABC carried no methods at all, however, learning that some object was a `ByteString` instance told you nothing of value about it. Furthermore, widespread buffer types like [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were never treated as subtypes of `ByteString`, neither at runtime nor by static type checkers.

See [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for more details.

Deprecated since version 3.9, will be removed in version 3.17.

[Subject index](INDEX.md) · [Previous](typing-abstractset-class.md) · [Continue](typing-collection-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Aliases to container ABCs in `collections.abc`](typing-abstractset-class.md)
