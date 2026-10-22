# compression.zstd: `compression.zstd.ZstdDecompressor`, `decompress()`

*class *compression.zstd.ZstdDecompressor(*zstd_dict=None*, *options=None*)

Create a decompressor object, which can be used to decompress data incrementally.

If you would rather decompress a whole compressed stream in one go, turn to the module-level function `decompress()`.

The *options* argument is a Python dictionary holding advanced decompression parameters. Which keys and values are valid for compression parameters appears in the `DecompressionParameter` documentation.

The *zstd_dict* argument is a `ZstdDict` instance holding trained data applied during compression. It has to be the very same Zstandard dictionary that was used when compressing.

Note

Unlike the `decompress()` function and the `ZstdFile` class, this class will not silently cope with inputs holding several compressed frames. When you need to decompress a multi-frame input, reach for `decompress()`, for `ZstdFile` if a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) is involved, or for several `ZstdDecompressor` instances.

 decompress(*data*, *max_length=-1*)

Decompress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), giving back uncompressed data as bytes. Part of *data* may stay buffered inside, ready for later calls to `decompress()`. Join the returned data with whatever earlier calls to `decompress()` produced.

Where *max_length* is non-negative, the method gives back no more than *max_length* bytes of decompressed data. Once that ceiling is hit while more output remains available, the `needs_input` attribute is set to `False`. From there, the following call to `decompress()` can hand *data* as `b''` to pull out more of the output.

Where every byte of the input data got decompressed and returned (whether because it came to fewer than *max_length* bytes, or because *max_length* was negative), the `needs_input` attribute is set to `True`.

Trying to decompress data past the end of a frame raises a `ZstdError`. Whatever data sits beyond the end of the frame is disregarded and kept in the `unused_data` attribute.

 eof

`True` if the end-of-stream marker has been reached.

 unused_data

Data found after the end of the compressed stream.

Before the end of the stream is reached, this will be `b''`.

 needs_input

`False` whenever the `decompress()` method still has additional decompressed output to hand back before it needs fresh compressed input.

[Subject index](INDEX.md) · [Previous](zstd-compressor-and-pledged-input-size.md) · [Continue](compression-zstd-train-dict-to-compression-zstd-finalize-dict.md) · [Owning module, declaration or section: Compressing and decompressing data in memory](compression-zstd-compress-to-compression-zstd-decompress.md)
