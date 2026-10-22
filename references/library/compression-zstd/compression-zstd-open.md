# compression.zstd: `compression.zstd.open()`

### Reading and writing compressed files

 compression.zstd.open(*file*, */*, *mode='rb'*, ***, *level=None*, *options=None*, *zstd_dict=None*, *encoding=None*, *errors=None*, *newline=None*)

Open a Zstandard-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

You may pass the *file* argument as a file name ? supplied as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object, which then opens the named file ? or as an already-open file object to read from or write to.

For the mode argument, choose `'rb'` for reading (default), `'wb'` for overwriting, `'ab'` for appending, or `'xb'` for exclusive creation. The shorter equivalents are `'r'`, `'w'`, `'a'`, and `'x'` respectively. Text mode is likewise available through `'rt'`, `'wt'`, `'at'`, and `'xt'` respectively.

For reads, the *options* argument may be a dictionary of advanced decompression parameters; consult `DecompressionParameter` for full details about which parameters are supported. The *zstd_dict* argument supplies a `ZstdDict` instance to apply during decompression. For reads, passing a *level* argument that is not None raises a `TypeError`.

For writes, the *options* argument may be a dictionary of advanced compression parameters; consult `CompressionParameter` for full details about which parameters are supported. The *level* argument selects the compression level applied as compressed data is written. At most one of *level* or *options* may be non-None. The *zstd_dict* argument supplies a `ZstdDict` instance to apply during compression.

When using binary mode, calling this function matches invoking the `ZstdFile` constructor: `ZstdFile(file, mode, ...)`. Here the *encoding*, *errors*, and *newline* parameters must not be provided.

For text mode, a `ZstdFile` object is built and then wrapped inside an [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) instance carrying the chosen encoding, error handling behavior, and line endings.

[Subject index](INDEX.md) · [Previous](compression-zstd-zstderror.md) · [Continue](zstd-file-class-and-peek.md)
