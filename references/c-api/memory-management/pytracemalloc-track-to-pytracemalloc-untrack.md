# tracemalloc C API

### tracemalloc C API

Added in version 3.7.

 int PyTraceMalloc_Track(unsigned int domain, uintptr_t ptr, size_t size)

Register an allocated memory block with the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module.

Hand back `0` when it works, or `-1` on a failure (the trace storage could not be allocated). The result is `-2` should tracemalloc be turned off.

Where the block is already on record, its current trace gets refreshed.

 int PyTraceMalloc_Untrack(unsigned int domain, uintptr_t ptr)

Remove an allocated memory block from the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module's records. If the block was never being tracked, this has no effect.

When tracemalloc is turned off the result is `-2`; in every other case it is `0`.

[Subject index](INDEX.md) · [Previous source contract](the-mimalloc-allocator.md) · [Following source contract](examples.md)
