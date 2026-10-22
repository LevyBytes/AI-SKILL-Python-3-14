# gzip: `gzip.GzipFile`, `peek()`

*class *gzip.GzipFile(*filename=None*, *mode=None*, *compresslevel=9*, *fileobj=None*, *mtime=None*)

The constructor for the `GzipFile` class, which mimics nearly every method of a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) save for the [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate) method. You have to supply a meaningful value for at least one of *fileobj* and *filename*.

The fresh class instance is built on *fileobj*, which can be a plain file, an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object, or any other object that imitates a file. Its default is `None`, and in that situation *filename* is opened to furnish a file object.

Whenever *fileobj* is not `None`, the *filename* argument serves solely to be embedded in the **gzip** file header, which can record the uncompressed file's original name. It defaults to the name of *fileobj* where that is recoverable; failing that, it defaults to the empty string, and then no original filename ends up in the header.

The *mode* argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`, `'w'`, `'wb'`, `'x'`, or `'xb'`, according to whether the file is to be read or written. The default mirrors the mode of *fileobj* where recoverable; otherwise the default is `'rb'`. Upcoming Python releases will stop relying on the mode of *fileobj*. You are better off always stating *mode* when writing.

Bear in mind that the file is invariably opened in binary mode. To work with a compressed file in text mode, turn to `open()` (or wrap your `GzipFile` inside an [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper)).

The *compresslevel* argument is an integer spanning `0` to `9` that governs the compression level; `1` is the quickest and gives the least compression, whereas `9` is the slowest and gives the most. `0` means no compression. The default is `9`.

The optional *mtime* argument is the timestamp that gzip asks for. The time follows Unix format, namely seconds elapsed since 00:00:00 UTC, January 1, 1970. With *mtime* left out or `None`, the present time is taken. Set *mtime* = 0 to produce a compressed stream that is independent of the creation time.

Refer below to the `mtime` attribute that gets populated during decompression.

Invoking a `GzipFile` object's `close()` method leaves *fileobj* open, on the chance that you want to append further content past the compressed data. This further lets you hand an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object opened for writing as *fileobj* and afterward pull back the resulting memory buffer through the `io.BytesIO` object's [`getvalue()`](https://docs.python.org/3.14/library/io.html#io.BytesIO.getvalue) method.

`GzipFile` honors the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) interface, iteration and the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement included. The lone unimplemented piece is the [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate) method.

`GzipFile` additionally exposes the following method and attribute:

 peek(*n*)

Read back *n* uncompressed bytes while leaving the file position where it was. The count of bytes handed back might exceed or fall short of what you asked for.

Note

Although a `peek()` call leaves the file position of the `GzipFile` untouched, it can shift the position of the underlying file object (for example, when the `GzipFile` was created via the *fileobj* parameter).

Added in version 3.2.

 mode

`'rb'` while reading and `'wb'` while writing.

Changed in version 3.13: Earlier on, this had been an integer of either `1` or `2`.

 mtime

During decompression, this attribute takes on the final timestamp from the header most recently read. It is an integer counting the seconds since the Unix epoch (00:00:00 UTC, January 1, 1970). Before any header has been read its starting value is `None`.

 name

The on-disk path to the gzip file, given as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). It equals what [`os.fspath()`](https://docs.python.org/3.14/library/os.html#os.fspath) yields for the original input path, with no further normalization, resolution, or expansion applied.

Changed in version 3.1: Gained support for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, together with the *mtime* constructor argument and the `mtime` attribute.

Changed in version 3.2: Gained support for zero-padded and unseekable files.

Changed in version 3.3: The [`io.BufferedIOBase.read1()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read1) method is now implemented.

Changed in version 3.4: Added support for the `'x'` and `'xb'` modes.

Changed in version 3.5: Gained support for writing arbitrary [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). The [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) method now takes an argument of `None`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Deprecated since version 3.9: Opening `GzipFile` for writing while leaving the *mode* argument unspecified is deprecated.

Changed in version 3.12: Remove the `filename` attribute, use the `name` attribute instead.

[Subject index](INDEX.md) · [Previous](gzip-open-to-gzip-badgzipfile.md) · [Continue](gzip-compress-to-gzip-decompress.md) · [Owning module, declaration or section: gzip](gzip-open-to-gzip-badgzipfile.md)
