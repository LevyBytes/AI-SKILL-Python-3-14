# What's New In Python 3.11 / gzip — gzip, zlib

### gzip

- The [`gzip.compress()`](https://docs.python.org/3.14/library/gzip.html#gzip.compress) function now runs quicker with the **mtime=0** argument, since it hands the whole compression job off to a single [`zlib.compress()`](https://docs.python.org/3.14/library/zlib.html#zlib.compress) call. This carries one consequence: a gzip file header holds an "OS" byte. By convention the [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module always wrote 255 there to mean "unknown". These days, calling `compress()` with **mtime=0** may leave a different value, chosen by whichever zlib C library Python was linked against. (Refer to [gh-112346](https://github.com/python/cpython/issues/112346) for specifics about this consequence.)

[Subject index](INDEX.md) · [Previous source section](functools.md) · [Next source section](hashlib.md) · [Release/subject declaration](summary-release-highlights.md)
