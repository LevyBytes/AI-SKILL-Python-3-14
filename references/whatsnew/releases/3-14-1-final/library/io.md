# Python 3.14.1 final / library / io

[gh-132551](https://github.com/python/cpython/issues/132551): Render [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) safe under the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[gh-140607](https://github.com/python/cpython/issues/140607): During [`io.RawIOBase.read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read), the byte count handed back by [`io.RawIOBase.readinto()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.readinto) is now checked for validity (that it stays within the supplied buffer).

[gh-141570](https://github.com/python/cpython/issues/141570): Color detection (`_colorize.can_colorize()`) now tolerates a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) whose [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) throws [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). Redirecting `sys.stdout` is one way to trigger that.

[gh-141314](https://github.com/python/cpython/issues/141314): An assertion failure inside [`io.TextIOWrapper.tell()`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper.tell), seen when reading files that use lone carriage return (`\r`) line endings, is fixed.

[gh-141311](https://github.com/python/cpython/issues/141311): Corrects an assertion failure in `io.BytesIO.readinto()` together with the undefined behavior that occurred when the read position sat above capcity inside [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
