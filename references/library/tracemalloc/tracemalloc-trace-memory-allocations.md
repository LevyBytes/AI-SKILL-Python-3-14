# tracemalloc`tracemalloc` - Trace memory allocations

# Tracemalloc

### `tracemalloc` - Trace memory allocations

Added in version 3.4.

**Source code:** [Lib/tracemalloc.py](https://github.com/python/cpython/tree/3.14/Lib/tracemalloc.py)

---

For debugging memory usage, the tracemalloc module records the memory blocks that Python allocates. The data it surfaces covers:

- The traceback identifying where any object was allocated

- Per-filename and per-line-number statistics for allocated blocks: total size, the count of blocks, and their average size

- Differencing of two snapshots, which exposes memory leaks

So that the module captures as many allocations as possible, launch it at the earliest point you can: either set the [`PYTHONTRACEMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable to `1`, or pass the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `tracemalloc` command line option. Alternatively, invoke `tracemalloc.start()` while the program runs to begin tracing Python memory allocations.

Out of the box, each allocated block's trace keeps only its single most recent frame (1 frame). If you instead want 25 frames captured from startup, give the [`PYTHONTRACEMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable the value `25`, or supply the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `tracemalloc=25` command line option.

[Subject index](INDEX.md) · [Continue](display-the-top-10.md)
