# bz2: BZ2File filename attribute

name

The bzip2 file name. Equivalent to the [`name`](https://docs.python.org/3.14/library/io.html#io.FileIO.name) attribute of the underlying [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

Added in version 3.13.

Changed in version 3.1: Support for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement was added.

Changed in version 3.3: Allowing *filename* to be a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) rather than a real filename became supported.

The `'a'` (append) mode arrived, together with the ability to read multi-stream files.

Changed in version 3.4: The `'x'` (exclusive creation) mode was added.

Changed in version 3.5: The [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) method now accepts an argument of `None`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.9: The *buffering* parameter has been removed. Ignored and deprecated ever since Python 3.0, it is now gone. To govern how the file is opened, pass in an already-open file object.

The *compresslevel* parameter became keyword-only.

Changed in version 3.10: This class is thread unsafe when faced with several concurrent readers or writers, exactly like its counterpart classes in [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) and [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) have always been.

[Subject index](INDEX.md) · [Previous](bz2-bz2file-class-to-bz2-bz2file-readinto.md) · [Continue](bz2-bz2compressor-class.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md) · [Owning module, declaration or section: bz2.BZ2File](bz2-bz2file-class-to-bz2-bz2file-readinto.md) · [Owning module, declaration or section: (De)compression of files](bz2-open.md)
