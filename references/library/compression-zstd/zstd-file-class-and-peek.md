# compression.zstd: `compression.zstd.ZstdFile`, `peek()`

*class *compression.zstd.ZstdFile(*file*, */*, *mode='rb'*, ***, *level=None*, *options=None*, *zstd_dict=None*)

Open a Zstandard-compressed file in binary mode.

A `ZstdFile` may either wrap a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) that is already open or work straight on a named file. The *file* argument names either the file object to wrap or the file to open (as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object). When an existing file object is wrapped, closing the `ZstdFile` leaves that wrapped file open.

For the *mode* argument, pick `'rb'` for reading (default), `'wb'` for overwriting, `'xb'` for exclusive creation, or `'ab'` for appending. The shorter equivalents are `'r'`, `'w'`, `'x'` and `'a'` respectively.

Where *file* is a file object instead of a real file name, a `'w'` mode performs no truncation and behaves the same as `'a'`.

For reads, the *options* argument may be a dictionary of advanced decompression parameters; consult `DecompressionParameter` for full details about which parameters are supported. The *zstd_dict* argument supplies a `ZstdDict` instance to apply during decompression. For reads, passing a *level* argument that is not None raises a `TypeError`.

For writes, the *options* argument may be a dictionary of advanced compression parameters; consult `CompressionParameter` for full details about which parameters are supported. The *level* argument selects the compression level applied as compressed data is written. At most one of *level* or *options* may be passed. The *zstd_dict* argument supplies a `ZstdDict` instance to apply during compression.

`ZstdFile` provides every member listed by [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase), apart from [`detach()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.detach) and [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate). Both iteration and the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement work.

These additional method and attributes are supplied as well:

 peek(*size=-1*)

Return buffered data while leaving the file position where it is. You always get back at least one byte unless EOF has already been hit. How many bytes come back is not specified (and the *size* argument is disregarded).

Note

Although `peek()` leaves the `ZstdFile` position untouched, it can shift the position of the underlying file object (say, when a file object was handed to the `ZstdFile` constructor as *file*).

 mode

`'rb'` for reading and `'wb'` for writing.

 name

The Zstandard file's name. This mirrors the [`name`](https://docs.python.org/3.14/library/io.html#io.FileIO.name) attribute belonging to the underlying [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

[Subject index](INDEX.md) · [Previous](compression-zstd-open.md) · [Continue](compression-zstd-compress-to-compression-zstd-decompress.md) · [Owning module, declaration or section: Reading and writing compressed files](compression-zstd-open.md)
