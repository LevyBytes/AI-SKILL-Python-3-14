# Python 3.14.0 alpha 1 / library / tomllib

[gh-124835](https://github.com/python/cpython/issues/124835): Has [`tomllib.loads()`](https://docs.python.org/3.14/library/tomllib.html#tomllib.loads) throw [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) for unsupported input types lacking the `replace` attribute. The error text shown when [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) arrives is also better now.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
