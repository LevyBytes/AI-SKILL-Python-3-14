# enum: `enum.StrEnum`

*class *enum.StrEnum

*StrEnum* matches `Enum`, except its members are strings as well and may appear in most of the places a string is valid. Whatever a string operation yields when applied to or with a *StrEnum* member falls outside the enumeration.

```python
>>> from enum import StrEnum, auto
>>> class Color(StrEnum):
...     RED = 'r'
...     GREEN = 'g'
...     BLUE = 'b'
...     UNKNOWN = auto()
...
>>> Color.RED
<Color.RED: 'r'>
>>> Color.UNKNOWN
<Color.UNKNOWN: 'unknown'>
>>> str(Color.UNKNOWN)
'unknown'

```

Note

Certain spots in the stdlib test for an exact [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) rather than a `str` subclass (that is, `type(unknown) == str` in place of `isinstance(unknown, str)`), and at those spots you must resort to `str(MyStrEnum.MY_MEMBER)`.

Note

Pairing `auto` with `StrEnum` yields the lower-cased member name as the value.

Note

To better serve the *replacement of existing constants* use-case, [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) is `str.__str__()`. By the same token, [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) is `str.__format__()`.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](enum-intenum-class.md) · [Continue](enum-flag-class-to-enum-flag-or.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
