# Language and standard library pending removal in 3.17: collections.abc; typing

### Pending removal in Python 3.17

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc):

  - [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) is set for removal in Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or a union naming exactly the types your code handles (for example, `bytes | bytearray | memoryview`).

The intent behind `ByteString` was an abstract class acting as a supertype of both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Because the ABC carried no methods, though, learning that an object was a `ByteString` instance told you nothing useful about it. Widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as subtypes of `ByteString`, whether at runtime or by static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for further detail. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Prior to Python 3.14, old-style unions relied on the private class `typing._UnionGenericAlias`. The implementation no longer needs this class, but it stays for backward compatibility, with removal targeted for Python 3.17. Rather than depending on private internals, use documented introspection helpers such as [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

  - [`typing.ByteString`](https://docs.python.org/3.14/library/typing.html#typing.ByteString), which has been deprecated since Python 3.9, is set for removal in Python 3.17.

To check at runtime whether `obj` supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), call `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or a union naming exactly the types your code handles (for example, `bytes | bytearray | memoryview`).

The intent behind `ByteString` was an abstract class acting as a supertype of both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Because the ABC carried no methods, though, learning that an object was a `ByteString` instance told you nothing useful about it. Widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never treated as subtypes of `ByteString`, whether at runtime or by static type checkers.

Consult [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for further detail. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

## Pending removal in Python 3.17

### Pending removal in Python 3.17

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc):

  - Removal of [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) is scheduled for Python 3.17.

To check at runtime whether `obj` implements the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), use `isinstance(obj, collections.abc.Buffer)`. Within type annotations, either reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or a union spelling out exactly the types your code accepts (e.g., `bytes | bytearray | memoryview`).

The original aim of `ByteString` was an abstract class acting as a supertype for both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC carried no methods, learning that an object was a `ByteString` instance told you nothing useful about it. Static type checkers and the runtime alike never treated other widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) as subtypes of `ByteString`.

See [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - Prior to Python 3.14, old-style unions relied on the private class `typing._UnionGenericAlias`. The implementation no longer needs that class, but it stays around for backward compatibility, with removal scheduled for Python 3.17. Rather than leaning on private implementation details, users should turn to documented introspection helpers such as [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

  - [`typing.ByteString`](https://docs.python.org/3.14/library/typing.html#typing.ByteString) has carried a deprecation since Python 3.9 and is now set for removal in Python 3.17.

To check at runtime whether `obj` implements the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), use `isinstance(obj, collections.abc.Buffer)`. Within type annotations, either reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or a union spelling out exactly the types your code accepts (e.g., `bytes | bytearray | memoryview`).

The original aim of `ByteString` was an abstract class acting as a supertype for both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC carried no methods, learning that an object was a `ByteString` instance told you nothing useful about it. Static type checkers and the runtime alike never treated other widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) as subtypes of `ByteString`.

See [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

[Subject index](INDEX.md) · [Previous source section](../python-3-16/functools-through-tarfile.md) · [Next source section](../python-3-18/decimal.md)
