# Python 3.8.0 alpha 1 / core and builtins / gc

[bpo-33622](https://bugs.python.org/issue?@action=redirect&bpo=33622): Resolved a leak that occurred when the garbage collector could not add an object carrying a `__del__` method, or referenced by one, into the [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage) list. [`PyGC_Collect()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Collect) may now run while an exception is set, and it keeps that exception intact.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
