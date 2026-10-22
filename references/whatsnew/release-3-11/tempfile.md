# What's New In Python 3.11 / tempfile — io, tempfile

### tempfile

- Depending on file mode, [`SpooledTemporaryFile`](https://docs.python.org/3.14/library/tempfile.html#tempfile.SpooledTemporaryFile) objects now provide a complete implementation of the [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase) or [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) methods. Because of that, they interoperate properly with APIs anticipating file-like objects, compression modules among them. (Contributed by Carey Metcalfe in [gh-70363](https://github.com/python/cpython/issues/70363).)

[Subject index](INDEX.md) · [Previous source section](sysconfig.md) · [Next source section](threading.md) · [Release/subject declaration](summary-release-highlights.md)
