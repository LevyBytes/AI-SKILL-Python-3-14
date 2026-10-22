# enum: `enum.EnumCheck`

*class *enum.EnumCheck

*EnumCheck* holds the options consulted by the `verify()` decorator when enforcing various constraints; a failed constraint produces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 UNIQUE

Guarantee that every value maps to just one name:

```python
>>> from enum import Enum, verify, UNIQUE
>>> @verify(UNIQUE)
... class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
...     CRIMSON = 1
Traceback (most recent call last):
...
ValueError: aliases found in <enum 'Color'>: CRIMSON -> RED

```

 CONTINUOUS

Guarantee that no values are absent between the lowest-valued member and the highest-valued member:

```python
>>> from enum import Enum, verify, CONTINUOUS
>>> @verify(CONTINUOUS)
... class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 5
Traceback (most recent call last):
...
ValueError: invalid enum 'Color': missing values 3, 4

```

 NAMED_FLAGS

Guarantee that every flag group/mask holds nothing but named flags – handy whenever values are stated explicitly rather than produced by `auto()`:

```python
>>> from enum import Flag, verify, NAMED_FLAGS
>>> @verify(NAMED_FLAGS)
... class Color(Flag):
...     RED = 1
...     GREEN = 2
...     BLUE = 4
...     WHITE = 15
...     NEON = 31
Traceback (most recent call last):
...
ValueError: invalid Flag 'Color': aliases WHITE and NEON are missing combined values of 0x18 [use enum.show_flag_values(value) for details]

```

Note

CONTINUOUS and NAMED_FLAGS are built to operate on integer-valued members.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](enum-reprenum-class.md) · [Continue](enum-flagboundary-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
