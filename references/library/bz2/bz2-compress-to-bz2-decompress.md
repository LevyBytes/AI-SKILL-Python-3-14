# bz2 — One-shot (de)compression

### One-shot (de)compression

 bz2.compress(*data*, *compresslevel=9*)

Compress *data*, a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

*compresslevel*, where supplied, has to be an integer between `1` and `9`. The default is `9`.

For incremental compression, use a `BZ2Compressor` instead.

 bz2.decompress(*data*)

Decompress *data*, a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Where *data* is several compressed streams concatenated together, decompress every one of the streams.

For incremental decompression, use a `BZ2Decompressor` instead.

Changed in version 3.3: Support for multi-stream inputs was added.

[Subject index](INDEX.md) · [Previous](bz2-bz2decompressor-class-to-bz2-bz2decompressor-decompress.md) · [Continue](examples-of-usage.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md)
