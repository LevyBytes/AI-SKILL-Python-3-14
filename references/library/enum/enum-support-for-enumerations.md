# enum`enum` - Support for enumerations

### `enum` - Support for enumerations

Added in version 3.4.

**Source code:** [Lib/enum.py](https://github.com/python/cpython/tree/3.14/Lib/enum.py)

---

An enumeration:

- groups symbolic names (its members), each tied to a value that is unique

- supports iteration, yielding its canonical (that is, non-alias) members ordered as defined

- employs *call* syntax for fetching members by their value

- employs *index* syntax for fetching members by their name

You can build enumerations through [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) syntax, or alternatively through function-call syntax:

```python
>>> from enum import Enum

>>> # class syntax
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

>>> # functional syntax
>>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

```

While [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) syntax is available for building Enums, an Enum is not an ordinary Python class. Consult [How are Enums different?](https://docs.python.org/3.14/howto/enum.html#enum-class-differences) if you want the fuller treatment.

Note

Nomenclature

- The class `Color` counts as an *enumeration* (or *enum*)

- The attributes `Color.RED`, `Color.GREEN`, etc., serve as *enumeration members* (or *members*) and behave like constants.

- Each enum member carries both *names* and *values* (here the name of `Color.RED` is `RED`, while the value of `Color.BLUE` is `3`, and so on)

---

[Subject index](INDEX.md) · [Continue](property-to-unique.md)
