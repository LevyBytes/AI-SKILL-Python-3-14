# When to use `__new__()` vs. `__init__()`

### When to use [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) vs. [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__)

You must reach for [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) any time you need to tailor the actual value of an [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) member. Every other tweak can live in either `__new__()` or [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__), and `__init__()` is the preferred home.

As an illustration, suppose you want to hand the constructor several items yet treat only one of them as the value:

```python
>>> class Coordinate(bytes, Enum):
...     """
...     Coordinate with binary codes that can be indexed by the int code.
...     """
...     def __new__(cls, value, label, unit):
...         obj = bytes.__new__(cls, [value])
...         obj._value_ = value
...         obj.label = label
...         obj.unit = unit
...         return obj
...     PX = (0, 'P.X', 'km')
...     PY = (1, 'P.Y', 'km')
...     VX = (2, 'V.X', 'km/s')
...     VY = (3, 'V.Y', 'km/s')
...

>>> print(Coordinate['PY'])
Coordinate.PY

>>> print(Coordinate(3))
Coordinate.VY

```

Warning

*Do not* call `super().__new__()`, since the one that gets located is the lookup-only `__new__`; rather, reference the data type directly.

[Subject index](INDEX.md) · [Previous source context](others.md) · [Following source context](supported-dunder-and-sunder-names.md)
