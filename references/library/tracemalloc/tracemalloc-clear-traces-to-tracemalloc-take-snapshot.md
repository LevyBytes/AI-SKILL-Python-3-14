# tracemalloc — Functions

### API

### Functions

 tracemalloc.clear_traces()

Discard the traces of memory blocks that Python has allocated.

Refer also to `stop()`.

 tracemalloc.get_object_traceback(*obj*)

Fetch the traceback recording where the Python object *obj* came from. Returns a `Traceback` instance, or `None` when the `tracemalloc` module is not currently tracing memory allocations or never traced that object's allocation.

Refer also to the [`gc.get_referrers()`](https://docs.python.org/3.14/library/gc.html#gc.get_referrers) and [`sys.getsizeof()`](https://docs.python.org/3.14/library/sys.html#sys.getsizeof) functions.

 tracemalloc.get_traceback_limit()

Return the largest number of frames a trace's traceback can hold.

To query the limit, the `tracemalloc` module has to be tracing memory allocations; otherwise an exception is raised.

The `start()` function determines this limit.

 tracemalloc.get_traced_memory()

Return the present size and the peak size of the memory blocks the `tracemalloc` module is tracing, packaged as a tuple: `(current: int, peak: int)`.

 tracemalloc.reset_peak()

Reset the peak size of memory blocks tracked by the `tracemalloc` module down to whatever the current size is.

Has no effect when the `tracemalloc` module is not tracing memory allocations.

The call adjusts only the stored peak value; it leaves every trace untouched, in contrast to `clear_traces()`. A snapshot captured with `take_snapshot()` before `reset_peak()` runs remains meaningfully comparable to one captured afterward.

Refer also to `get_traced_memory()`.

Added in version 3.9.

 tracemalloc.get_tracemalloc_memory()

Return, in bytes, how much memory the `tracemalloc` module itself consumes to hold its traces of memory blocks. The value is an [`int`](https://docs.python.org/3.14/library/functions.html#int).

 tracemalloc.is_tracing()

Evaluates to `True` while the `tracemalloc` module is tracing Python memory allocations, and `False` otherwise.

Refer also to the `start()` and `stop()` functions.

 tracemalloc.start(*nframe: [int](https://docs.python.org/3.14/library/functions.html#int) = 1*)

Begin tracing Python memory allocations: place hooks on Python's memory allocators. Tracebacks gathered for traces are capped at *nframe* frames. By default a block's trace retains only the single most recent frame, so the limit is `1`. *nframe* must be at least `1`.

Even so, the full original count of frames making up the traceback stays available through the `Traceback.total_nframe` attribute.

Keeping more than `1` frame pays off only when you want statistics grouped by `'traceback'` or cumulative statistics: refer to the `Snapshot.compare_to()` and `Snapshot.statistics()` methods.

Each extra frame raises the memory and CPU cost of the `tracemalloc` module. Call the `get_tracemalloc_memory()` function to gauge how much memory the `tracemalloc` module is consuming.

To switch tracing on at startup, use either the [`PYTHONTRACEMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable (`PYTHONTRACEMALLOC=NFRAME`) or the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `tracemalloc=NFRAME` command line option.

Refer also to the `stop()`, `is_tracing()` and `get_traceback_limit()` functions.

 tracemalloc.stop()

Halt tracing of Python memory allocations: remove the hooks from Python's memory allocators. This also wipes out every trace of Python-allocated memory blocks gathered up to that point.

Invoke the `take_snapshot()` function to capture a snapshot of the traces before they are wiped.

Refer also to the `start()`, `is_tracing()` and `clear_traces()` functions.

 tracemalloc.take_snapshot()

Capture a snapshot of the traces for memory blocks Python has allocated. Returns a fresh `Snapshot` instance.

Any memory blocks allocated before the `tracemalloc` module began tracing are absent from the snapshot.

The tracebacks of traces are capped at `get_traceback_limit()` frames. Pass the *nframe* parameter to the `start()` function to keep more frames.

The `tracemalloc` module has to be tracing memory allocations for a snapshot to be taken; see the `start()` function.

Refer also to the `get_object_traceback()` function.

[Subject index](INDEX.md) · [Continue](tracemalloc-domainfilter-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
