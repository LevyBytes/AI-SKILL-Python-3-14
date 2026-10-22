# unittest.mock — Mocking Magic Methods — Contract: Unary numeric methods: `__neg__`, `__pos__` and `__invert__`

Unary numeric methods: `__neg__`, `__pos__` and `__invert__`

- The numeric methods (including right hand and in-place variants): `__add__`, `__sub__`, `__mul__`, `__matmul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__divmod__`, `__lshift__`, `__rshift__`, `__and__`, `__xor__`, `__or__`, and `__pow__`

- Numeric conversion methods: `__complex__`, `__int__`, `__float__` and `__index__`

- Descriptor methods: `__get__`, `__set__` and `__delete__`

- Pickling: `__reduce__`, `__reduce_ex__`, `__getinitargs__`, `__getnewargs__`, `__getstate__` and `__setstate__`

- File system path representation: `__fspath__`

- Asynchronous iteration methods: `__aiter__` and `__anext__`

Changed in version 3.8: Added support for [`os.PathLike.__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__).

Changed in version 3.8: Added support for `__aenter__`, `__aexit__`, `__aiter__` and `__anext__`.

These methods exist but are *not* supported, because they are either already used by mock, can't be assigned dynamically, or are liable to cause trouble:

- `__getattr__`, `__setattr__`, `__init__` and `__new__`

- `__prepare__`, `__instancecheck__`, `__subclasscheck__`, `__del__`

[Subject index](INDEX.md) · [Previous](magic-method-mocking-overview.md) · [Continue](unittest-mock-magicmock-class.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Mocking Magic Methods](magic-method-mocking-overview.md)
