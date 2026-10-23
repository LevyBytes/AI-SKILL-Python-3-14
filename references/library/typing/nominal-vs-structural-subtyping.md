# typing - Nominal vs structural subtyping

### Nominal vs structural subtyping

At the outset, [**PEP 484**](https://peps.python.org/pep-0484/) specified Python's static type system in terms of *nominal subtyping*. Under this rule, a class `A` is permitted in place of a class `B` exactly when `A` derives from `B`.

That same rule used to cover abstract base classes too, [`Iterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable) among them. The downside here is that a class needed an explicit declaration to be recognized for them, which feels unpythonic and runs against how one would ordinarily write idiomatic dynamically typed Python. As an example, the following satisfies [**PEP 484**](https://peps.python.org/pep-0484/):

```python
from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

```

[**PEP 544**](https://peps.python.org/pep-0544/) addresses this by letting authors write the same code without naming base classes in the class header, so that static type checkers can implicitly regard `Bucket` as a subtype of both `Sized` and `Iterable[int]`. The term for this is *structural subtyping* (or static duck-typing):

```python
from collections.abc import Iterator, Iterable

class Bucket:  # Note: no base classes
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result = collect(Bucket())  # Passes type check

```

Beyond that, by deriving from a dedicated class `Protocol`, an author can declare brand-new custom protocols and take full advantage of structural subtyping (examples appear below).

[Subject index](INDEX.md) · [Previous](the-any-type.md) · [Continue](module-contents.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
