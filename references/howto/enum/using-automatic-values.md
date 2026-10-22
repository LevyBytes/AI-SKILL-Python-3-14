# Using automatic values

### Using automatic values

When the precise value doesn't matter, [`auto`](https://docs.python.org/3.14/library/enum.html#enum.auto) is available:

```python
>>> from enum import Enum, auto
>>> class Color(Enum):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> [member.value for member in Color]
[1, 2, 3]

```

Those values come from [`_generate_next_value_()`](https://docs.python.org/3.14/library/enum.html#enum.Enum._generate_next_value_), and you may override it:

```python
>>> class AutoName(Enum):
...     @staticmethod
...     def _generate_next_value_(name, start, count, last_values):
...         return name
...
>>> class Ordinal(AutoName):
...     NORTH = auto()
...     SOUTH = auto()
...     EAST = auto()
...     WEST = auto()
...
>>> [member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']

```

Note

You have to declare the [`_generate_next_value_()`](https://docs.python.org/3.14/library/enum.html#enum.Enum._generate_next_value_) method ahead of any members.

[Subject index](INDEX.md) · [Previous source context](ensuring-unique-enumeration-values.md) · [Following source context](iteration.md)
