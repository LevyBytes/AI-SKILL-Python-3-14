# compileall - The `compression` package

## The compression package

### The `compression` package

Added in version 3.14.

Bundled inside the `compression` package are the canonical compression modules, each exposing an interface to one of several distinct compression algorithms. A number of these have long existed as standalone modules; for the sake of compatibility they stay reachable under their old names and won't disappear without first going through a deprecation cycle. Wherever it's reasonable, reaching for the modules in `compression` is the recommended path.

- `compression.bz2` – Re-exports [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2)

- `compression.gzip` – Re-exports [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip)

- `compression.lzma` – Re-exports [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma)

- `compression.zlib` – Re-exports [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib)

- [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) – Wrapper for the Zstandard compression library

[Subject index](INDEX.md)
