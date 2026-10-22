# typing: `typing.Protocol`

*class *typing.Protocol(*Generic*)

Base class for protocol classes.

Protocol classes are defined like this:

```python
class Proto(Protocol):
    def meth(self) -> int:
        ...

```

Their main use is alongside static type checkers that understand structural subtyping (static duck-typing), as in:

```python
class C:
    def meth(self) -> int:
        return 0

def func(x: Proto) -> int:
    return x.meth()

func(C())  # Passes static type check

```

Consult [**PEP 544**](https://peps.python.org/pep-0544/) for further detail. When a protocol class carries the `runtime_checkable()` decorator (covered below), it behaves as a simple-minded runtime protocol that verifies only that the named attributes are present, paying no attention to their type signatures. A protocol class lacking that decorator may not be passed as the second argument of [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) or [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass).

Protocol classes can be generic, for example:

```python
class GenProto[T](Protocol):
    def meth(self) -> T:
        ...

```

Where compatibility with Python 3.11 or earlier matters, generic Protocols may instead be spelled this way:

```python
T = TypeVar("T")

class GenProto(Protocol[T]):
    def meth(self) -> T:
        ...

```

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](typing-newtype-class.md) · [Continue](other-special-directives-closable-and-named.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
