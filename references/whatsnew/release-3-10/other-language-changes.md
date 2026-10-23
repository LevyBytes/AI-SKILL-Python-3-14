# What's New In Python 3.10 / Other Language Changes - decimal, fractions, types

### Other Language Changes

- A fresh method [`int.bit_count()`](https://docs.python.org/3.14/library/stdtypes.html#int.bit_count) now lives on the [`int`](https://docs.python.org/3.14/library/functions.html#int) type; it reports how many ones appear in an integer's binary form, a value often called the population count. (Contributed by Niklas Fiekas in [bpo-29882](https://bugs.python.org/issue?@action=redirect&bpo=29882).)

- Every view handed back by [`dict.keys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.keys), [`dict.values()`](https://docs.python.org/3.14/library/stdtypes.html#dict.values) and [`dict.items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) now carries a `mapping` attribute yielding a [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) object that wraps the source dictionary. (Contributed by Dennis Sweeney in [bpo-40890](https://bugs.python.org/issue?@action=redirect&bpo=40890).)

- [**PEP 618**](https://peps.python.org/pep-0618/): An optional `strict` flag is now accepted by the [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) function, letting you demand that each iterable share the same length.

- Integer-taking builtin and extension functions will no longer take [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)s, [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)s, or similar objects that convert to integers only with some loss (for instance, those carrying the [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) method yet lacking the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method). (Contributed by Serhiy Storchaka in [bpo-37999](https://bugs.python.org/issue?@action=redirect&bpo=37999).)

- Should [`object.__ipow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ipow__) hand back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented), the operator now properly retreats to [`object.__pow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__pow__) and [`object.__rpow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rpow__) the way you would want. (Contributed by Alex Shkop in [bpo-38302](https://bugs.python.org/issue?@action=redirect&bpo=38302).)

- It is now legal to write assignment expressions without parentheses inside set literals and set comprehensions, and likewise within sequence indexes (though slices remain off-limits).

- A new `__builtins__` attribute on functions now drives the search for builtin symbols whenever a function runs, in place of consulting `__globals__['__builtins__']`. That attribute starts out from `__globals__["__builtins__"]` when present, and otherwise from the builtins in effect at the time. (Contributed by Mark Shannon in [bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990).)

- Two fresh builtin functions – [`aiter()`](https://docs.python.org/3.14/library/functions.html#aiter) and [`anext()`](https://docs.python.org/3.14/library/functions.html#anext) now exist as the asynchronous equivalents of [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) and [`next()`](https://docs.python.org/3.14/library/functions.html#next), one apiece. (Contributed by Joshua Bronson, Daniel Pope, and Justin Wang in [bpo-31861](https://bugs.python.org/issue?@action=redirect&bpo=31861).)

- Both static methods ([`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod)) and class methods ([`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod)) now pick up the method attributes (`__module__`, `__name__`, `__qualname__`, `__doc__`, `__annotations__`) plus a brand-new `__wrapped__` attribute. On top of that, static methods can now be invoked like ordinary functions. (Contributed by Victor Stinner in [bpo-43682](https://bugs.python.org/issue?@action=redirect&bpo=43682).)

- Under `from __future__ import annotations`, annotations placed on complex targets (anything other than the `simple name` targets that [**PEP 526**](https://peps.python.org/pep-0526/) lays out) no longer trigger runtime effects of any kind. (Contributed by Batuhan Taskaya in [bpo-42737](https://bugs.python.org/issue?@action=redirect&bpo=42737).)

- Both class and module objects now build empty annotations dicts lazily, only as needed. For backwards compatibility those annotations dicts sit in the object’s `__dict__`. The upshot is better best practices around `__annotations__`; to dig deeper, consult [Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto). (Contributed by Larry Hastings in [bpo-43901](https://bugs.python.org/issue?@action=redirect&bpo=43901).)

- Because of their side effects, annotations made up of `yield`, `yield from`, `await` or named expressions are now disallowed when `from __future__ import annotations` is active. (Contributed by Batuhan Taskaya in [bpo-42725](https://bugs.python.org/issue?@action=redirect&bpo=42725).)

- Under `from __future__ import annotations`, relying on unbound variables, `super()`, and other expressions capable of changing how the symbol table is processed within annotations now has no effect. (Contributed by Batuhan Taskaya in [bpo-42725](https://bugs.python.org/issue?@action=redirect&bpo=42725).)

- For NaN values, hashes coming from both the [`float`](https://docs.python.org/3.14/library/functions.html#float) type and the [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) type now hinge on object identity. They used to hash uniformly to `0`, despite NaN values never being equal to each other. That behavior could drive roughly quadratic runtimes from too many hash collisions whenever dictionaries and sets held several NaNs. (Contributed by Raymond Hettinger in [bpo-43475](https://bugs.python.org/issue?@action=redirect&bpo=43475).)

- Removing the [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__) constant now triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) rather than a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError). (Contributed by Donghee Na in [bpo-45000](https://bugs.python.org/issue?@action=redirect&bpo=45000).)

- The [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions now carry `end_lineno` and `end_offset` attributes, which are set to `None` whenever they cannot be worked out. (Contributed by Pablo Galindo in [bpo-43914](https://bugs.python.org/issue?@action=redirect&bpo=43914).)

[Subject index](INDEX.md) · [Previous source section](pep-647-user-defined-type-guards.md) · [Next source section](new-modules.md) · [Release/subject declaration](summary-release-highlights.md)
