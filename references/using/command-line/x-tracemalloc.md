# -X tracemalloc

- `-X tracemalloc` to begin tracing Python memory allocations by means of the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module. By default a trace's traceback retains only the most recent frame. Pass `-X tracemalloc=NFRAME` to begin tracing with a traceback capped at *NFRAME* frames. Consult [`tracemalloc.start()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.start) and `PYTHONTRACEMALLOC` for further details.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous source section](x-showrefcount.md) · [Following source section](x-int-max-str-digits.md)
