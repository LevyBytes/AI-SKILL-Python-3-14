# Comparisons

### Comparisons

Identity is what's used to compare enumeration members:

```python
>>> Color.RED is Color.RED
True
>>> Color.RED is Color.BLUE
False
>>> Color.RED is not Color.BLUE
True

```

There is *no* support for ordered comparisons among enumeration values. Enum members aren't integers (though see IntEnum further down):

```python
>>> Color.RED < Color.BLUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'

```

Equality checks, on the other hand, do work:

```python
>>> Color.BLUE == Color.RED
False
>>> Color.BLUE != Color.RED
True
>>> Color.BLUE == Color.BLUE
True

```

Anything that isn't an enumeration value will always test as unequal (once more, [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) was deliberately built to act otherwise, covered below):

```python
>>> Color.BLUE == 2
False

```

Warning

Reloading modules is possible – should a reloaded module hold enums, those get rebuilt, and the fresh members might not test as identical/equal against the originals.

[Subject index](INDEX.md) · [Previous source context](iteration.md) · [Following source context](allowed-members-and-attributes-of-enumerations.md)
