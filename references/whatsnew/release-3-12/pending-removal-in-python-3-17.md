# What’s New In Python 3.12 / Pending removal in Python 3.17 — collections.abc

### Pending removal in Python 3.17

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc):

  - Removal of [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) is slated for Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. When annotating types, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer), or spell out a union covering exactly the types you handle (for instance, `bytes | bytearray | memoryview`).

The plan behind `ByteString` was for it to be an abstract base acting as a common supertype over [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) plus [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Because the ABC carried no methods at all, however, learning that some value counted as a `ByteString` instance conveyed nothing genuinely helpful about it. Additional widespread buffer kinds, for example [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview), were likewise never treated as `ByteString` subtypes, neither while running nor under static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the full discussion. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Up through Python 3.13, the runtime built old-style unions on top of the private class `typing._UnionGenericAlias`. The implementation no longer relies on it, yet it stays around for compatibility, slated to disappear in Python 3.17. Lean on the published introspection utilities such as [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args) rather than depending on private internals.

  - [`typing.ByteString`](https://docs.python.org/3.14/library/typing.html#typing.ByteString), which has carried a deprecation since Python 3.9, will go away in Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. When annotating types, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer), or spell out a union covering exactly the types you handle (for instance, `bytes | bytearray | memoryview`).

The plan behind `ByteString` was for it to be an abstract base acting as a common supertype over [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) plus [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Because the ABC carried no methods at all, however, learning that some value counted as a `ByteString` instance conveyed nothing genuinely helpful about it. Additional widespread buffer kinds, for example [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview), were likewise never treated as `ByteString` subtypes, neither while running nor under static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for the full discussion. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-16.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](undated-api-removals.md)
