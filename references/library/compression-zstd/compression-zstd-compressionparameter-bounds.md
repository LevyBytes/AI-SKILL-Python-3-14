# compression.zstd: `bounds()`

bounds()

Return the tuple of int bounds, `(lower, upper)`, of a compression parameter. Call this method on whichever attribute whose bounds you want to read. To learn the valid values for `compression_level`, for example, inspect the result of `CompressionParameter.compression_level.bounds()`.

Both the lower and upper bounds are inclusive.

 compression_level

A high-level lever for adjusting other compression parameters that shape the speed and ratio of compressing data.

Ordinary compression levels sit above `0`. Anything beyond `20` counts as ?ultra? compression and demands more memory than the other levels. You can pick negative values to swap a worse compression ratio for quicker compression.

Setting the level to zero uses `COMPRESSION_LEVEL_DEFAULT`.

 window_log

The greatest back-reference distance the compressor is allowed to reach while compressing data, given as a power of two, `1 << window_log` bytes. This parameter has a large effect on how much memory compression uses. Higher values cost more memory yet yield better compression values.

A value of zero causes the value to be selected automatically.

 hash_log

The size of the initial probe table, as a power of two. The memory it consumes works out to `1 << (hash_log+2)` bytes. Bigger tables raise the compression ratio of strategies <= `dfast`, and raise the compression speed of strategies > `dfast`.

A value of zero causes the value to be selected automatically.

 chain_log

How large the multi-probe search table is, given as a power of two. Its memory footprint comes out to `1 << (chain_log+2)` bytes. Bigger tables yield better but slower compression. The parameter does nothing for the `fast` strategy. It still helps with the `dfast` strategy, where it sets up a secondary probe table.

A value of zero causes the value to be selected automatically.

 search_log

The count of search attempts, as a power of two. More attempts yield better but slower compression. This parameter does nothing for the `fast` and `dfast` strategies.

A value of zero causes the value to be selected automatically.

 min_match

The smallest size of searched matches. Bigger values speed up compression and decompression while lowering the ratio. Keep in mind that Zstandard can still turn up matches below this size; it merely nudges its search algorithm toward this size and above. Across all strategies < `btopt`, the effective minimum is `4`; across all strategies > `fast`, the effective maximum is `6`.

A value of zero causes the value to be selected automatically.

 target_length

What this field does hinges on the chosen `Strategy`.

With strategies `btopt`, `btultra` and `btultra2`, the value sets the match length deemed ?good enough? to halt searching. Bigger values lift compression ratios but slow compression down.

With strategy `fast`, the value sets the spacing between match sampling. Bigger values quicken compression at the cost of a worse compression ratio.

A value of zero causes the value to be selected automatically.

 strategy

[Subject index](INDEX.md) · [Previous](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: compression.zstd.CompressionParameter](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: Advanced parameter control](compression-zstd-compressionparameter-class.md) · [Required continuation of the source contract](compression-strategy-and-long-distance-matching.md)
