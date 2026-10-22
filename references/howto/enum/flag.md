# Flag

### Flag

[`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) is the final variant. As with [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag), `Flag` members support the bitwise operators (&, |, ^, ~) for combining them. The difference from `IntFlag` is that they cannot be merged with, or measured against, any other `Flag` enumeration, nor an [`int`](https://docs.python.org/3.14/library/functions.html#int). Although you may assign the values yourself, the better practice is to set the value to [`auto`](https://docs.python.org/3.14/library/enum.html#enum.auto) and allow `Flag` to pick a suitable one.

Added in version 3.6.

Just as with [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag), when combining [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) members yields no flags at all, evaluating it as a boolean gives [`False`](https://docs.python.org/3.14/library/constants.html#False):

```python
>>> from enum import Flag, auto
>>> class Color(Flag):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> Color.RED & Color.GREEN
<Color: 0>
>>> bool(Color.RED & Color.GREEN)
False

```

Each separate flag ought to carry a value that is a power of two (1, 2, 4, 8, …), whereas combined flags will not:

```python
>>> class Color(Flag):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...     WHITE = RED | BLUE | GREEN
...
>>> Color.WHITE
<Color.WHITE: 7>

```

Assigning a name to the “no flags set” state leaves its boolean value untouched:

```python
>>> class Color(Flag):
...     BLACK = 0
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> Color.BLACK
<Color.BLACK: 0>
>>> bool(Color.BLACK)
False

```

You can also loop through [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) members:

```python
>>> purple = Color.RED | Color.BLUE
>>> list(purple)
[<Color.RED: 1>, <Color.BLUE: 2>]

```

Added in version 3.11.

Note

In most fresh code, reach for [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) and [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag), because [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) and [`IntFlag`](https://docs.python.org/3.14/library/enum.html#enum.IntFlag) violate certain semantic guarantees of an enumeration (since they compare equal to integers, and therefore by transitivity to other unrelated enumerations). Save `IntEnum` and `IntFlag` for the situations where `Enum` and `Flag` simply won’t suffice; for instance, when swapping out integer constants for enumerations, or when interoperating with external systems.

[Subject index](INDEX.md) · [Previous source context](intflag-continuation.md) · [Following source context](others.md)
