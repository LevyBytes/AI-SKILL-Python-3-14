# Others

### Others

Even though [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) ships as part of the [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module, rolling your own version would take very little effort:

```python
class IntEnum(int, ReprEnum):   # or Enum instead of ReprEnum
    pass

```

That illustrates how comparable derived enumerations could be built; you could, say, define a `FloatEnum` that mixes in [`float`](https://docs.python.org/3.14/library/functions.html#float) rather than [`int`](https://docs.python.org/3.14/library/functions.html#int).

Some rules:

1.

While subclassing [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum), the mix-in types have to be listed ahead of the `Enum` class within the base sequence, just as the [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) sample above shows.

2.

A mix-in type has to allow subclassing. Take [`bool`](https://docs.python.org/3.14/library/functions.html#bool) and [`range`](https://docs.python.org/3.14/library/stdtypes.html#range): neither can be subclassed, so each raises an error during Enum creation if supplied as the mix-in type.

3.

Although [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) accepts members of any type, the moment an extra type is mixed in, every member has to hold a value of that type — for example [`int`](https://docs.python.org/3.14/library/functions.html#int) above. That constraint is waived for mix-ins that merely contribute methods and declare no other type.

4.

After a second data type joins the mix, the enum member itself is *not the same* as its [`value`](https://docs.python.org/3.14/library/enum.html#enum.Enum.value) attribute, even though the pair are equivalent and will compare equal.

5.

A `data type` refers to a mixin that supplies [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__), or a [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass)

6.

%-style formatting: `%s` and `%r` invoke the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) class’s [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) respectively; the remaining codes (for instance `%i` or `%h` for IntEnum) handle the enum member as its mixed-in type.

7.

[Formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), and [`format()`](https://docs.python.org/3.14/library/functions.html#format) all rely on the enum’s [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) method.

Note

Given that [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum), [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag), and [`StrEnum`](https://docs.python.org/3.14/library/enum.html#enum.StrEnum) are meant to serve as drop-in stand-ins for existing constants, their [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) method is restored to the `__str__()` method of their underlying data types.

[Subject index](INDEX.md) · [Previous source context](flag.md) · [Following source context](when-to-use-new-vs-init.md)
