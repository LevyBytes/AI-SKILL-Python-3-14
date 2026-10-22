# Python 3.13.0 beta 1 / library / types

[gh-110209](https://github.com/python/cpython/issues/110209): Adds [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) to [`types.GeneratorType`](https://docs.python.org/3.14/library/types.html#types.GeneratorType) and [`types.CoroutineType`](https://docs.python.org/3.14/library/types.html#types.CoroutineType) so they can be used in type hints. James Hilton-Balfe wrote the patch.

[gh-108191](https://github.com/python/cpython/issues/108191): The [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace) now takes an optional positional argument that provides starting attribute values, given either as a dict or as an iterable of key-value pairs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
