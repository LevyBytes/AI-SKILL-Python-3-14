# OrderedEnum

### OrderedEnum

An ordered enumeration that does not derive from [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) and therefore keeps the usual [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) invariants (for instance not being comparable to other enumerations):

```python
>>> class OrderedEnum(Enum):
...     def __ge__(self, other):
...         if self.__class__ is other.__class__:
...             return self.value >= other.value
...         return NotImplemented
...     def __gt__(self, other):
...         if self.__class__ is other.__class__:
...             return self.value > other.value
...         return NotImplemented
...     def __le__(self, other):
...         if self.__class__ is other.__class__:
...             return self.value <= other.value
...         return NotImplemented
...     def __lt__(self, other):
...         if self.__class__ is other.__class__:
...             return self.value < other.value
...         return NotImplemented
...
>>> class Grade(OrderedEnum):
...     A = 5
...     B = 4
...     C = 3
...     D = 2
...     F = 1
...
>>> Grade.C < Grade.A
True

```

[Subject index](INDEX.md) · [Previous source context](using-a-custom-new.md) · [Following source context](duplicatefreeenum.md)
