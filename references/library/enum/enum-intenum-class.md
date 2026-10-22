# enum: `enum.IntEnum`

*class *enum.IntEnum

*IntEnum* matches `Enum`, except its members are integers as well and may appear anywhere an integer is valid. Whenever an integer operation involves an *IntEnum* member, the produced value sheds its enumeration status.

```python
>>> from enum import IntEnum
>>> class Number(IntEnum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...
>>> Number.THREE
<Number.THREE: 3>
>>> Number.ONE + Number.TWO
3
>>> Number.THREE + 5
8
>>> Number.THREE == 3
True

```

Note

Pairing `auto` with `IntEnum` produces integers that grow in value, beginning at `1`.

Changed in version 3.11: To better serve the *replacement of existing constants* use-case, [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) now maps to `int.__str__()`. For that very same purpose, [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) had already been `int.__format__()`.

[Subject index](INDEX.md) · [Previous](enum-enum-str-to-enum-enum-add-value-alias.md) · [Continue](enum-strenum-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
