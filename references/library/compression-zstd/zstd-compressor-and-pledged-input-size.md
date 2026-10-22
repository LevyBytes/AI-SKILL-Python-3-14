# compression.zstd: `compression.zstd.ZstdCompressor`, `compress()`, `flush()`, `set_pledged_input_size()`

*class *compression.zstd.ZstdCompressor(*level=None*, *options=None*, *zstd_dict=None*)

Create a compressor object, which can be used to compress data incrementally.

If you would rather compress one chunk of data in a single call, turn to the module-level function `compress()`.

The *level* argument is an integer that governs how aggressively data is compressed. *level* serves as a shortcut for assigning `CompressionParameter.compression_level` inside *options*. Call `bounds()` on `compression_level` to learn which values *level* accepts. When you need advanced compression options, drop the *level* argument and instead assign the `CompressionParameter.compression_level` parameter within the *options* dictionary.

The *options* argument is a Python dictionary holding advanced compression parameters. Which keys and values are valid for compression parameters appears in the `CompressionParameter` documentation.

The *zstd_dict* argument is an optional `ZstdDict` instance holding trained data that boosts compression efficiency. You can build a Zstandard dictionary with the `train_dict()` function.

 compress(*data*, *mode=ZstdCompressor.CONTINUE*)

Compress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), giving back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object holding compressed data when possible, and otherwise an empty `bytes` object. Part of *data* may stay buffered inside, ready for later calls to `compress()` and `flush()`. Join the returned data with whatever earlier calls to `compress()` produced.

The *mode* argument is a `ZstdCompressor` attribute, either `CONTINUE`, `FLUSH_BLOCK`, or `FLUSH_FRAME`.

Once every piece of data has reached the compressor, invoke the `flush()` method to wrap up compression. Where `compress()` runs with *mode* set to `FLUSH_FRAME`, skip `flush()`, since calling it would emit a fresh empty frame.

 flush(*mode=ZstdCompressor.FLUSH_FRAME*)

Wrap up compression, giving back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object that holds whatever data sat in the compressor's internal buffers.

The *mode* argument is a `ZstdCompressor` attribute, either `FLUSH_BLOCK`, or `FLUSH_FRAME`.

 set_pledged_input_size(*size*)

State the quantity of uncompressed data *size* that the next frame will receive. *size* gets recorded in the frame header of the next frame, unless `CompressionParameter.content_size_flag` equals `False` or `0`. When *size* is `0`, the frame holds nothing. Where *size* is `None`, the frame header leaves out the frame size. Frames carrying the uncompressed data size need less memory at decompression time, and this matters more at higher compression levels.

Where `last_mode` differs from `FLUSH_FRAME`, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised because the compressor sits somewhere other than the start of a frame. Should the pledged size differ from the real size of the data fed to `compress()`, later calls to `compress()` or `flush()` might raise `ZstdError` and the final chunk of data could be lost.

Once `flush()` or `compress()` run with mode `FLUSH_FRAME`, the next frame keeps the frame size out of its header until `set_pledged_input_size()` runs once more.

 CONTINUE

Gather additional data for compression, possibly emitting output right away or possibly not. This mode pushes the compression ratio higher by packing as much data as it can into each block and frame.

 FLUSH_BLOCK

Finish and emit a block onto the data stream. Whatever data has come back up to now can be decompressed straight away. Later blocks emitted by `compress()` calls can still point back at earlier data, which helps compression.

 FLUSH_FRAME

Finish and emit a frame. Any data fed to `compress()` afterward lands in a new frame and *cannot* reference earlier data.

 last_mode

The most recent mode handed to either `compress()` or `flush()`. That value is one of `CONTINUE`, `FLUSH_BLOCK`, or `FLUSH_FRAME`. It starts out as `FLUSH_FRAME`, marking the compressor as positioned at the start of a new frame.

[Subject index](INDEX.md) · [Previous](compression-zstd-compress-to-compression-zstd-decompress.md) · [Continue](zstd-decompressor-and-decompression.md) · [Owning module, declaration or section: Compressing and decompressing data in memory](compression-zstd-compress-to-compression-zstd-decompress.md)
