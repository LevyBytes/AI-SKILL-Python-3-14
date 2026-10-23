# What’s New In Python 3.12 / PEP 698: Override Decorator for Static Typing - typing

### PEP 698: Override Decorator for Static Typing

The [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module gains a new decorator, [`typing.override()`](https://docs.python.org/3.14/library/typing.html#typing.override). It signals to type checkers that the method is meant to override one in a superclass. With this, type checkers can flag errors where a method written to override something in a base class actually fails to do so.

Example:

```python
from typing import override

class Base:
  def get_color(self) -> str:
    return "blue"

class GoodChild(Base):
  @override  # ok: overrides Base.get_color
  def get_color(self) -> str:
    return "yellow"

class BadChild(Base):
  @override  # type checker error: does not override Base.get_color
  def get_colour(self) -> str:
    return "red"

```

See [**PEP 698**](https://peps.python.org/pep-0698/) for more details.

(Contributed by Steven Troxler in [gh-101561](https://github.com/python/cpython/issues/101561).)

[Subject index](INDEX.md) · [Previous source section](pep-692-using-typeddict-for-more-precise-kwargs-typing.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
