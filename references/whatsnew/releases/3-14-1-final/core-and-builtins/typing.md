# Python 3.14.1 final / core and builtins / typing

[gh-140000](https://github.com/python/cpython/issues/140000): Resolve a possible memory leak whenever a reference cycle forms between some instance of [`typing.TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType), [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), or [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple) and that object's `__name__` attribute. Mikhail Efimov supplied the patch.

[gh-139988](https://github.com/python/cpython/issues/139988): Resolve a memory leak that occurs upon failing to create a [`Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) type. Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
