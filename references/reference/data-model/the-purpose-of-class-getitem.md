# 3.3.5.1. The purpose of *__class_getitem__*

#### 3.3.5.1. The purpose of *__class_getitem__*

`__class_getitem__()` exists to permit runtime parameterization of standard-library generic classes so that [type hints](https://docs.python.org/3.14/glossary.html#term-type-hint) can be applied to those classes more readily.

If you want to build custom generic classes that can be parameterized at runtime and recognised by static type-checkers, you should either inherit from a standard library class that already provides `__class_getitem__()`, or inherit from [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic), which carries its own implementation of `__class_getitem__()`.

Custom `__class_getitem__()` implementations on classes outside the standard library may go unrecognised by third-party type-checkers such as mypy. Putting `__class_getitem__()` on any class for reasons besides type hinting is discouraged.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-generic-types.md) · [Previous source section](emulating-generic-types.md) · [Following source section](class-getitem-versus-getitem.md)
