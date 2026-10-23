# What’s New In Python 3.12 / typing - inspect, typing

### typing

- When [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) is run against [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable), the attribute-existence check now goes through [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static) in place of [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr). Consequently, descriptors and [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) methods will no longer fire unexpectedly while an `isinstance()` test runs against a runtime-checkable protocol. The flip side is that, on Python 3.12+, an object once treated as an instance of such a protocol might no longer qualify, and the reverse can happen too. The change should leave most users unaffected. (Contributed by Alex Waygood in [gh-102433](https://github.com/python/cpython/issues/102433).)

- Once the class is built, a runtime-checkable protocol's members are now treated as "frozen" at runtime. You can still monkey-patch attributes onto such a protocol, yet doing so will not change the outcome of [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests that compare objects against it. Here is an illustration:

```python
>>> from typing import Protocol, runtime_checkable
>>> @runtime_checkable
... class HasX(Protocol):
...     x = 1
...
>>> class Foo: ...
...
>>> f = Foo()
>>> isinstance(f, HasX)
False
>>> f.x = 1
>>> isinstance(f, HasX)
True
>>> HasX.y = 2
>>> isinstance(f, HasX)  # unchanged, even though HasX now also has a "y" attribute
True

```

The motivation for this adjustment was to accelerate `isinstance()` tests against runtime-checkable protocols.

- How [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests perform against [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) has shifted markedly. Against protocols that declare only a handful of members, most `isinstance()` tests ought to run at least 2x quicker than they did in 3.11, with some running 20x faster or beyond. That said, when a protocol carries many members, an `isinstance()` test against it might run slower than under Python 3.11. (Contributed by Alex Waygood in [gh-74690](https://github.com/python/cpython/issues/74690) and [gh-103193](https://github.com/python/cpython/issues/103193).)

- The `__orig_bases__` attribute is now present on every [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) and [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class. (Contributed by Adrian Garcia Badaracco in [gh-103699](https://github.com/python/cpython/issues/103699).)

- A `frozen_default` parameter is now part of [`typing.dataclass_transform()`](https://docs.python.org/3.14/library/typing.html#typing.dataclass_transform). (Contributed by Erik De Bonte in [gh-99957](https://github.com/python/cpython/issues/99957).)

[Subject index](INDEX.md) · [Previous source section](types.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)
