# Python 3.13.0 alpha 6 / library / types

[gh-117182](https://github.com/python/cpython/issues/117182): When lazily loading modules that overwrite their own `__class__`, the `__class__` is no longer reset back to [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
