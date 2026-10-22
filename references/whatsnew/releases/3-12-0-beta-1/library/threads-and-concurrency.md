# Python 3.12.0 beta 1 / library / threads and concurrency

[gh-96522](https://github.com/python/cpython/issues/96522): Resolve a possible deadlock within pty.spawn()

[gh-104536](https://github.com/python/cpython/issues/104536): Resolve a race condition inside the internal `multiprocessing.process` cleanup path that could surface as an unexpected `AttributeError` while invoking `process.close()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
