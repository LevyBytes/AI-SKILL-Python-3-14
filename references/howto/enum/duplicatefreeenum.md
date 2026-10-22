# DuplicateFreeEnum

### DuplicateFreeEnum

Throws an error when a duplicate member value turns up, in place of building an alias:

```python
>>> class DuplicateFreeEnum(Enum):
...     def __init__(self, *args):
...         cls = self.__class__
...         if any(self.value == e.value for e in cls):
...             a = self.name
...             e = cls(self.value).name
...             raise ValueError(
...                 "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
...                 % (a, e))
...
>>> class Color(DuplicateFreeEnum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
...     GRENE = 2
...
Traceback (most recent call last):
  ...
ValueError: aliases not allowed in DuplicateFreeEnum:  'GRENE' --> 'GREEN'

```

Note

This makes a handy example for subclassing Enum to introduce or adjust other behaviors as well as to forbid aliases. Should the only change you want be forbidding aliases, you can instead apply the [`unique()`](https://docs.python.org/3.14/library/enum.html#enum.unique) decorator.

[Subject index](INDEX.md) · [Previous source context](orderedenum.md) · [Following source context](multivalueenum.md)
