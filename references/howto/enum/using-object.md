# Using `object`

#### Using [`object`](https://docs.python.org/3.14/library/functions.html#object)

Reaching for [`object`](https://docs.python.org/3.14/library/functions.html#object) would look like:

```python
>>> class Color(Enum):
...     RED = object()
...     GREEN = object()
...     BLUE = object()
...
>>> Color.GREEN
<Color.GREEN: <object object at 0x...>>

```

This also serves as a fine illustration of why you might choose to supply your own [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__):

```python
>>> class Color(Enum):
...     RED = object()
...     GREEN = object()
...     BLUE = object()
...     def __repr__(self):
...         return "<%s.%s>" % (self.__class__.__name__, self._name_)
...
>>> Color.GREEN
<Color.GREEN>

```

[Subject index](INDEX.md) · [Previous source context](using-auto.md) · [Following source context](using-a-descriptive-string.md)
