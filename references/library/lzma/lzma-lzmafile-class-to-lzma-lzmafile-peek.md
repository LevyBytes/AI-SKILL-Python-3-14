# lzma / Reading and writing compressed files: `lzma.LZMAFile`, `peek()`

*class *lzma.LZMAFile(*filename=None*, *mode='r'*, ***, *format=None*, *check=-1*, *preset=None*, *filters=None*)

Open up an LZMA-compressed file in binary mode.

An `LZMAFile` may either wrap a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) that is already open or work straight on a named file. The *filename* argument names either that file object to wrap or the file to open by name (as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object). Where you wrap a pre-existing file object, that wrapped file stays open after the `LZMAFile` itself is closed.

The *mode* argument accepts `"r"` for reading (the default), `"w"` to overwrite, `"x"` for exclusive creation, or `"a"` to append. Equivalent forms are `"rb"`, `"wb"`, `"xb"` and `"ab"` in that order.

Where *filename* names a file object instead of a true file name, a `"w"` mode leaves the file untruncated and acts like `"a"`.

While opening a file to read, the supplied input may be several distinct compressed streams joined together. Such streams get decoded transparently as one logical stream.

While opening a file to read, the *format* and *filters* arguments carry the same significance they do for `LZMADecompressor`. Under those circumstances, leave the *check* and *preset* arguments unused.

While opening a file to write, the *format*, *check*, *preset* and *filters* arguments take on the same significance they hold for `LZMACompressor`.

`LZMAFile` honors every member listed by [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase), apart from [`detach()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.detach) and [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate). Both iteration and the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement work.

These additional method and attributes round out the interface:

 peek(*size=-1*)

Hand back buffered data while leaving the file position where it is. You'll get back at least one byte, except once EOF has been hit. Exactly how many bytes come back is undefined (and the *size* argument plays no role).

Note

Even though `peek()` leaves the `LZMAFile`'s own file position untouched, it can shift the position of the underlying file object (for instance, when the `LZMAFile` was built by handing a file object in via *filename*).

 mode

`'rb'` for reading and `'wb'` for writing.

Added in version 3.13.

 name

The name of the lzma file. This matches the [`name`](https://docs.python.org/3.14/library/io.html#io.FileIO.name) attribute belonging to the underlying [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

Added in version 3.13.

Changed in version 3.4: Added support for the `"x"` and `"xb"` modes.

Changed in version 3.5: The [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) method now accepts an argument of `None`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](lzma-open.md) · [Continue](lzma-lzmacompressor-class.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md) · [Owning module, declaration or section: Reading and writing compressed files](lzma-open.md)
