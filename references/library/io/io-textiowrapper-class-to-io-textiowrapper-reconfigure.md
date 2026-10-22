# io / Text I/O: `io.TextIOWrapper`, `reconfigure()`

*class *io.TextIOWrapper(*buffer*, *encoding=None*, *errors=None*, *newline=None*, *line_buffering=False*, *write_through=False*)

A buffered text stream offering more abstract access to a `BufferedIOBase` buffered binary stream. It derives from `TextIOBase`.

*encoding* names the encoding with which the stream is to be decoded or encoded. Under [UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode), its default is UTF-8. Elsewhere it defaults to [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding). Passing `encoding="locale"` lets you name the current locale’s encoding outright. Refer to Text Encoding for further detail.

*errors* is an optional string dictating how encoding and decoding errors get treated. Pass `'strict'` to raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception upon an encoding error (the `None` default behaves the same), or pass `'ignore'` to skip past errors. (Bear in mind that skipping encoding errors may cost you data.) `'replace'` drops a replacement marker (`'?'` for instance) wherever the data is malformed. `'backslashreplace'` swaps malformed data for a backslashed escape sequence. For writing, `'xmlcharrefreplace'` (swap in the suitable XML character reference) or `'namereplace'` (swap in `\N{...}` escape sequences) are options. Any further error-handling name that has been signed up through [`codecs.register_error()`](https://docs.python.org/3.14/library/codecs.html#codecs.register_error) is likewise acceptable.

*newline* governs the treatment of line endings. Its permitted values are `None`, `''`, `'\n'`, `'\r'`, and `'\r\n'`. It operates this way:

- While reading input from the stream, a *newline* of `None` switches on [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) mode. Input lines may terminate with `'\n'`, `'\r'`, or `'\r\n'`, all of which become `'\n'` before reaching the caller. A *newline* of `''` likewise switches on universal newlines mode, yet leaves the line endings untranslated when they reach the caller. With *newline* set to any of the other allowed values, input lines terminate only on the supplied string, and the line ending reaches the caller untranslated.

- While writing output to the stream, a *newline* of `None` turns every `'\n'` written into the platform’s default line separator, [`os.linesep`](https://docs.python.org/3.14/library/os.html#os.linesep). A *newline* of `''` or `'\n'` performs no translation. With *newline* set to any of the other allowed values, every `'\n'` written becomes the supplied string.

A *line_buffering* of `True` makes `flush()` happen whenever a write call holds a newline character or a carriage return.

A *write_through* of `True` promises that `write()` calls won’t be buffered: whatever gets written on the `TextIOWrapper` object goes immediately to its backing binary *buffer*.

Changed in version 3.3: The *write_through* argument has been added.

Changed in version 3.3: For the default *encoding*, `locale.getpreferredencoding(False)` replaced `locale.getpreferredencoding()`. Rather than briefly altering the locale encoding via [`locale.setlocale()`](https://docs.python.org/3.14/library/locale.html#locale.setlocale), rely on the active locale encoding in place of whichever encoding the user prefers.

Changed in version 3.10: For the *encoding* argument, the `"locale"` placeholder encoding name became accepted.

Note

Should the backing raw stream be non-blocking, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) may be raised when a read operation cannot finish right away.

Beyond what `TextIOBase` and `IOBase` provide, `TextIOWrapper` supplies these data attributes and methods:

 line_buffering

Whether line buffering is turned on.

 write_through

Whether writes go straight through to the backing binary buffer.

Added in version 3.7.

 reconfigure(***, *encoding=None*, *errors=None*, *newline=None*, *line_buffering=None*, *write_through=None*)

Reconfigure this text stream with fresh settings for *encoding*, *errors*, *newline*, *line_buffering* and *write_through*.

Any parameter left out retains its current setting, with the exception that `errors='strict'` applies when *encoding* is given but *errors* is not.

Altering the encoding or newline is impossible once any data has already been read off the stream. Changing the encoding after a write, by contrast, is allowed.

This method performs an implicit stream flush ahead of applying the new parameters.

Added in version 3.7.

Changed in version 3.11: The method supports `encoding="locale"` option.

[Subject index](INDEX.md) · [Previous](io-textiobase-detach-to-io-textiobase-write.md) · [Continue](io-textiowrapper-seek-to-io-textiowrapper-tell.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md) · [Owning module, declaration or section: Text I/O](io-textiobase-class.md)
