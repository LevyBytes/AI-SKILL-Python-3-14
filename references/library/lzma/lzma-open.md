# lzma: `lzma.open()`

### Reading and writing compressed files

 lzma.open(*filename*, *mode='rb'*, ***, *format=None*, *check=-1*, *preset=None*, *filters=None*, *encoding=None*, *errors=None*, *newline=None*)

Open up an LZMA-compressed file in either binary or text mode; the call hands back a [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

For the *filename* argument you may pass a genuine file name (supplied as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) object), which opens that named file, or alternatively an already-open file object to be read from or written to.

Permitted values for the *mode* argument are `"r"`, `"rb"`, `"w"`, `"wb"`, `"x"`, `"xb"`, `"a"` or `"ab"` when working in binary, or `"rt"`, `"wt"`, `"xt"`, or `"at"` when working in text. It defaults to `"rb"`.

While opening a file to read, the *format* and *filters* arguments carry the same significance they do for `LZMADecompressor`. Under those circumstances, leave the *check* and *preset* arguments unused.

While opening a file to write, the *format*, *check*, *preset* and *filters* arguments take on the same significance they hold for `LZMACompressor`.

In binary mode this call behaves the same as the `LZMAFile` constructor: `LZMAFile(filename, mode, ...)`. Under those conditions, you must omit the *encoding*, *errors* and *newline* arguments.

For text mode, an `LZMAFile` object gets built and then wrapped inside an [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) instance carrying the chosen encoding, error-handling policy, and line ending(s).

Changed in version 3.4: Added support for the `"x"`, `"xb"` and `"xt"` modes.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](lzma-lzmaerror.md) · [Continue](lzma-lzmafile-class-to-lzma-lzmafile-peek.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md)
