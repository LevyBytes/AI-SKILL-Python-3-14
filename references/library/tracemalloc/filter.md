# tracemalloc: Filter address-space selection

domain

Address space of a memory block (`int` or `None`).

tracemalloc reserves domain `0` for the memory allocations Python makes. Other domains are available to C extensions for tracing different resources.

 inclusive

When *inclusive* is `True` (include), match only those memory blocks allocated in a file whose name matches `filename_pattern` at line number `lineno`.

When *inclusive* is `False` (exclude), skip memory blocks allocated in a file whose name matches `filename_pattern` at line number `lineno`.

 lineno

Line number (`int`) the filter targets. When *lineno* is `None`, the filter applies to every line number.

 filename_pattern

Filename pattern of the filter (`str`). Read-only property.

 all_frames

When *all_frames* is `True`, every frame in the traceback is examined. When *all_frames* is `False`, only the single most recent frame is examined.

The attribute is inert whenever the traceback limit is `1`. See the `get_traceback_limit()` function and the `Snapshot.traceback_limit` attribute.

[Subject index](INDEX.md) · [Previous](tracemalloc-filter-class.md) · [Continue](tracemalloc-frame-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md) · [Owning module, declaration or section: tracemalloc.Filter](tracemalloc-filter-class.md) · [Owning module, declaration or section: Filter](tracemalloc-filter-class.md)
