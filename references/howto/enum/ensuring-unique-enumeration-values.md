# Ensuring unique enumeration values

### Ensuring unique enumeration values

Out of the box, enumerations permit several names to act as aliases of one value. To turn that off, apply the [`unique()`](https://docs.python.org/3.14/library/enum.html#enum.unique) decorator:

```python
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

```

[Subject index](INDEX.md) · [Previous source context](duplicating-enum-members-and-values.md) · [Following source context](using-automatic-values.md)
