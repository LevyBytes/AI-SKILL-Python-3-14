# IntEnum

### Derived Enumerations

### IntEnum

The first [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) variant on offer also subclasses [`int`](https://docs.python.org/3.14/library/functions.html#int). You can compare the members of an [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) against integers; and by the same token, integer enumerations of differing types compare against one another as well:

```python
>>> from enum import IntEnum
>>> class Shape(IntEnum):
...     CIRCLE = 1
...     SQUARE = 2
...
>>> class Request(IntEnum):
...     POST = 1
...     GET = 2
...
>>> Shape == 1
False
>>> Shape.CIRCLE == 1
True
>>> Shape.CIRCLE == Request.POST
True

```

Nevertheless, comparing them with regular [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) enumerations remains impossible:

```python
>>> class Shape(IntEnum):
...     CIRCLE = 1
...     SQUARE = 2
...
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...
>>> Shape.CIRCLE == Color.RED
False

```

In the other respects you'd anticipate, [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) values act like integers:

```python
>>> int(Shape.CIRCLE)
1
>>> ['a', 'b', 'c'][Shape.CIRCLE]
'b'
>>> [i for i in range(Shape.SQUARE)]
[0, 1]

```

[Subject index](INDEX.md) · [Previous source context](functional-enum-signature-and-start-parameter.md) · [Following source context](strenum.md)
