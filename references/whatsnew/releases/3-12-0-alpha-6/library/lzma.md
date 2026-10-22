# Python 3.12.0 alpha 6 / library / lzma

[bpo-23224](https://bugs.python.org/issue?@action=redirect&bpo=23224): Repair segfaults that occurred when [`lzma.LZMADecompressor`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMADecompressor) and [`bz2.BZ2Decompressor`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2Decompressor) objects were created without `__init__()` being called, and repair the leaking of locks and internal buffers when the `__init__()` methods of `lzma.LZMADecompressor`, [`lzma.LZMACompressor`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMACompressor), [`bz2.BZ2Compressor`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2Compressor), and `bz2.BZ2Decompressor` objects get invoked more than once.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
