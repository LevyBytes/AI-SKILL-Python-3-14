# What's new in Python 3.14 / Built-ins - copy, pickle

### Built-ins

- ASCII [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) along with [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) are now accepted by the [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) and [`bytearray.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.fromhex) methods. (Contributed by Daniel Pope in [gh-129349](https://github.com/python/cpython/issues/129349).)

- Two new class methods, [`float.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#float.from_number) and [`complex.from_number()`](https://docs.python.org/3.14/library/stdtypes.html#complex.from_number), now turn a number into the [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`complex`](https://docs.python.org/3.14/library/functions.html#complex) type respectively. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised when the argument fails to be a real number. (Contributed by Serhiy Storchaka in [gh-84978](https://github.com/python/cpython/issues/84978).)

- Within the fractional part of floating-point presentation types in new-style string formatting (whether via [`format()`](https://docs.python.org/3.14/library/functions.html#format) or [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings)), both underscore and comma are now permitted as thousands separators. (Contributed by Sergey B Kirpichev in [gh-87790](https://github.com/python/cpython/issues/87790).)

- Delegation to [`__trunc__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__trunc__) by the [`int()`](https://docs.python.org/3.14/library/functions.html#int) function has ended. A class seeking to allow conversion to `int()` is required to provide either [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) or [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__). (Contributed by Mark Dickinson in [gh-119743](https://github.com/python/cpython/issues/119743).)

- Just like [`zip()`](https://docs.python.org/3.14/library/functions.html#zip), the [`map()`](https://docs.python.org/3.14/library/functions.html#map) function now offers an optional keyword-only *strict* flag that verifies every iterable shares an equal length. (Contributed by Wannes Boeykens in [gh-119793](https://github.com/python/cpython/issues/119793).)

- Subscription is now available on the [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) type, turning it into a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type). (Contributed by Brian Schubert in [gh-126012](https://github.com/python/cpython/issues/126012).)

- A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) will now be raised by employing [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) within a boolean context. Since Python 3.9 this had been raising a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Jelle Zijlstra in [gh-118767](https://github.com/python/cpython/issues/118767).)

- When required, three-argument [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) now attempts a call to [`__rpow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rpow__). Up to now that call happened only for two-argument `pow()` and the binary power operator. (Contributed by Serhiy Storchaka in [gh-130104](https://github.com/python/cpython/issues/130104).)

- It is now possible to make [`super`](https://docs.python.org/3.14/library/functions.html#super) objects [`copyable`](https://docs.python.org/3.14/library/copy.html#module-copy) and [`pickleable`](https://docs.python.org/3.14/library/pickle.html#module-pickle). (Contributed by Serhiy Storchaka in [gh-125767](https://github.com/python/cpython/issues/125767).)

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](command-line-and-environment.md) · [Release/subject declaration](summary-release-highlights.md)
