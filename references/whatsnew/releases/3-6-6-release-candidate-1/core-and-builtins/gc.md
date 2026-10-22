# Python 3.6.6 release candidate 1 / core and builtins / gc

[bpo-33622](https://bugs.python.org/issue?@action=redirect&bpo=33622): Plugged a leak that occurred whenever the garbage collector could not place an object carrying the `__del__` method ? or referenced by such an object ? into the [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage) list. It is now valid to invoke [`PyGC_Collect()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Collect) while an exception is set, and that exception is preserved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
