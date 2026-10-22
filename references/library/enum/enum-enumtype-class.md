# enum: `enum.EnumType`

### Data types

 *class *enum.EnumType

*EnumType* acts as the [metaclass](https://docs.python.org/3.14/glossary.html#term-metaclass) for *enum* enumerations. Subclassing *EnumType* is permitted – consult [Subclassing EnumType](https://docs.python.org/3.14/howto/enum.html#enumtype-examples) for the specifics.

`EnumType` handles installing the proper `__repr__()`, `__str__()`, `__format__()`, and `__reduce__()` methods on the finished *enum*, plus building the enum members, dealing correctly with duplicates, supplying iteration across the enum class, and so on.

Added in version 3.11: Prior to 3.11 `EnumType` went by the name `EnumMeta`, which remains usable as an alias.

[Subject index](INDEX.md) · [Previous](verify-to-enum-bin.md) · [Continue](enum-enumtype-call-to-enum-enumtype-dir.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)
