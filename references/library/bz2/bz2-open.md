# bz2: `bz2.open()`

### (De)compression of files

 bz2.open(*filename*, *mode='rb'*, *compresslevel=9*, *encoding=None*, *errors=None*, *newline=None*)

Open a bzip2-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

Just as with the `BZ2File` constructor, the *filename* argument may be a genuine filename (a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object), or else an existing file object to read from or write to.

The *mode* argument accepts any of `'r'`, `'rb'`, `'w'`, `'wb'`, `'x'`, `'xb'`, `'a'` or `'ab'` for binary mode, or else `'rt'`, `'wt'`, `'xt'`, or `'at'` for text mode. The default is `'rb'`.

The *compresslevel* argument is an integer running from 1 to 9, the same as for the `BZ2File` constructor.

In binary mode, this function amounts to the `BZ2File` constructor: `BZ2File(filename, mode, compresslevel=compresslevel)`. Under those circumstances, the *encoding*, *errors* and *newline* arguments must be left out.

In text mode, a `BZ2File` object gets built and then wrapped inside an [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) instance carrying the given encoding, error-handling behavior, and line ending(s).

Added in version 3.3.

Changed in version 3.4: The `'x'` (exclusive creation) mode was added.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](bz2-support-for-bzip2-compression.md) · [Continue](bz2-bz2file-class-to-bz2-bz2file-readinto.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md)
