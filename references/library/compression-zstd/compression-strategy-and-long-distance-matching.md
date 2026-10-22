# compression.zstd: Zstandard strategy choice and long-distance matching

Pick a strategy with a larger value and zstd reaches for a more elaborate compression technique, which buys you better compression ratios at the cost of slower compression.

See also

`Strategy`

 enable_long_distance_matching

For sizable inputs, long distance matching helps compression by turning up large matches that lie farther apart. The trade-off is more memory consumed and a bigger window size.

`True` or `1` enable long distance matching while `False` or `0` disable it.

Switching this parameter on bumps the default `window_log` up to 128 MiB, unless you have deliberately pinned it elsewhere. It is on out of the box whenever `window_log` >= 128 MiB and the compression strategy >= `btopt` (compression level 16+).

 ldm_hash_log

The long-distance-matching table’s size, expressed as a power of two. Raising it lifts both memory consumption and the compression ratio while dragging compression speed down.

Leave this at zero and the value is picked for you automatically.

 ldm_min_match

The smallest match size the long distance matcher will accept. Push it too high or too low and the compression ratio frequently suffers.

Set this to zero and the value gets chosen for you automatically.

 ldm_bucket_size_log

The log size of every bucket within the long distance matcher hash table, used for resolving collisions. Bigger values sharpen collision resolution yet slow compression down.

A zero here hands the choice of value over to automatic selection.

 ldm_hash_rate_log

How often entries are inserted into or looked up in the long distance matcher hash table. Bigger values quicken compression. Stray too far from the default, though, and you will probably see the compression ratio drop.

A zero value triggers automatic selection of the setting.

 content_size_flag

Record the size of the data destined for compression into the Zstandard frame header, provided that size is known ahead of compressing.

There are only a few situations in which this flag does anything:

- Invoking `compress()` to compress in a single shot

- Handing over every byte meant for the frame within one `ZstdCompressor.compress()` call, using the `ZstdCompressor.FLUSH_FRAME` mode.

- Invoking `ZstdCompressor.set_pledged_input_size()` with the precise quantity of data the compressor is about to receive, done before any `ZstdCompressor.compress()` calls for the present frame. Every fresh frame demands its own `ZstdCompressor.set_pledged_input_size()` call.

Outside of these, other compression calls might leave the size detail out of the frame header.

`True` or `1` enable the content size flag while `False` or `0` disable it.

 checksum_flag

At the close of every frame, a four-byte XXHash64 checksum of the uncompressed content gets written out. During decompression, Zstandard’s code checks that checksum, and a mismatch raises a `ZstdError` exception.

`True` or `1` enable checksum generation while `False` or `0` disable it.

 dict_id_flag

Compress using a `ZstdDict` and that dictionary’s ID is recorded in the frame header.

`True` or `1` enable storing the dictionary ID while `False` or `0` disable it.

 nb_workers

Choose the number of threads to spin up for compressing in parallel. Any `nb_workers` > 0 turns multi-threaded compression on, while `1` denotes “one-thread multi-threaded mode”. Adding workers gains you speed but also eats more memory and trims the compression ratio a little.

Leaving it at zero shuts multi-threading off entirely.

[Subject index](INDEX.md) · [Continue](parallel-compression-job-controls.md) · [Owning module, declaration or section: compression.zstd.CompressionParameter](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: Advanced parameter control](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: strategy](compression-zstd-compressionparameter-bounds.md) · [Preceding source contract and version conditions](compression-zstd-compressionparameter-bounds.md)
