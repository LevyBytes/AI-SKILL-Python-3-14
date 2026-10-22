# What's New In Python 3.11 / functools — functools, types, typing

### functools

- [`functools.singledispatch()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatch) now accepts [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) and [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) as annotations on the dispatched argument.:

```python
>>> from functools import singledispatch
>>> @singledispatch
... def fun(arg, verbose=False):
...     if verbose:
...         print("Let me just say,", end=" ")
...     print(arg)
...
>>> @fun.register
... def _(arg: int | float, verbose=False):
...     if verbose:
...         print("Strength in numbers, eh?", end=" ")
...     print(arg)
...
>>> from typing import Union
>>> @fun.register
... def _(arg: Union[list, set], verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)
...

```

(Contributed by Yurii Karabas in [bpo-46014](https://bugs.python.org/issue?@action=redirect&bpo=46014).)

[Subject index](INDEX.md) · [Previous source section](fractions.md) · [Next source section](gzip.md) · [Release/subject declaration](summary-release-highlights.md)
