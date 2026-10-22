# Python 3.12.0 alpha 1 / library / typing

[gh-96079](https://github.com/python/cpython/issues/96079): Inside [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing), a missing `name` field plus a wrong `__module__` on _AnnotatedAlias are repaired.

[gh-94309](https://github.com/python/cpython/issues/94309): The aliases [`typing.Hashable`](https://docs.python.org/3.14/library/typing.html#typing.Hashable) and [`typing.Sized`](https://docs.python.org/3.14/library/typing.html#typing.Sized) are deprecated.

[gh-94607](https://github.com/python/cpython/issues/94607): Subclassing complex generics that use type variables in [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) is fixed. Earlier an error reading `Some type variables ... are not listed in Generic[...]` appeared. `typing` no longer fills `__parameters__` using the `__parameters__` of a Python class.

[bpo-46642](https://bugs.python.org/issue?@action=redirect&bpo=46642): Made the error message clearer when somebody attempts to subclass an instance of [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple), and so on. Gregory Beauregard supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
