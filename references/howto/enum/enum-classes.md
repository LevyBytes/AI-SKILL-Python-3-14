# Enum Classes

### Enum Classes

The [`EnumType`](https://docs.python.org/3.14/library/enum.html#enum.EnumType) metaclass supplies the [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__), [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__dir__), [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) and additional methods that let you perform actions on an [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) class that would fail on a regular class, such as `list(Color)` or `some_enum_var in Color`. `EnumType` also makes certain that the various remaining methods on the finished `Enum` class behave correctly (for instance [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__), [`__getnewargs__()`](https://docs.python.org/3.14/library/pickle.html#object.__getnewargs__), [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__)).

[Subject index](INDEX.md) · [Previous source context](how-are-enums-and-flags-different.md) · [Following source context](flag-classes.md)
