# What's New In Python 3.9 / typing — typing

### typing

[**PEP 593**](https://peps.python.org/pep-0593/) brought in the [`typing.Annotated`](https://docs.python.org/3.14/library/typing.html#typing.Annotated) type for annotating existing types with context-specific metadata, plus a new `include_extras` parameter on [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) that retrieves that metadata at runtime. (Contributed by Till Varoquaux and Konstantin Kashin.)

### Notable changes in Python 3.9.1

### typing

How [`typing.Literal`](https://docs.python.org/3.14/library/typing.html#typing.Literal) behaves was reworked to line up with [**PEP 586**](https://peps.python.org/pep-0586/) and to mirror the static type checker behavior that the PEP lays out.

1.

`Literal` now de-duplicates parameters.

2.

Equality comparisons between `Literal` objects are now order independent.

3.

`Literal` comparisons take types into account from now on. Take `Literal[0] == Literal[False]`: it used to come out as `True`, but it yields `False` these days. Backing that shift, the type cache used behind the scenes can now tell types apart.

4.

During equality comparisons, `Literal` objects from now on throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception whenever one of their parameters isn’t [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). Be aware, though, that spelling out a `Literal` with mutable parameters raises no error:

```python
>>> from typing import Literal
>>> Literal[{0}]
>>> Literal[{0}] == Literal[{False}]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

```

(Contributed by Yurii Karabas in [bpo-42345](https://bugs.python.org/issue?@action=redirect&bpo=42345).)

[Subject index](INDEX.md) · [Previous source section](tracemalloc.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](c-api-changes-removed.md) · [Next source section](macos-11-0-and-apple-silicon-mac-support.md)
