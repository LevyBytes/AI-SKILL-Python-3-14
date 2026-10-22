# Using `auto`

#### Using [`auto`](https://docs.python.org/3.14/library/enum.html#enum.auto)

Reaching for [`auto`](https://docs.python.org/3.14/library/enum.html#enum.auto) would look like:

```python
>>> class Color(Enum):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> Color.GREEN
<Color.GREEN: 3>

```

[Subject index](INDEX.md) · [Previous source context](omitting-values.md) · [Following source context](using-object.md)
