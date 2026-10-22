# Python 3.12.0 alpha 1 / core and builtins / types

[gh-89828](https://github.com/python/cpython/issues/89828): [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias) stops forwarding the `__class__` attribute. As an example, `isinstance(list[int], type)` will no longer give back `True`.

[gh-87995](https://github.com/python/cpython/issues/87995): [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) instances become hashable whenever their underlying mapping is hashable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
