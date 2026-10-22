# Python 3.14.0 alpha 3 / tests / io

[gh-127076](https://github.com/python/cpython/issues/127076): When checking [`io`](https://docs.python.org/3.14/library/io.html#module-io) behaviour via strace, strip the memory-oriented `mmap`, `munmap`, and `mprotect` calls away from the file-oriented ones.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
