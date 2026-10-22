# Python 3.14.3 final / core and builtins / contextvars

[gh-142829](https://github.com/python/cpython/issues/142829): Address a use-after-free crash during [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) comparison that happened when a custom `__eq__` method changed the context through [`set()`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar.set).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
