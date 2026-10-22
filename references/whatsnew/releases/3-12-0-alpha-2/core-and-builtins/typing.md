# Python 3.12.0 alpha 2 / core and builtins / typing

[gh-98852](https://github.com/python/cpython/issues/98852): Correct subscripting of type aliases that wrap bare generic types or constructs such as [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar): consider `tuple[A, T][int]` together with `tuple[TypeVar, T][int]`, in which `A` denotes a generic type and `T` stands for a type variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
