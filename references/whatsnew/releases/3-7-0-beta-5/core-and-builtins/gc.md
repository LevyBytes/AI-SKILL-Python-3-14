# Python 3.7.0 beta 5 / core and builtins / gc

[bpo-33622](https://bugs.python.org/issue?@action=redirect&bpo=33622): Repaired a leak occurring when the garbage collector cannot move an object owning a `__del__` method, or referenced from one, into the [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage) list. [`PyGC_Collect()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyGC_Collect) may now run while an exception is set and keeps it intact.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
