# io.IOBase: `close()`, `fileno()`, `flush()`, `isatty()`, `readable()`, `readline()`, `readlines()`, `seek()`, `seekable()`, `tell()`, `truncate()`, `writable()`, `writelines()`

close()

Flush this stream and close it. Where the file has already been closed, this method does nothing. After the file is closed, any further operation on it (reading or writing, for instance) will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

For convenience, calling this method repeatedly is permitted; nevertheless, only the initial call takes effect.

 closed

`True` if the stream is closed.

 fileno()

Return the stream's underlying file descriptor (an integer), should one exist. Where the IO object works without a file descriptor, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised.

 flush()

Flush the stream's write buffers where that applies. For read-only and non-blocking streams this is a no-op.

 isatty()

Return `True` whenever the stream is interactive — that is, hooked up to a terminal/tty device.

 readable()

Return `True` if the stream can be read from. If `False`, `read()` will raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 readline(*size=-1*, */*)

Read a single line from the stream and return it. When *size* is given, no more than *size* bytes are read.

For binary files the line terminator is invariably `b'\n'`; for text files, the *newline* argument supplied to [`open()`](https://docs.python.org/3.14/library/functions.html#open) determines which line terminator(s) are recognized.

 readlines(*hint=-1*, */*)

Read lines from the stream and return them as a list. You can supply *hint* to govern how many lines are read: once the combined size (in bytes/characters) of the lines gathered so far passes *hint*, no further lines are read.

A *hint* of `0` or below, and likewise `None`, counts as supplying no hint at all.

Keep in mind that you can already iterate over file objects with `for line in file: ...`, with no call to `file.readlines()` needed.

 seek(*offset*, *whence=os.SEEK_SET*, */*)

Move the stream position to the byte *offset* given, taken relative to the position that *whence* designates, and return the resulting absolute position. The values *whence* can take are:

- [`os.SEEK_SET`](https://docs.python.org/3.14/library/os.html#os.SEEK_SET) or `0` – the stream's beginning (this is the default); here *offset* ought to be zero or positive

- [`os.SEEK_CUR`](https://docs.python.org/3.14/library/os.html#os.SEEK_CUR) or `1` – wherever the stream currently sits; here *offset* is allowed to be negative

- [`os.SEEK_END`](https://docs.python.org/3.14/library/os.html#os.SEEK_END) or `2` – the stream's end; here *offset* tends to be negative

Added in version 3.1: The `SEEK_*` constants.

Added in version 3.3: Certain operating systems might allow further values, such as [`os.SEEK_HOLE`](https://docs.python.org/3.14/library/os.html#os.SEEK_HOLE) or [`os.SEEK_DATA`](https://docs.python.org/3.14/library/os.html#os.SEEK_DATA). Which values are valid for a file may hinge on whether it was opened in text or binary mode.

 seekable()

Return `True` if the stream supports random access. If `False`, `seek()`, `tell()` and `truncate()` will raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 tell()

Return the current stream position.

 truncate(*size=None*, */*)

Resize the stream to the *size* in bytes provided (or to the current position when *size* is left out). The current stream position stays put. Such resizing may grow or shrink the present file size. Where it grows, what fills the newly added file region is platform-dependent (on most systems, the extra bytes are zero-filled). The resulting file size is returned.

Changed in version 3.5: When a file is extended on Windows, it now gets zero-filled.

 writable()

Return `True` if the stream supports writing. If `False`, `write()` and `truncate()` will raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 writelines(*lines*, */*)

Write a list of lines to the stream. Because line separators aren't inserted, each line you provide ordinarily carries a line separator at its end.

[Subject index](INDEX.md) · [Previous](io-iobase-class.md) · [Continue](io-iobase-del.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: io.IOBase](io-iobase-class.md) · [Owning module, declaration or section: I/O Base Classes](io-iobase-class.md)
