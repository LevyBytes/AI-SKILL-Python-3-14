# enum / Module contents: `property()`, `unique()`

### Module contents

>

`EnumType`

>

The `type` backing Enum together with its subclasses.

`Enum`

>

Base class used to define enumerated constants.

`IntEnum`

>

Base class for enumerated constants which are additionally subclasses of [`int`](https://docs.python.org/3.14/library/functions.html#int). (Notes)

`StrEnum`

>

Base class for enumerated constants which are additionally subclasses of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). (Notes)

`Flag`

>

Base class for enumerated constants that may be combined via the bitwise operations while still retaining their `Flag` membership.

`IntFlag`

>

Base class for enumerated constants that may be combined via the bitwise operators while still retaining their `IntFlag` membership. The members of `IntFlag` are additionally subclasses of [`int`](https://docs.python.org/3.14/library/functions.html#int). (Notes)

`ReprEnum`

>

Relied upon by `IntEnum`, `StrEnum`, and `IntFlag` so that the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of the mixed-in type is preserved.

`EnumCheck`

>

An enumeration carrying the values `CONTINUOUS`, `NAMED_FLAGS`, and `UNIQUE`, meant for use alongside `verify()` to confirm that a given enumeration satisfies particular constraints.

`FlagBoundary`

>

An enumeration carrying the values `STRICT`, `CONFORM`, `EJECT`, and `KEEP` that grants finer control over the treatment of invalid values within an enumeration.

`EnumDict`

>

A subclass of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) intended for use when subclassing `EnumType`.

`auto`

>

Each instance gets swapped for a fitting value for Enum members. With `StrEnum` the default is the lower-cased form of the member name; the rest of the Enums start at 1 and count upward.

`property()`

>

Lets `Enum` members carry attributes without colliding with member names. The `value` and `name` attributes are built using exactly this mechanism.

`unique()`

>

An Enum class decorator guaranteeing that no value gets bound to more than one name.

[Subject index](INDEX.md) · [Previous](enum-support-for-enumerations.md) · [Continue](verify-to-enum-bin.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)
