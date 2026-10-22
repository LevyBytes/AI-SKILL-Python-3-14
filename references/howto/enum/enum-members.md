# Enum Members (aka instances)

### Enum Members (aka instances)

What stands out most about enum members is that each is a singleton. [`EnumType`](https://docs.python.org/3.14/library/enum.html#enum.EnumType) builds them all during the construction of the enum class itself, then installs a custom [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) that guarantees none are ever created anew by handing back only the members that already exist.

[Subject index](INDEX.md) · [Previous source context](flag-classes.md) · [Following source context](flag-members.md)
