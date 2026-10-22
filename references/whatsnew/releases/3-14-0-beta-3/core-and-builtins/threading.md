# Python 3.14.0 beta 3 / core and builtins / threading

[gh-134679](https://github.com/python/cpython/issues/134679): Resolve a crash inside the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build's QSBR code that was triggerable while an object's `__dict__` attribute was being swapped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
