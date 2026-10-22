# What's New In Python 3.4 / tracemalloc — tracemalloc

### tracemalloc

The fresh [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module (specified in [**PEP 454**](https://peps.python.org/pep-0454/)) is a debugging aid that follows memory blocks allocated by Python. The data it surfaces covers:

- Trace where an object was allocated

- Per-filename and per-line-number statistics across the allocated memory blocks: their total size, plus the count and mean size of those blocks

- Compute the differences between two snapshots to detect memory leaks

See also

[**PEP 454**](https://peps.python.org/pep-0454/) ? Add a new tracemalloc module to trace Python memory allocations

PEP written and implemented by Victor Stinner

[Subject index](INDEX.md) · [Previous source section](statistics.md) · [Next source section](abc.md) · [Release/subject declaration](release-highlights.md)
