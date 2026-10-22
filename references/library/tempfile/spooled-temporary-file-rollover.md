# tempfile / Generate temporary files and directories: `tempfile.SpooledTemporaryFile`, `rollover()`

*class *tempfile.SpooledTemporaryFile(*max_size=0*, *mode='w+b'*, *buffering=-1*, *encoding=None*, *newline=None*, *suffix=None*, *prefix=None*, *dir=None*, ***, *errors=None*)

This class works just like `TemporaryFile()`, except that the data stays buffered in memory until either the file grows past *max_size* or the file's [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method gets called; at that moment the contents are flushed to disk and things carry on as in `TemporaryFile()`.

 rollover()

The file you get carries one extra method, `rollover()`, which forces the file over to an on-disk file no matter its current size.

The object handed back is a file-like object whose `_file` attribute is either an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) or [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) object (according to whether binary or text *mode* was chosen) or else a real file object, depending on whether `rollover()` has already fired. That file-like object drops into a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement just like a regular file.

Changed in version 3.3: a *size* argument is now taken by the truncate method.

Changed in version 3.8: Added *errors* parameter.

Changed in version 3.11: Fully implements the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) and [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) abstract base classes (according to whether binary or text *mode* was chosen).

[Subject index](INDEX.md) · [Previous](tempfile-temporaryfile.md) · [Continue](temporary-directory-lifecycle.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
