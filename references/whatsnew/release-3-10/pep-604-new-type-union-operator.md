# What's New In Python 3.10 / PEP 604: New Type Union Operator - typing

### PEP 604: New Type Union Operator

A fresh type union operator landed, unlocking the syntax `X | Y`. It offers a tidier route to saying "either type X or type Y" rather than reaching for [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union), particularly within type hints.

Under earlier Python releases, supplying a type hint for functions that take arguments spanning several types meant employing [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union):

```python
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2

```

Now those type hints can be expressed far more compactly:

```python
def square(number: int | float) -> int | float:
    return number ** 2

```

This fresh syntax is likewise taken as the second argument passed to [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass):

```python
>>> isinstance(1, int | str)
True

```

Refer to [Union Type](https://docs.python.org/3.14/library/stdtypes.html#types-union) and [**PEP 604**](https://peps.python.org/pep-0604/) for additional detail.

[Subject index](INDEX.md) · [Previous source section](new-features-related-to-type-hints.md) · [Next source section](pep-612-parameter-specification-variables.md) · [Release/subject declaration](summary-release-highlights.md)
