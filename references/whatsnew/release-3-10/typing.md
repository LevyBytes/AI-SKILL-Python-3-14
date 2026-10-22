# What's New In Python 3.10 / typing — typing

### typing

For major changes, see New Features Related to Type Hints.

[`typing.Literal`](https://docs.python.org/3.14/library/typing.html#typing.Literal) had its behavior altered so it lines up with [**PEP 586**](https://peps.python.org/pep-0586/) and matches how the static type checkers described in the PEP behave.

1.

`Literal` now de-duplicates parameters.

2.

Equality comparisons between `Literal` objects are now order independent.

3.

Types are now honored when `Literal` comparisons run. As an illustration, `Literal[0] == Literal[False]` used to yield `True`, whereas the result is now `False`. Enabling this required the internal type cache to gain the ability to tell types apart.

4.

During an equality comparison, `Literal` objects will from now on raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception should any of their parameters fail to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). Be aware that merely declaring a `Literal` whose parameters are unhashable triggers no error:

```python
>>> from typing import Literal
>>> Literal[{0}]
>>> Literal[{0}] == Literal[{False}]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

```

(Contributed by Yurii Karabas in [bpo-42345](https://bugs.python.org/issue?@action=redirect&bpo=42345).)

Add new function [`typing.is_typeddict()`](https://docs.python.org/3.14/library/typing.html#typing.is_typeddict), letting you check whether a given annotation happens to be a [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict). (Contributed by Patrick Reader in [bpo-41792](https://bugs.python.org/issue?@action=redirect&bpo=41792).)

Subclasses of `typing.Protocol` that declare only data variables will from now on raise a `TypeError` when an `isinstance` check runs against them, unless the [`runtime_checkable()`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) decorator has been applied. Earlier, such checks succeeded without comment. Anyone wanting runtime protocols should mark their subclasses with the `runtime_checkable()` decorator. (Contributed by Yurii Karabas in [bpo-38908](https://bugs.python.org/issue?@action=redirect&bpo=38908).)

Pulling anything in from the `typing.io` and `typing.re` submodules will from now on emit [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Those submodules have carried deprecated status since Python 3.8 and a later Python release will drop them. Whatever lives in those submodules ought to be imported straight from [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) instead. (Contributed by Sebastian Rittau in [bpo-38291](https://bugs.python.org/issue?@action=redirect&bpo=38291).)

[Subject index](INDEX.md) · [Previous source section](types.md) · [Next source section](unittest.md) · [Release/subject declaration](summary-release-highlights.md)
