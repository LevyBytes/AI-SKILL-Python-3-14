# tracemalloc: `tracemalloc.Traceback`

### Traceback

 *class *tracemalloc.Traceback

A sequence of `Frame` instances ordered from the oldest frame through to the most recent frame.

Every traceback holds a minimum of `1` frame. When the `tracemalloc` module cannot obtain a frame, it substitutes the filename `"<unknown>"` at line number `0`.

At the moment a snapshot is captured, the tracebacks of its traces are capped at `get_traceback_limit()` frames. See the `take_snapshot()` function. The traceback's original frame count is preserved in the `Traceback.total_nframe` attribute, letting you tell whether the traceback limit truncated a traceback.

The `Trace.traceback` attribute is a `Traceback` instance.

Changed in version 3.7: The ordering of frames now runs oldest-to-newest, a reversal of the former newest-to-oldest arrangement.

[Subject index](INDEX.md) · [Previous](trace.md) · [Continue](tracemalloc-traceback-format.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
