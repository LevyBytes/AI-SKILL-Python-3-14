# Python 3.6.4 release candidate 1 / core and builtins / functions and types

[bpo-31311](https://bugs.python.org/issue?@action=redirect&bpo=31311): Repair a crash within the `__setstate__()` method of `ctypes._CData` triggered by a bad `__dict__`. Oren Milman wrote the patch.

[bpo-31285](https://bugs.python.org/issue?@action=redirect&bpo=31285): Repair an assertion failure inside `warnings.warn_explicit` that happens when the value returned by the loader’s `get_source()` carries a bad `splitlines()` method. Oren Milman wrote the patch.

[bpo-31588](https://bugs.python.org/issue?@action=redirect&bpo=31588): Throw a `TypeError` carrying a useful message when class creation breaks because a metaclass has a bad `__prepare__()` method. Oren Milman wrote the patch.

[bpo-31478](https://bugs.python.org/issue?@action=redirect&bpo=31478): Repair an assertion failure inside `_random.Random.seed()` triggered when the argument carries a bad `__abs__()` method. Oren Milman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
