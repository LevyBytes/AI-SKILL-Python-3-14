# compression.zstd: `compression.zstd.compress()`, `compression.zstd.decompress()`

### Compressing and decompressing data in memory

 compression.zstd.compress(*data*, *level=None*, *options=None*, *zstd_dict=None*)

Compress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), handing back the compressed data as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

The *level* argument is an integer that governs how aggressively data is compressed. *level* serves as a shortcut for assigning `CompressionParameter.compression_level` inside *options*. Call `bounds()` on `compression_level` to learn which values *level* accepts. When you need advanced compression options, drop the *level* argument and instead assign the `CompressionParameter.compression_level` parameter within the *options* dictionary.

The *options* argument is a Python dictionary holding advanced compression parameters. Which keys and values are valid for compression parameters appears in the `CompressionParameter` documentation.

The *zstd_dict* argument is a `ZstdDict` instance holding trained data that boosts compression efficiency. You can build a Zstandard dictionary with the `train_dict()` function.

 compression.zstd.decompress(*data*, *zstd_dict=None*, *options=None*)

Decompress *data* (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), handing back the uncompressed data as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

The *options* argument is a Python dictionary holding advanced decompression parameters. Which keys and values are valid for compression parameters appears in the `DecompressionParameter` documentation.

The *zstd_dict* argument is a `ZstdDict` instance holding trained data applied during compression. It has to be the very same Zstandard dictionary that was used when compressing.

Where *data* joins several separate compressed frames together, every one of those frames is decompressed and the joined results are returned.

[Subject index](INDEX.md) · [Previous](zstd-file-class-and-peek.md) · [Continue](zstd-compressor-and-pledged-input-size.md)
