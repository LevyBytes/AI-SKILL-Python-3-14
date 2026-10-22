# tracemalloc: StatisticDiff allocation changes and traceback properties

count

Number of memory blocks in the new snapshot (`int`): `0` when the memory blocks have been freed in the new snapshot.

 count_diff

Change in the number of memory blocks between the old and new snapshots (`int`): `0` when the memory blocks were allocated in the new snapshot.

 size

Total size of memory blocks in bytes in the new snapshot (`int`): `0` when the memory blocks have been freed in the new snapshot.

 size_diff

Change in the total size of memory blocks in bytes between the old and new snapshots (`int`): `0` when the memory blocks were allocated in the new snapshot.

 traceback

The traceback for where the memory blocks were allocated, a `Traceback` instance.

[Subject index](INDEX.md) · [Previous](tracemalloc-statisticdiff-class.md) · [Continue](tracemalloc-trace-class.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md) · [Owning module, declaration or section: tracemalloc.StatisticDiff](tracemalloc-statisticdiff-class.md) · [Owning module, declaration or section: StatisticDiff](tracemalloc-statisticdiff-class.md)
