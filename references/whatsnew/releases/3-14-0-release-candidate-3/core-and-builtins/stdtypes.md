# Python 3.14.0 release candidate 3 / core and builtins / stdtypes

[gh-138479](https://github.com/python/cpython/issues/138479): Stop a crash triggered when a generic object’s `__typing_subst__` hands back something that is not a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

[gh-138318](https://github.com/python/cpython/issues/138318): When built-in names (such as [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`format()`](https://docs.python.org/3.14/library/functions.html#format)) appear as attribute names (for example in `value.set` or `text.format`), the default REPL now refrains from highlighting them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
