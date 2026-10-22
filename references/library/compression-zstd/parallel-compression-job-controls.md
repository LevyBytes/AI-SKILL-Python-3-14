# compression.zstd: Parallel compression job size and overlap controls

job_size

A compression job’s size, given in bytes. It only matters once `nb_workers` >= 1. Because jobs run in parallel, this figure can have a knock-on effect on how many threads stay active.

A zero leaves the value to be determined for you automatically.

 overlap_log

Determines the amount of data carried over from earlier jobs (threads) into new ones, feeding the look behind window as compression proceeds. It comes into play solely when `nb_workers` >= 1. Permitted values run from 0 to 9.

>
- 0 lets the overlap amount be set dynamically

- 1 yields zero overlap

- 9 applies a full window size carried from the previous job

Stepping the value by one halves or doubles the overlap size. So “8” gives an overlap of `window_size/2`, “7” gives `window_size/4`, and so on.

[Subject index](INDEX.md) · [Previous](compression-strategy-and-long-distance-matching.md) · [Continue](decompression-parameter-bounds.md) · [Owning module, declaration or section: compression.zstd.CompressionParameter](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: Advanced parameter control](compression-zstd-compressionparameter-class.md)
