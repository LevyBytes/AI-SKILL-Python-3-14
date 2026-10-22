# gc: `gc.enable()`, `gc.disable()`, `gc.isenabled()`, `gc.collect()`, `gc.set_debug()`, `gc.get_debug()`, `gc.get_objects()`, `gc.get_stats()`, `gc.set_threshold()`

### `gc` — Garbage Collector interface

---

An interface to Python's optional garbage collector is exposed through this module. With it you can switch the collector off, adjust how frequently collection runs, and turn on debugging options. The module also exposes unreachable objects that the collector located yet was unable to release. Because the collector works alongside the reference counting that Python already performs, turning the collector off is safe whenever you know for certain that your program never builds reference cycles. Calling `gc.disable()` shuts off automatic collection. When chasing a leak, invoke `gc.set_debug(gc.DEBUG_LEAK)`. Be aware that this flag implies `gc.DEBUG_SAVEALL`, so collected garbage is preserved in gc.garbage where you can examine it.

The `gc` module provides the following functions:

 gc.enable()

Enable automatic garbage collection.

 gc.disable()

Disable automatic garbage collection.

 gc.isenabled()

Return `True` if automatic collection is enabled.

 gc.collect(*generation=2*)

If you supply no arguments, a complete collection runs. The optional *generation* argument accepts an integer that selects which generation to collect (ranging from 0 through 2). When the generation number is not valid, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results. What gets returned is the combined total of collected objects plus uncollectable ones.

Each full collection — or a collection of the topmost generation (2) — clears the free lists kept for several built-in types. Depending on the specific implementation, certain entries in some free lists might not be released, [`float`](https://docs.python.org/3.14/library/functions.html#float) being one such case.

What happens if you call `gc.collect()` when the interpreter is in the middle of a collection is undefined.

Changed in version 3.14: `generation=1` performs an increment of collection.

Changed in version 3.14.5: `generation=1` performs collection of the middle generation.

 gc.set_debug(*flags*)

Establish the debugging flags for garbage collection. Diagnostic output goes to `sys.stderr`. A roster of debugging flags appears further down; you can combine them with bit operations to govern what gets debugged.

 gc.get_debug()

Return the debugging flags currently set.

 gc.get_objects(*generation=None*)

Hands back a list of every object the collector is tracking, with the returned list itself left out. When *generation* is something other than `None`, only the tracked objects belonging to that generation are returned.

Changed in version 3.8: New *generation* parameter.

Changed in version 3.14: Generation 1 is removed

Changed in version 3.14.5: Generation 1 is reintroduced to maintain GC behavior from 3.13.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `gc.get_objects` with argument `generation`.

 gc.get_stats()

Hands back a list of three per-generation dictionaries holding collection statistics accumulated since the interpreter began running. How many keys exist could grow later on, but for now each dictionary holds these items:

- `collections` is the number of times this generation was collected;

- `collected` is the total number of objects collected inside this generation;

- `uncollectable` counts, within this generation, all objects deemed uncollectable (and consequently relocated into the `garbage` list).

Added in version 3.4.

 gc.set_threshold(*threshold0*[, *threshold1*[, *threshold2*]])

Establish the garbage collection thresholds, which govern collection frequency. Assigning *threshold0* a value of zero turns collection off.

The GC sorts objects into three generations according to the count of collection sweeps each has lived through. A freshly created object enters the youngest generation (generation `0`). Surviving a collection promotes an object into the next older generation. Generation `2` being the oldest, its objects stay put once collected. To work out when collection should fire, the collector tracks the count of object allocations and deallocations that have occurred since collection last ran. Collection kicks off once the allocation count minus the deallocation count climbs above *threshold0*. At first only generation `0` is inspected. Should generation `0` have been inspected more than *threshold1* times since the last time generation `1` was inspected, then generation `1` gets inspected too. The third generation behaves in a somewhat more involved fashion; consult [Collecting the oldest generation](https://github.com/python/cpython/blob/ff0ef0a54bef26fc507fbf9b7a6009eb7d3f17f5/InternalDocs/garbage_collector.md#collecting-the-oldest-generation) for further detail.

On the free-threaded build, the growth in process memory consumption is examined too before the collector fires. The collection is skipped if memory usage hasn't grown by 10% since the previous collection and the net count of object allocations hasn't gone past 40 times *threshold0*.

See [Garbage collector design](https://github.com/python/cpython/blob/3.14/InternalDocs/garbage_collector.md) for more information.

Changed in version 3.14: *threshold2* is ignored

Changed in version 3.14.5: *threshold2* is restored to match Python 3.13 behavior.

[Subject index](INDEX.md) · [Previous](garbage-collector-interface.md) · [Continue](gc-get-count-to-gc-unfreeze.md)
