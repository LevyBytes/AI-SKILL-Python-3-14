# Python 3.6.0 alpha 1 / core and builtins / tracemalloc

[bpo-26564](https://bugs.python.org/issue?@action=redirect&bpo=26564): When an error arises, the debug hooks belonging to Python memory allocators now consult the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module to recover the traceback marking where a given memory block had been allocated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
