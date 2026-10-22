# What's New In Python 3.9 / collections.abc — collections.abc, types, typing

### Notable changes in Python 3.9.2

### collections.abc

The [`collections.abc.Callable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable) generic from now on flattens its type parameters, much as [`typing.Callable`](https://docs.python.org/3.14/library/typing.html#typing.Callable) already does. What that comes to is `collections.abc.Callable[[int, str], str]` ending up with `__args__` equal to `(int, str, str)`, where before it read `([int, str], str)`. Enabling the change, [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias) can now be subclassed, and subscripting the `collections.abc.Callable` type hands back such a subclass. Any code that pulls the arguments out through [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args) or `__args__` has to adapt to this. Invalid ways of parameterizing `collections.abc.Callable` — ones that may have slipped by quietly in Python 3.9.1 — can now trigger a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Come Python 3.10, that `DeprecationWarning` graduates to a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). (Contributed by Ken Jin in [bpo-42195](https://bugs.python.org/issue?@action=redirect&bpo=42195).)

[Subject index](INDEX.md) · [Previous source section](macos-11-0-and-apple-silicon-mac-support.md) · [Next source section](urllib-parse.md) · [Release/subject declaration](summary-release-highlights.md)
