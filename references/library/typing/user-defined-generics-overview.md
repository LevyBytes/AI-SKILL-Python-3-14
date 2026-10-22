# typing — User-defined generic types — Section introduction and initial examples

### User-defined generic types

Your own class can be declared as a generic class.

```python
from logging import Logger

class LoggedVar[T]:
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

```

That notation conveys that class `LoggedVar` is parameterised over one type variable `T`. It additionally lets `T` serve as a type throughout the class body.

A generic class inherits from `Generic` implicitly. To stay compatible with Python 3.11 and earlier, you can also spell out that inheritance from `Generic` explicitly to denote a generic class:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class LoggedVar(Generic[T]):
    ...

```

Because generic classes carry [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) methods, they admit parameterisation at runtime (for example `LoggedVar[int]` below):

```python
from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

```

There is no cap on how many type variables a generic type may carry. Every flavour of `TypeVar` is allowed as a parameter to a generic type:

```python
from typing import TypeVar, Generic, Sequence

class WeirdTrio[T, B: Sequence[bytes], S: (int, str)]:
    ...

OldT = TypeVar('OldT', contravariant=True)
OldB = TypeVar('OldB', bound=Sequence[bytes], covariant=True)
OldS = TypeVar('OldS', int, str)

class OldWeirdTrio(Generic[OldT, OldB, OldS]):
    ...

```

Every type variable handed to `Generic` has to be unique, which makes the following illegal:

```python
from typing import TypeVar, Generic
...

class Pair[M, M]:  # SyntaxError
    ...

T = TypeVar('T')

class Pair(Generic[T, T]):   # INVALID
    ...

```

[Subject index](INDEX.md) · [Previous](annotating-generators-and-coroutines.md) · [Continue](generic-class-inheritance-contract.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
