# enum: `enum.IntFlag`

*class *enum.IntFlag

`IntFlag` matches `Flag`, except its members are integers as well and may appear anywhere an integer is valid.

```python
>>> from enum import IntFlag, auto
>>> class Color(IntFlag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> Color.RED & 2
<Color: 0>
>>> Color.RED | 2
<Color.RED|GREEN: 3>

```

Whenever an integer operation involves an *IntFlag* member, what comes back is not an *IntFlag*:

```python
>>> Color.RED + 2
3

```

When a `Flag` operation involves an *IntFlag* member, then:

- the result is a valid *IntFlag*: an *IntFlag* is returned

- the result is not a valid *IntFlag*: what happens is governed by the `FlagBoundary` setting

For unnamed zero-valued flags, the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) has been altered. These days it reads:

```python
>>> Color(0)
<Color: 0>

```

Note

Pairing `auto` with `IntFlag` produces integers that are powers of two, beginning at `1`.

Changed in version 3.11: To better serve the *replacement of existing constants* use-case, [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) now maps to `int.__str__()`. For that very same purpose, [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) had already been `int.__format__()`.

Inverting an `IntFlag` now hands back a positive value representing the union of every flag absent from the supplied flag, in place of a negative value. This lines up with the established `Flag` behavior.

[Subject index](INDEX.md) · [Previous](enum-flag-and-to-enum-flag-numeric-repr.md) · [Continue](enum-reprenum-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
