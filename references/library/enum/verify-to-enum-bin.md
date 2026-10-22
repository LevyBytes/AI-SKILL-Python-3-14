# enum / Module contents: `verify()`, `member()`, `nonmember()`, `global_enum()`, `show_flag_values()`, `enum.bin()`

`verify()`

>

An Enum class decorator that validates user-selectable constraints against an enumeration.

`member()`

>

Turn `obj` into a member. May serve as a decorator.

`nonmember()`

>

Keep `obj` from becoming a member. May serve as a decorator.

`global_enum()`

>

Adjust an enum's [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) so its members appear to belong to the module rather than its class, and publish the enum members into the global namespace.

`show_flag_values()`

>

Yield a list of every power-of-two integer held within a flag.

`enum.bin()`

>

Behaves like the built-in [`bin()`](https://docs.python.org/3.14/library/functions.html#bin), except that negative values appear in two’s complement form, with the leading bit consistently marking the sign (`0` implies positive, `1` implies negative).

Added in version 3.6: `Flag`, `IntFlag`, `auto`

Added in version 3.11: `StrEnum`, `EnumCheck`, `ReprEnum`, `FlagBoundary`, `property`, `member`, `nonmember`, `global_enum`, `show_flag_values`

Added in version 3.13: `EnumDict`

---

[Subject index](INDEX.md) · [Previous](property-to-unique.md) · [Continue](enum-enumtype-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Module contents](property-to-unique.md)
