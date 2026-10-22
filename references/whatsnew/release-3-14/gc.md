# What's new in Python 3.14 / gc — gc

### gc

- **From Python 3.14.5 onwards:**

The releases Python 3.14.0-3.14.4 came with a new incremental garbage collector. Yet, owing to numerous [reports](https://github.com/python/cpython/issues/142516) about serious memory pressure in production deployments, it was rolled back to the generational GC carried over from 3.13. That collector is the GC employed in Python 3.14.5 and afterward.

- **Previously in Python 3.14.0-3.14.4:**

With the new incremental garbage collector, peak pause durations shrink by an order of magnitude or beyond for sizable heaps.

Owing to this optimization, the interpretation of the values returned by [`get_threshold()`](https://docs.python.org/3.14/library/gc.html#gc.get_threshold) and [`set_threshold()`](https://docs.python.org/3.14/library/gc.html#gc.set_threshold) shifted, as did those of [`get_count()`](https://docs.python.org/3.14/library/gc.html#gc.get_count) and [`get_stats()`](https://docs.python.org/3.14/library/gc.html#gc.get_stats).

  - To preserve backwards compatibility, [`get_threshold()`](https://docs.python.org/3.14/library/gc.html#gc.get_threshold) still hands back a three-item tuple. Its first entry is the threshold governing young collections, just as earlier; its second entry controls how fast the old collection gets scanned (10 by default, with larger numbers meaning the old collection gets scanned more slowly). Its third entry is now without meaning and stays at zero throughout.

  - [`set_threshold()`](https://docs.python.org/3.14/library/gc.html#gc.set_threshold) now disregards whatever items follow the second.

  - [`get_count()`](https://docs.python.org/3.14/library/gc.html#gc.get_count) and [`get_stats()`](https://docs.python.org/3.14/library/gc.html#gc.get_stats) still hand back results in the same shape. The sole change is that, rather than the results pointing to the young, aging and old generations, they instead point to the young generation together with the aging and collecting spaces of the old generation.

To sum up, code that tried to tune how the cycle GC behaves might not act precisely as planned, although it is highly improbable to do harm. Every other piece of code will operate perfectly well.

(Contributed by Mark Shannon in [gh-108362](https://github.com/python/cpython/issues/108362).)

### Notable changes in 3.14.5

### gc

- The incremental collector that came with Python 3.14.0-3.14.4 has been rolled back to 3.13's generational collector, prompted by several [reports](https://github.com/python/cpython/issues/142516) describing heavy memory pressure in live production settings. Consult Garbage collection for the full account.

[Subject index](INDEX.md) · [Previous source section](difflib.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](notable-changes-in-3-14-1.md)
