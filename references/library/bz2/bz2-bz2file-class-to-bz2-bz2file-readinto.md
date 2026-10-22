# bz2 / (De)compression of files: `bz2.BZ2File`, `peek()`, `fileno()`, `readable()`, `seekable()`, `writable()`, `read1()`, `readinto()`

*class *bz2.BZ2File(*filename*, *mode='r'*, ***, *compresslevel=9*)

Open a bzip2-compressed file in binary mode.

Where *filename* is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, the named file is opened directly. Failing that, *filename* ought to be a [file object](https://docs.python.org/3.14/glossary.html#term-file-object), which gets used to read or write the compressed data.

The *mode* argument may be `'r'` for reading (the default), `'w'` for overwriting, `'x'` for exclusive creation, or `'a'` for appending. Each of these can equally be expressed as `'rb'`, `'wb'`, `'xb'` and `'ab'` respectively.

Where *filename* is a file object (in place of a genuine file name), a mode of `'w'` does not truncate the file, behaving instead like `'a'`.

Where *mode* is `'w'` or `'a'`, *compresslevel* may be an integer between `1` and `9` that sets the level of compression: `1` yields the least compression, while `9` (the default) yields the most compression.

Where *mode* is `'r'`, the input file is permitted to be several compressed streams concatenated together.

`BZ2File` supplies every member laid out by [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase), apart from [`detach()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.detach) and [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate). Iteration along with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement are supported.

`BZ2File` further supplies these methods and attributes:

 peek([*n*])

Hand back buffered data without moving the file position forward. A minimum of one byte of data comes back (barring EOF). Precisely how many bytes return is left unspecified.

Note

Although invoking `peek()` leaves the file position of the `BZ2File` unchanged, it can shift the position of the underlying file object (for instance where the `BZ2File` was built by passing in a file object for *filename*).

Added in version 3.3.

 fileno()

Return the file descriptor for the underlying file.

Added in version 3.3.

 readable()

Return whether the file was opened for reading.

Added in version 3.3.

 seekable()

Return whether the file supports seeking.

Added in version 3.3.

 writable()

Return whether the file was opened for writing.

Added in version 3.3.

 read1(*size=-1*)

Read up to *size* uncompressed bytes, while striving to keep down the number of reads made against the underlying stream. Where size is negative, reads up to a buffer's worth of data.

Returns `b''` if the file is at EOF.

Added in version 3.3.

 readinto(*b*)

Read bytes into *b*.

Returns the number of bytes read (0 for EOF).

Added in version 3.3.

 mode

`'rb'` for reading and `'wb'` for writing.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](bz2-open.md) · [Continue](de-compression-of-files.md) · [Owning module, declaration or section: bz2](bz2-support-for-bzip2-compression.md) · [Owning module, declaration or section: (De)compression of files](bz2-open.md)
