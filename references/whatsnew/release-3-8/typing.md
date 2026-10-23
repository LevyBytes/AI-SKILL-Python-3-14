# What’s New In Python 3.8 / typing - typing

### typing

Several fresh capabilities land in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module:

- A dictionary type carrying a separate type per key. Consult [**PEP 589**](https://peps.python.org/pep-0589/) plus [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict). String keys are all that TypedDict accepts. Each key, by default, has to be present. To make keys optional, give "total=False":

```python
class Location(TypedDict, total=False):
    lat_long: tuple
    grid_square: str
    xy_coordinate: tuple

```

- Literal types. Consult [**PEP 586**](https://peps.python.org/pep-0586/) plus [`typing.Literal`](https://docs.python.org/3.14/library/typing.html#typing.Literal). A literal type signals that a parameter or returned value is limited to one or several specific literal values:

```python
def get_status(port: int) -> Literal['connected', 'disconnected']:
    ...

```

- "Final" variables, functions, methods and classes. Consult [**PEP 591**](https://peps.python.org/pep-0591/), [`typing.Final`](https://docs.python.org/3.14/library/typing.html#typing.Final) plus [`typing.final()`](https://docs.python.org/3.14/library/typing.html#typing.final). A static type checker reads the final qualifier as an order to forbid subclassing, overriding, or reassignment:

```python
pi: Final[float] = 3.1415926536

```

- Protocol definitions. Consult [**PEP 544**](https://peps.python.org/pep-0544/), [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) plus [`typing.runtime_checkable()`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable). Straightforward ABCs such as [`typing.SupportsInt`](https://docs.python.org/3.14/library/typing.html#typing.SupportsInt) are henceforth `Protocol` subclasses.

- New protocol class [`typing.SupportsIndex`](https://docs.python.org/3.14/library/typing.html#typing.SupportsIndex).

- New functions [`typing.get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

[Subject index](INDEX.md) · [Previous source section](time.md) · [Next source section](unicodedata.md) · [Release/subject declaration](assignment-expressions.md)
