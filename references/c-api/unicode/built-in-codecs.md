# Built-in Codecs

### Built-in Codecs

For speed, Python ships a collection of built-in codecs implemented in C. Each one of them can be used directly through the routines below.

A good many of the APIs that follow accept the pair of arguments encoding and errors, whose semantics line up with those belonging to the built-in [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) string object constructor.

Leaving encoding as `NULL` selects the default encoding, namely UTF-8. For encoding file names, the file system calls ought to rely on `PyUnicode_FSConverter()`. Internally that draws on the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

The errors argument governs error handling and may likewise be left as `NULL`, signaling that the codec's own default handling should apply. Across every built-in codec the default error handling is “strict” (a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised).

A common interface is shared among all the codecs. For brevity, only the places where one departs from the generic descriptions below are spelled out.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-fromwidechar-to-pyunicode-aswidecharstring.md) · [Following source contract](py-unicode-replacement-character-to-pyunicode-asencodedstring.md)
