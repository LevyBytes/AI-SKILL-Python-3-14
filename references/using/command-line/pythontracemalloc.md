# PYTHONTRACEMALLOC

PYTHONTRACEMALLOC

When this environment variable holds a non-empty string, begin tracing Python memory allocations with the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module. The variable's value is the cap on how many frames are kept in a trace's traceback. For instance, `PYTHONTRACEMALLOC=1` keeps only the single most recent frame. Consult the [`tracemalloc.start()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.start) function for further details. This amounts to setting the `-X` `tracemalloc` option.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous source section](pythonfaulthandler.md) · [Following source section](pythonprofileimporttime.md)
