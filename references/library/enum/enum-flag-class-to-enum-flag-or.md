# enum / Data types: `enum.Flag`, `__contains__()`, `__iter__()`, `__len__()`, `__bool__()`, `__or__()`

*class *enum.Flag

`Flag` matches `Enum`, except its members work with the bitwise operators `&` (*AND*), `|` (*OR*), `^` (*XOR*), and `~` (*INVERT*); whatever those operations yield are (aliases of) members belonging to the enumeration.

 __contains__(*self*, *value*)

Yields *True* whenever value is contained in self:

```python
>>> from enum import Flag, auto
>>> class Color(Flag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> purple = Color.RED | Color.BLUE
>>> white = Color.RED | Color.GREEN | Color.BLUE
>>> Color.GREEN in purple
False
>>> Color.GREEN in white
True
>>> purple in white
True
>>> white in purple
False

```

 __iter__(*self*)

Yields all the non-alias members it contains:

```python
>>> list(Color.RED)
[<Color.RED: 1>]
>>> list(purple)
[<Color.RED: 1>, <Color.BLUE: 4>]

```

Added in version 3.11.

 __len__(*self*)

Yields the count of members within flag:

```python
>>> len(Color.GREEN)
1
>>> len(white)
3

```

Added in version 3.11.

 __bool__(*self*)

Yields *True* when flag holds any members, and *False* if not:

```python
>>> bool(Color.GREEN)
True
>>> bool(white)
True
>>> black = Color(0)
>>> bool(black)
False

```

 __or__(*self*, *other*)

Yields the present flag binary or’ed together with other:

```python
>>> Color.RED | Color.GREEN
<Color.RED|GREEN: 3>

```

[Subject index](INDEX.md) · [Previous](enum-strenum-class.md) · [Continue](enum-flag-and-to-enum-flag-numeric-repr.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
