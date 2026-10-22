# Python 3.7.0 alpha 2 / core and builtins / functions and types

[bpo-31311](https://bugs.python.org/issue?@action=redirect&bpo=31311): Repair a crash within the `__setstate__()` method of `ctypes._CData` whenever the `__dict__` is bad. Oren Milman wrote the patch.

[bpo-31285](https://bugs.python.org/issue?@action=redirect&bpo=31285): Repair an assertion failure in `warnings.warn_explicit` whenever the value returned by the loader's `get_source()` carries a bad `splitlines()` method. Oren Milman wrote the patch.

[bpo-31478](https://bugs.python.org/issue?@action=redirect&bpo=31478): Repair an assertion failure within `_random.Random.seed()` whenever the argument carries a bad `__abs__()` method. Oren Milman wrote the patch.

[bpo-31336](https://bugs.python.org/issue?@action=redirect&bpo=31336): Make class creation 10-20% faster by trimming the overhead in the required special method lookups. Stefan Behnel wrote the patch.

[bpo-31410](https://bugs.python.org/issue?@action=redirect&bpo=31410): Wrapper and classmethod descriptor calls were optimized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
