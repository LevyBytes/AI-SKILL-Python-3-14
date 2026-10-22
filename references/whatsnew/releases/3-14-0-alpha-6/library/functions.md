# Python 3.14.0 alpha 6 / library / functions

[gh-82987](https://github.com/python/cpython/issues/82987): Inline breakpoints such as [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) or [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) will halt the program at the calling frame every time, disregarding any `skip` pattern that may exist.

[gh-130230](https://github.com/python/cpython/issues/130230): Repairs a crash within [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) when only the third argument is a [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal).

[gh-85795](https://github.com/python/cpython/issues/85795): Drawing on [`super()`](https://docs.python.org/3.14/library/functions.html#super) plus the `__class__` [closure variable](https://docs.python.org/3.14/glossary.html#term-closure-variable) within user-defined methods of [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) subclasses is now flatly forbidden at runtime. Bartosz Sławecki landed this in [gh-130082](https://github.com/python/cpython/issues/130082).

[gh-117151](https://github.com/python/cpython/issues/117151): The value of `io.DEFAULT_BUFFER_SIZE` rises from 8k to 128k, and [`open()`](https://docs.python.org/3.14/library/functions.html#open) is tuned on platforms whose [`os.fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat) exposes a `st_blksize` field (Linux among them) so that it picks `max(min(blocksize, 8 MiB), io.DEFAULT_BUFFER_SIZE)` rather than relying on the device block size every time. The expectation is faster I/O. Romain Morotti supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
