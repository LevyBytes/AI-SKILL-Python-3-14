# Python 3.13.0 alpha 5 / library / inspect

[gh-112006](https://github.com/python/cpython/issues/112006): Repair [`inspect.unwrap()`](https://docs.python.org/3.14/library/inspect.html#inspect.unwrap) for types carrying the `__wrapper__` data descriptor. Repair [`inspect.Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable) for the builtins [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) and [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod).

[gh-101293](https://github.com/python/cpython/issues/101293): Handle callables that carry the `__call__()` method, plus types whose `__new__()` and `__init__()` methods are set to class methods, static methods, bound methods, partial functions, and further kinds of methods and descriptors, inside [`inspect.Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
