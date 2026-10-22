# Python 3.14.0 alpha 6 / library / io

[gh-128647](https://github.com/python/cpython/issues/128647): Writes eagerly into buffers handed to the [`readinto()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.readinto) and [`readinto1()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.readinto1) implementations of [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile), which sidesteps needless allocations. Chris Markiewicz wrote this patch.

[gh-127647](https://github.com/python/cpython/issues/127647): The protocols [`io.Reader`](https://docs.python.org/3.14/library/io.html#io.Reader) and [`io.Writer`](https://docs.python.org/3.14/library/io.html#io.Writer) are now available, serving as substitutes for [`typing.IO`](https://docs.python.org/3.14/library/typing.html#typing.IO), [`typing.TextIO`](https://docs.python.org/3.14/library/typing.html#typing.TextIO), and [`typing.BinaryIO`](https://docs.python.org/3.14/library/typing.html#typing.BinaryIO).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
