# typing: `typing.Unpack`

typing.Unpack

Typing operator to conceptually mark an object as having been unpacked.

As an example, applying the unpack operator `*` to a type variable tuple amounts to the same thing as using `Unpack` to flag the type variable tuple as already unpacked:

```python
Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]
# Effectively does:
tup: tuple[Unpack[Ts]]

```

Indeed, within the setting of `typing.TypeVarTuple` and [`builtins.tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) types, `Unpack` and `*` may be swapped freely. Explicit use of `Unpack` tends to show up in earlier Python releases, where `*` was not permitted in certain positions:

```python
# In older versions of Python, TypeVarTuple and Unpack
# are located in the `typing_extensions` backports package.
from typing_extensions import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]         # Syntax error on Python <= 3.10!
tup: tuple[Unpack[Ts]]  # Semantically equivalent, and backwards-compatible

```

It is likewise possible to pair `Unpack` with `typing.TypedDict` so as to type `**kwargs` within a function signature:

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
    name: str
    year: int

# This function expects two keyword arguments - `name` of type `str`
# and `year` of type `int`.
def foo(**kwargs: Unpack[Movie]): ...

```

Refer to [**PEP 692**](https://peps.python.org/pep-0692/) for more on applying `Unpack` to `**kwargs` typing.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](typing-typeguard.md) · [Continue](typing-generic-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
