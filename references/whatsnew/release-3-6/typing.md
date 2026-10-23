# What's New In Python 3.6 / typing - collections.abc, contextlib, typing

### typing

Because the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module remains [provisional](https://docs.python.org/3.14/glossary.html#term-provisional-API), every modification landed in Python 3.6 was also backported into the Python 3.5.x line.

The [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module gained considerably better handling of generic type aliases. To illustrate, `Dict[str, Tuple[S, T]]` now counts as a legal type annotation. (Contributed by Guido van Rossum in [Github #195](https://github.com/python/typing/pull/195).)

A [`typing.ContextManager`](https://docs.python.org/3.14/library/typing.html#typing.ContextManager) class was introduced to represent [`contextlib.AbstractContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractContextManager). (Contributed by Brett Cannon in [bpo-25609](https://bugs.python.org/issue?@action=redirect&bpo=25609).)

A [`typing.Collection`](https://docs.python.org/3.14/library/typing.html#typing.Collection) class was introduced to represent [`collections.abc.Collection`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Collection). (Contributed by Ivan Levkivskyi in [bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598).)

The [`typing.ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar) type construct now exists so that class variables can be flagged. Per [**PEP 526**](https://peps.python.org/pep-0526/), an annotation on a variable enclosed by ClassVar signals that the attribute in question is meant to serve as a class variable rather than being assigned on instances of the class. (Contributed by Ivan Levkivskyi in [Github #280](https://github.com/python/typing/pull/280).)

A fresh [`TYPE_CHECKING`](https://docs.python.org/3.14/library/typing.html#typing.TYPE_CHECKING) constant exists, which static type checkers treat as `True`, yet evaluates to `False` while the program executes. (Contributed by Guido van Rossum in [Github #230](https://github.com/python/typing/issues/230).)

A fresh [`NewType()`](https://docs.python.org/3.14/library/typing.html#typing.NewType) helper function arrived for producing lightweight, distinct types meant for annotations:

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)

```

For purposes of static checking, the freshly minted type is handled as though it subclassed the original. (Contributed by Ivan Levkivskyi in [Github #189](https://github.com/python/typing/issues/189).)

[Subject index](INDEX.md) · [Previous source section](tracemalloc.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)
