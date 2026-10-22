# Python 3.11.0 beta 1 / library / typing

[gh-92332](https://github.com/python/cpython/issues/92332): Mark [`typing.Text`](https://docs.python.org/3.14/library/typing.html#typing.Text) as deprecated (no removal of the class is presently planned). Alex Waygood authored the patch.

[gh-88089](https://github.com/python/cpython/issues/88089): Introduce support for generic [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple).

[gh-91860](https://github.com/python/cpython/issues/91860): Introduce [`typing.dataclass_transform()`](https://docs.python.org/3.14/library/typing.html#typing.dataclass_transform), which implements [**PEP 681**](https://peps.python.org/pep-0681/). Jelle Zijlstra authored the patch.

[gh-90633](https://github.com/python/cpython/issues/90633): Carry the supplied value into the exception that [`typing.assert_never()`](https://docs.python.org/3.14/library/typing.html#typing.assert_never) raises. Jelle Zijlstra authored the patch.

[gh-91621](https://github.com/python/cpython/issues/91621): Repair [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) when used with [`collections.abc.Callable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable). Shantanu Jain authored the patch.

[bpo-44791](https://bugs.python.org/issue?@action=redirect&bpo=44791): Permit an ellipsis as the final argument given to [`typing.Concatenate`](https://docs.python.org/3.14/library/typing.html#typing.Concatenate).

[bpo-44863](https://bugs.python.org/issue?@action=redirect&bpo=44863): Let [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) subclasses list [`Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic) among their base classes when using the class-based syntax. That makes it possible to write a generic `TypedDict`, behaving like any user-defined generic yet carrying `TypedDict` semantics.

[bpo-45100](https://bugs.python.org/issue?@action=redirect&bpo=45100): Provide [`typing.get_overloads()`](https://docs.python.org/3.14/library/typing.html#typing.get_overloads) plus [`typing.clear_overloads()`](https://docs.python.org/3.14/library/typing.html#typing.clear_overloads). Jelle Zijlstra authored the patch.

[bpo-44807](https://bugs.python.org/issue?@action=redirect&bpo=44807): [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) will no longer quietly swap out `__init__()` methods that subclasses have defined. Adrian Garcia Badaracco authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
