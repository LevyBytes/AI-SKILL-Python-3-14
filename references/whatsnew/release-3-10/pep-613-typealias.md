# What's New In Python 3.10 / PEP 613: TypeAlias - typing

### PEP 613: TypeAlias

The notion of type aliases came in with [**PEP 484**](https://peps.python.org/pep-0484/), which only insisted that they be top-level assignments carrying no annotation. That bareness occasionally left type checkers unable to tell a type alias apart from a plain assignment, particularly once forward references or invalid types entered the picture. Contrast these:

```python
StrCache = 'Cache[str]'  # a type alias
LOG_PREFIX = 'LOG[DEBUG]'  # a module constant

```

These days the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module ships a dedicated value [`TypeAlias`](https://docs.python.org/3.14/library/typing.html#typing.TypeAlias), giving you a more explicit way to spell out type aliases:

```python
StrCache: TypeAlias = 'Cache[str]'  # a type alias
LOG_PREFIX = 'LOG[DEBUG]'  # a module constant

```

Consult [**PEP 613**](https://peps.python.org/pep-0613/) if you want the full picture.

(Contributed by Mikhail Golubev in [bpo-41923](https://bugs.python.org/issue?@action=redirect&bpo=41923).)

[Subject index](INDEX.md) · [Previous source section](pep-612-parameter-specification-variables.md) · [Next source section](pep-647-user-defined-type-guards.md) · [Release/subject declaration](summary-release-highlights.md)
