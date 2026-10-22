# sys.getallocatedblocks

sys.getallocatedblocks()

Report how many memory blocks the interpreter currently holds allocated, no matter what size each is. The function chiefly helps when you are tracing and debugging memory leaks. Owing to the interpreter's internal caches, the figure may differ between successive calls; you might need to invoke `_clear_internal_caches()` and [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) to obtain steadier numbers.

When a particular Python build or implementation has no practical way to compute this figure, `getallocatedblocks()` may return 0 in its place.

Added in version 3.4.

[API family](INDEX.md) · [sys context index](../INDEX.md).
