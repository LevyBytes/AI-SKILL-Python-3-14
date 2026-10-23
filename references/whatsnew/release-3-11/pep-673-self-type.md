# What's New In Python 3.11 / PEP 673: `Self` type - typing

> (Contributed by David Foster and Jelle Zijlstra in [bpo-47087](https://bugs.python.org/issue?@action=redirect&bpo=47087). PEP written by David Foster.)

### PEP 673: `Self` type

The fresh [`Self`](https://docs.python.org/3.14/library/typing.html#typing.Self) annotation offers a clear, intuitive route to annotating methods whose return value is an instance of the class they belong to. It carries the same meaning as the [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar)-driven pattern [**specified in PEP 484**](https://peps.python.org/pep-0484/#annotating-instance-and-class-methods), yet reads more compactly and clearly.

Typical scenarios cover alternative constructors exposed as [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod)s, plus [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) methods handing back `self`:

```python
class MyLock:
    def __enter__(self) -> Self:
        self.lock()
        return self

    ...

class MyInt:
    @classmethod
    def fromhex(cls, s: str) -> Self:
        return cls(int(s, 16))

    ...

```

You may also apply [`Self`](https://docs.python.org/3.14/library/typing.html#typing.Self) to method parameters or attributes whose type matches the class they live in.

Consult [**PEP 673**](https://peps.python.org/pep-0673/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep655-required-and-optional-typeddict-items.md) · [Next source section](pep-675-arbitrary-literal-string-type.md) · [Release/subject declaration](summary-release-highlights.md)
