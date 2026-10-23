# What's new in Python 3.14 / typing - types, typing

### typing

- The pair of types [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) and [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) have become aliases of one another, so both old-style unions (built with `Union[int, str]`) and new-style unions (`int | str`) now yield instances of one shared runtime type. That harmonizes how the two syntaxes act, yet it introduces several behavioral shifts that can matter for anyone who inspects types while a program runs:

  - Either syntax for assembling a union now yields an identical string form in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr). To illustrate, `repr(Union[int, str])` now reads `"int | str"` rather than `"typing.Union[int, str]"`.

  - Unions built through the older syntax are no longer cached. Earlier, evaluating `Union[int, str]` repeatedly handed back the very same object (`Union[int, str] is Union[int, str]` evaluated to `True`), whereas now you get two separate objects. Compare unions for equality with `==` rather than `is`. New-style unions were never cached in that manner. The shift might raise memory consumption for certain programs that rely on many unions built by subscripting `typing.Union`. Still, a handful of counterbalancing factors apply: per [**PEP 649**](https://peps.python.org/pep-0649/), unions appearing in annotations are no longer evaluated by default under Python 3.14; an instance of [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) is itself far smaller than whatever `Union[]` previously produced on earlier Python releases; and dropping the cache reclaims some space as well. Consequently it is improbable that the shift will meaningfully grow memory consumption for the majority of users.

  - Earlier, old-style unions relied on the private class `typing._UnionGenericAlias`. The implementation no longer requires that class, though it stays around for backward compatibility, slated to be dropped in Python 3.17. Rather than depending on private implementation internals, callers should reach for documented introspection helpers such as [`get_origin()`](https://docs.python.org/3.14/library/typing.html#typing.get_origin) and [`typing.get_args()`](https://docs.python.org/3.14/library/typing.html#typing.get_args).

  - You may now pass [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) itself into [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks. As an example, `isinstance(int | str, typing.Union)` yields `True`; formerly that raised [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

  - On [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) objects, the `__args__` attribute can no longer be written.

  - Setting attributes of any kind on [`Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) objects is no longer permitted. Previously this functioned solely for dunder attributes, was never documented as supported, and behaved in subtly broken ways across many situations.

(Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499).)

- [`TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType) gains support for star unpacking.

[Subject index](INDEX.md) · [Previous source section](types.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)
