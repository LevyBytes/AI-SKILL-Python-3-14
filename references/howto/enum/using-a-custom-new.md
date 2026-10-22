# Using a custom `__new__()`

#### Using a custom [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__)

Employing an auto-numbering [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) would look like:

```python
>>> class AutoNumber(Enum):
...     def __new__(cls):
...         value = len(cls.__members__) + 1
...         obj = object.__new__(cls)
...         obj._value_ = value
...         return obj
...
>>> class Color(AutoNumber):
...     RED = ()
...     GREEN = ()
...     BLUE = ()
...
>>> Color.GREEN
<Color.GREEN: 2>

```

For a more all-purpose `AutoNumber`, append `*args` to the signature:

```python
>>> class AutoNumber(Enum):
...     def __new__(cls, *args):      # this is the only change from above
...         value = len(cls.__members__) + 1
...         obj = object.__new__(cls)
...         obj._value_ = value
...         return obj
...

```

After that, inheriting from `AutoNumber` lets you supply your own `__init__` to deal with any leftover arguments:

```python
>>> class Swatch(AutoNumber):
...     def __init__(self, pantone='unknown'):
...         self.pantone = pantone
...     AUBURN = '3497'
...     SEA_GREEN = '1246'
...     BLEACHED_CORAL = () # New color, no Pantone code yet!
...
>>> Swatch.SEA_GREEN
<Swatch.SEA_GREEN: 2>
>>> Swatch.SEA_GREEN.pantone
'1246'
>>> Swatch.BLEACHED_CORAL.pantone
'unknown'

```

Note

When present, the [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method is invoked while the Enum members are being created; afterward Enum’s own `__new__()` takes its place and handles lookups of existing members once the class is built.

Warning

*Do not* call `super().__new__()`, since the one that gets located is the lookup-only `__new__`; rather, reference the data type directly – e.g.:

```python
obj = int.__new__(cls, value)

```

[Subject index](INDEX.md) · [Previous source context](using-a-descriptive-string.md) · [Following source context](orderedenum.md)
