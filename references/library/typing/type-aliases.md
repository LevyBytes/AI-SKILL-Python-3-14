# typing — Type aliases

### Type aliases

You declare a type alias with the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement, which produces a `TypeAliasType` instance. Below, static type checkers regard `Vector` and `list[float]` as interchangeable:

```python
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])

```

Where type signatures grow complicated, aliases help cut them down. As an illustration:

```python
from collections.abc import Sequence

type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
    message: str,
    servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
) -> None:
    ...

```

Python 3.12 introduced the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement. So that older code keeps working, you may instead build a type alias by plain assignment:

```python
Vector = list[float]

```

Alternatively, tag it with `TypeAlias` to signal that the binding is a type alias rather than an ordinary variable:

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]

```

[Subject index](INDEX.md) · [Previous](specification-for-the-python-type-system.md) · [Continue](newtype.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
