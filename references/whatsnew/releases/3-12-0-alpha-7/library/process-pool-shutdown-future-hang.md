# Python 3.12.0 alpha 7 / library / resolve concurrent futures process defect processpoolexecutor shutdown might hang once future

[gh-94440](https://github.com/python/cpython/issues/94440): Resolve a `concurrent.futures.process` defect in which `ProcessPoolExecutor` shutdown might hang once a future had been promptly submitted and then canceled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
