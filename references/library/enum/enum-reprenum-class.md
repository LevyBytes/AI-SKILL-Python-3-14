# enum: `enum.ReprEnum`

*class *enum.ReprEnum

`ReprEnum` adopts the `repr()` of `Enum` while taking the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) from the mixed-in data type:

- `int.__str__()` for `IntEnum` and `IntFlag`

- `str.__str__()` for `StrEnum`

Subclass `ReprEnum` to retain the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) / [`format()`](https://docs.python.org/3.14/library/functions.html#format) belonging to the mixed-in data type rather than falling back on the `Enum`-default `str()`.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](enum-intflag-class.md) · [Continue](enum-enumcheck-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
