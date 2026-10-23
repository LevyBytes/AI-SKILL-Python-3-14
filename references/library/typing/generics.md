# typing - Generics

### Generics

Type information about the objects held inside containers can't be deduced statically in any general fashion, so the standard library lets many container classes be subscripted to spell out the element types they are expected to hold.

```python
from collections.abc import Mapping, Sequence

class Employee: ...

# Sequence[Employee] indicates that all elements in the sequence
# must be instances of "Employee".
# Mapping[str, str] indicates that all keys and all values in the mapping
# must be strings.
def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: ...

```

To make functions and classes generic, use the [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) to parameterize them:

```python
from collections.abc import Sequence

def first[T](l: Sequence[T]) -> T:  # Function is generic over the TypeVar "T"
    return l[0]

```

Or invoke the `TypeVar` factory yourself:

```python
from collections.abc import Sequence
from typing import TypeVar

U = TypeVar('U')                  # Declare type variable "U"

def second(l: Sequence[U]) -> U:  # Function is generic over the TypeVar "U"
    return l[1]

```

Changed in version 3.12: The dedicated syntax for generics arrived with Python 3.12.

[Subject index](INDEX.md) · [Previous](annotating-callable-objects.md) · [Continue](annotating-tuples.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
