# typing - User-defined generic types - Contract: Other classes may serve as bases for generic classes as well:

Other classes may serve as bases for generic classes as well:

```python
from collections.abc import Sized

class LinkedList[T](Sized):
    ...

```

A subclass that inherits from a generic class may pin down some of its type parameters:

```python
from collections.abc import Mapping

class MyDict[T](Mapping[str, T]):
    ...

```

So `MyDict` here carries one parameter, `T`.

If you use a generic class but leave its type parameters unspecified, each slot is taken to be `Any`. In the example that follows, `MyIterable` is itself not generic but inherits implicitly from `Iterable[Any]`:

```python
from collections.abc import Iterable

class MyIterable(Iterable): # Same as Iterable[Any]
    ...

```

User-defined generic type aliases work too. For example:

```python
from collections.abc import Iterable

type Response[S] = Iterable[S] | int

# Return type here is same as Iterable[str] | int
def response(query: str) -> Response[str]:
    ...

type Vec[T] = Iterable[tuple[T, T]]

def inproduct[T: (int, float, complex)](v: Vec[T]) -> T: # Same as Iterable[tuple[T, T]]
    return sum(x*y for x, y in v)

```

To preserve backward compatibility, a generic type alias can equally be made via plain assignment:

```python
from collections.abc import Iterable
from typing import TypeVar

S = TypeVar("S")
Response = Iterable[S] | int

```

Changed in version 3.7: `Generic` no longer has a custom metaclass.

Changed in version 3.12: Dedicated syntax covering both generics and type aliases first appeared in version 3.12. Before that, a generic class had to either inherit from `Generic` outright or hold a type variable somewhere among its bases.

Parameter specification variables of the form `[**P]` likewise let you write user-defined generics over parameter expressions. The `typing` module treats a parameter specification variable as a specialised kind of type variable, so behaviour matches the type variables covered above. The lone difference is that a list of types may substitute for a `ParamSpec`:

```python
>>> class Z[T, **P]: ...  # T is a TypeVar; P is a ParamSpec
...
>>> Z[int, [dict, float]]
__main__.Z[int, [dict, float]]

```

You can equally build classes generic over a `ParamSpec` by inheriting explicitly from `Generic`, in which case `**` is omitted:

[Subject index](INDEX.md) · [Previous](user-defined-generics-overview.md) · [Continue](paramspec-generic-class-example.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: User-defined generic types](user-defined-generics-overview.md)
