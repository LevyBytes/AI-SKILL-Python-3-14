# Python 3.9.0 alpha 1 / library / typing

[bpo-38191](https://bugs.python.org/issue?@action=redirect&bpo=38191): The constructors of [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) and [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) types now tolerate any keyword argument names whatsoever, “cls”, “self”, “typename”, “_typename”, “fields” and “_fields” among them.

[bpo-38405](https://bugs.python.org/issue?@action=redirect&bpo=38405): It is now possible to pickle nested subclasses of [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple).

[bpo-37953](https://bugs.python.org/issue?@action=redirect&bpo=37953): Within [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing), the `__hash__` and `__eq__` methods for `ForwardReferences` were improved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
