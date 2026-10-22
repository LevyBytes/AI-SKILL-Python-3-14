# Python 3.13.0 alpha 1 / library / asyncio

[gh-105987](https://github.com/python/cpython/issues/105987): Address a crash stemming from faulty reference counting within the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) eager task factory internal routines.

[gh-106527](https://github.com/python/cpython/issues/106527): Lower the cost of adding and removing [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) readers and writers.

[gh-82500](https://github.com/python/cpython/issues/82500): Correct an overflow seen on 32-bit systems within the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
