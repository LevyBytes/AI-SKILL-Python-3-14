# tracemalloc.Snapshot: `compare_to()`, `dump()`, `filter_traces()`, `load()`, `statistics()`

compare_to(*old_snapshot: Snapshot*, *key_type: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*, *cumulative: [bool](https://docs.python.org/3.14/library/functions.html#bool) = False*)

Work out the differences against an earlier snapshot. Returns statistics as a sorted list of `StatisticDiff` instances grouped by *key_type*.

For the *key_type* and *cumulative* parameters, consult the `Snapshot.statistics()` method.

Results run from largest to smallest, keyed on: the absolute value of `StatisticDiff.size_diff`, then `StatisticDiff.size`, then the absolute value of `StatisticDiff.count_diff`, then `Statistic.count`, and finally `StatisticDiff.traceback`.

 dump(*filename*)

Persist the snapshot to a file.

Use `load()` to bring the snapshot back.

 filter_traces(*filters*)

Produce a new `Snapshot` instance whose `traces` sequence has been filtered, where *filters* is a list of `DomainFilter` and `Filter` instances. When *filters* is empty, return a new `Snapshot` instance carrying a copy of the traces.

Every inclusive filter is applied together; a trace is dropped unless at least one inclusive filter matches it. A trace is also dropped when even one exclusive filter matches it.

Changed in version 3.6: `DomainFilter` instances are now also accepted in *filters*.

 *classmethod *load(*filename*)

Read a snapshot back from a file.

Refer also to `dump()`.

 statistics(*key_type: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*, *cumulative: [bool](https://docs.python.org/3.14/library/functions.html#bool) = False*)

Return statistics as a sorted list of `Statistic` instances grouped by *key_type*:

| key_type | description |
| --- | --- |
| `'filename'` | filename |
| `'lineno'` | filename and line number |
| `'traceback'` | traceback |

When *cumulative* is `True`, accumulate the size and count of memory blocks over every frame in a trace's traceback rather than the most recent frame alone. Cumulative mode works only when *key_type* is `'filename'` or `'lineno'`.

Results run from largest to smallest, keyed on: `Statistic.size`, then `Statistic.count`, and finally `Statistic.traceback`.

 traceback_limit

The largest number of frames retained in the traceback of `traces`: the value `get_traceback_limit()` returned at the moment the snapshot was taken.

 traces

Traces for every memory block Python has allocated: a sequence of `Trace` instances.

The order of the sequence is unspecified. Apply the `Snapshot.statistics()` method to obtain a sorted statistics list.

[Subject index](INDEX.md) · [Previous](tracemalloc-snapshot-class.md) · [Continue](tracemalloc-statistic-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md) · [Owning module, declaration or section: tracemalloc.Snapshot](tracemalloc-snapshot-class.md) · [Owning module, declaration or section: Snapshot](tracemalloc-snapshot-class.md)
