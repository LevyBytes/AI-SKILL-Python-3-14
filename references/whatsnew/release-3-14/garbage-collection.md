# What's new in Python 3.14 / Garbage collection - gc

### Garbage collection

**From Python 3.14.5 onwards:**

A change to the garbage collector (GC) landed in Python 3.14.5.

Python 3.14.0-3.14.4 came with a new incremental GC. Yet, following several [reports](https://github.com/python/cpython/issues/142516) of considerable memory pressure within production environments, it has been rolled back to the generational GC from 3.13. That is the GC in use by Python 3.14.5 and beyond.

**Previously in Python 3.14.0-3.14.4:**

The cycle garbage collector is now incremental. What this means is that, for larger heaps, peak pause times drop by an order of magnitude or more.

Only two generations exist now: young and old. Whenever [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) is left uncalled directly, the GC runs somewhat less often. Each run collects the young generation plus an increment of the old generation, rather than gathering one or more generations.

A slight shift applies to how `gc.collect()` behaves:

- `gc.collect(1)`: Carries out an increment of garbage collection instead of gathering generation 1.

- Every other call to `gc.collect()` stays the same.

(Contributed by Mark Shannon in [gh-108362](https://github.com/python/cpython/issues/108362).)

[Subject index](INDEX.md) · [Previous source section](pep-765-control-flow-in-finally-blocks.md) · [Next source section](default-interactive-shell.md) · [Release/subject declaration](summary-release-highlights.md)
