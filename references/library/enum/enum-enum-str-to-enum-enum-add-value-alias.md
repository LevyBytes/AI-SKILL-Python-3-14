# enum.Enum: `__str__()`, `__format__()`, `_add_alias_()`, `_add_value_alias_()`

__str__(*self*)

Yields the string employed by *str()* calls. By default this returns the *Enum* name plus the member name, but you may override it:

```python
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __str__(self):
...         return f'{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(<OtherStyle.ALTERNATE: 1>, 'ALTERNATE', 'ALTERNATE')

```

 __format__(*self*)

Yields the string employed by *format()* and *f-string* calls. By default this returns the `__str__()` return value, but you may override it:

```python
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __format__(self, spec):
...         return f'{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(<OtherStyle.ALTERNATE: 1>, 'OtherStyle.ALTERNATE', 'ALTERNATE')

```

Note

Pairing `auto` with `Enum` produces integers that grow in value, beginning at `1`.

Changed in version 3.12: Added [Dataclass support](https://docs.python.org/3.14/howto/enum.html#enum-dataclass-support)

 _add_alias_()

Registers an additional name as an alias pointing at an existing member:

```python
>>> Color.RED._add_alias_("ERROR")
>>> Color.ERROR
<Color.RED: 1>

```

Raises a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) should the name already belong to a different member.

Added in version 3.13.

 _add_value_alias_()

Registers an additional value as an alias pointing at an existing member:

```python
>>> Color.RED._add_value_alias_(42)
>>> Color(42)
<Color.RED: 1>

```

   Raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) should the value already be tied to a different member. Refer to [MultiValueEnum](https://docs.python.org/3.14/howto/enum.html#multi-value-enum) for an illustration.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](weekday-init-to-enum-enum-repr.md) · [Continue](enum-intenum-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.Enum](enum-enum-class.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
