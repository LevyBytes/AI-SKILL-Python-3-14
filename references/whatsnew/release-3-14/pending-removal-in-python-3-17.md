# What's new in Python 3.14 / Pending removal in Python 3.17 - collections.abc, typing

### Pending removal in Python 3.17

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc):

  - Removal of [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) is planned for Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer), or write a union naming exactly the types your code handles (e.g., `bytes | bytearray | memoryview`).

The original design for `ByteString` was an abstract class acting as a common supertype above both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC defined no methods at all, learning that an object was a `ByteString` instance conveyed nothing useful about it. Additional widespread buffer types like [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as `ByteString` subtypes, whether at runtime or under static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the full account. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Prior to Python 3.14, the private class `typing._UnionGenericAlias` backed the implementation of old-style unions. The implementation no longer requires this class, though it survives for backward compatibility, with its removal slated for Python 3.17. Rather than leaning on private internals, code should reach for documented introspection helpers such as [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

  - [`typing.ByteString`](https://docs.python.org/3.14/library/typing.html#typing.ByteString), which has carried a deprecation since Python 3.9, is slated to go away in Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer), or write a union naming exactly the types your code handles (e.g., `bytes | bytearray | memoryview`).

The original design for `ByteString` was an abstract class acting as a common supertype above both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC defined no methods at all, learning that an object was a `ByteString` instance conveyed nothing useful about it. Additional widespread buffer types like [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as `ByteString` subtypes, whether at runtime or under static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the full account. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-16.md) · [Next source section](pending-removal-in-python-3-18.md) · [Release/subject declaration](summary-release-highlights.md)
