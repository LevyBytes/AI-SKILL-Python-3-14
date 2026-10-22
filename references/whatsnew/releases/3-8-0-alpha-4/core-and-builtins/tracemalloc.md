# Python 3.8.0 alpha 4 / core and builtins / tracemalloc

[bpo-36611](https://bugs.python.org/issue?@action=redirect&bpo=36611): Debug memory allocators: the serialno field is now switched off by default in the debug hooks for Python memory allocators, trimming memory usage by 5%. Turn on [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) so that, when a fatal memory fault is reported, you can obtain the traceback of where the block came from and choose a breakpoint location. To restore the field, build Python with `PYMEM_DEBUG_SERIALNO` defined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
