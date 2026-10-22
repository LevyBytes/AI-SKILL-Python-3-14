# Flag Classes

### Flag Classes

Flags treat aliasing more broadly: for a flag to count as canonical, its value must be a power-of-two value and must not be a duplicate name. Hence, on top of the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) notion of an alias, any flag that has no value (i.e. `0`) or that holds more than a single power-of-two value (e.g. `3`) qualifies as an alias.

[Subject index](INDEX.md) · [Previous source context](enum-classes.md) · [Following source context](enum-members.md)
