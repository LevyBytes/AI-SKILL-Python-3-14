# `compression.zstd` ? Compression compatible with the Zstandard format

### `compression.zstd` — Compression compatible with the Zstandard format

Added in version 3.14.

**Source code:** [Lib/compression/zstd/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/compression/zstd/__init__.py)

---

Use this module to compress and decompress data with the Zstandard (or *zstd*) compression algorithm; it ships both classes and functions for the job. The [zstd manual](https://facebook.github.io/zstd/doc/api_manual_latest.html) characterizes Zstandard as ?a fast lossless compression algorithm,? one ?targeting real-time compression scenarios,? delivering throughput ?at zlib-level and better compression ratios.? The module further offers a file interface for reading and writing the contents of `.zst` files produced by the **zstd** utility, plus raw zstd compressed streams.

What the `compression.zstd` module provides:

- The `open()` function and `ZstdFile` class for reading and writing compressed files.

- The `ZstdCompressor` and `ZstdDecompressor` classes for incremental (de)compression.

- The `compress()` and `decompress()` functions for one-shot (de)compression.

- The `train_dict()` and `finalize_dict()` functions and the `ZstdDict` class to train and manage Zstandard dictionaries.

- The `CompressionParameter`, `DecompressionParameter`, and `Strategy` classes for setting advanced (de)compression parameters.

This is an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your CPython build lack it, consult whatever documentation came from your distributor (meaning whoever handed Python to you). Distributors themselves should refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

[Subject index](INDEX.md) · [Continue](compression-zstd-zstderror.md)
