# bz2`bz2` - Support for **bzip2** compression

# Bz2

### `bz2` - Support for **bzip2** compression

**Source code:** [Lib/bz2.py](https://github.com/python/cpython/tree/3.14/Lib/bz2.py)

---

This module delivers a thorough interface for both compressing and decompressing data by way of the bzip2 compression algorithm.

The `bz2` module contains:

- The `open()` function and `BZ2File` class for reading and writing compressed files.

- The `BZ2Compressor` and `BZ2Decompressor` classes for incremental (de)compression.

- The `compress()` and `decompress()` functions for one-shot (de)compression.

This counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Where your build of CPython lacks it, seek out documentation from your distributor (meaning whoever supplied Python to you). Should you be the distributor yourself, refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

[Subject index](INDEX.md) · [Continue](bz2-open.md)
