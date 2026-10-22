# What’s New In Python 3.12 / PEP 692: Using `TypedDict` for more precise `**kwargs` typing

### PEP 692: Using `TypedDict` for more precise `**kwargs` typing

Annotating `**kwargs` within a function signature, as brought in by [**PEP 484**](https://peps.python.org/pep-0484/), produced valid annotations only when every one of the `**kwargs` shared one type.

[**PEP 692**](https://peps.python.org/pep-0692/) lays out a sharper approach to typing `**kwargs` that leans on typed dictionaries:

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
  name: str
  year: int

def foo(**kwargs: Unpack[Movie]): ...

```

See [**PEP 692**](https://peps.python.org/pep-0692/) for more details.

(Contributed by Franek Magiera in [gh-103629](https://github.com/python/cpython/issues/103629).)

[Subject index](INDEX.md) · [Previous source section](new-features-related-to-type-hints.md) · [Next source section](pep-698-override-decorator-for-static-typing.md) · [Release/subject declaration](summary-release-highlights.md)
