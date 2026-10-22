# Python 3.14.1 final / core and builtins / threading

[gh-137433](https://github.com/python/cpython/issues/137433): Resolve a possible deadlock within the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build whenever daemon threads turn profiling or tracing on or off as the main thread is closing down the interpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
