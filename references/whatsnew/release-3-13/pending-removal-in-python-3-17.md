# What's New In Python 3.13 / Pending removal in Python 3.17 — collections.abc, typing

### Pending removal in Python 3.17

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc):

  - Removal of [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) is planned for Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), apply `isinstance(obj, collections.abc.Buffer)`. Within type annotations, you can either reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or write a union spelling out precisely the types you handle (e.g., `bytes | bytearray | memoryview`).

The initial design for `ByteString` was an abstract class acting as a common supertype above both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC carried no methods at all, learning that some object was a `ByteString` instance conveyed nothing of value about it. Frequently used buffer types like [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as subtypes of `ByteString`, whether at runtime or by static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the fuller picture. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Prior to Python 3.14, the private class `typing._UnionGenericAlias` backed old-style unions. The implementation no longer requires that class, though it has been kept around for backward compatibility, with its removal targeted at Python 3.17. Rather than leaning on private implementation details, callers should turn to documented introspection helpers such as [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

  - [`typing.ByteString`](https://docs.python.org/3.14/library/typing.html#typing.ByteString), already deprecated since Python 3.9, is planned for removal in Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), apply `isinstance(obj, collections.abc.Buffer)`. Within type annotations, you can either reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or write a union spelling out precisely the types you handle (e.g., `bytes | bytearray | memoryview`).

The initial design for `ByteString` was an abstract class acting as a common supertype above both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC carried no methods at all, learning that some object was a `ByteString` instance conveyed nothing of value about it. Frequently used buffer types like [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as subtypes of `ByteString`, whether at runtime or by static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the fuller picture. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-16.md) · [Next source section](pending-removal-in-python-3-18.md) · [Release/subject declaration](summary-release-highlights.md)
