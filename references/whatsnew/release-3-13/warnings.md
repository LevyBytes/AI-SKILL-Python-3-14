# What's New In Python 3.13 / warnings - warnings

### warnings

- [**PEP 702**](https://peps.python.org/pep-0702/): The added [`warnings.deprecated()`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated) decorator offers a route for signalling deprecations to a [static type checker](https://docs.python.org/3.14/glossary.html#term-static-type-checker) and for warning whenever deprecated classes and functions get used. At runtime a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) can additionally fire when a decorated function or class is invoked. (Contributed by Jelle Zijlstra in [gh-104003](https://github.com/python/cpython/issues/104003).)

[Subject index](INDEX.md) · [Previous source section](venv.md) · [Next source section](xml.md) · [Release/subject declaration](summary-release-highlights.md)
