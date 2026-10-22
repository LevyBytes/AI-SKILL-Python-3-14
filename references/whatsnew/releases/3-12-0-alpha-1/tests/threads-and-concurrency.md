# Python 3.12.0 alpha 1 / tests / threads and concurrency

[gh-95243](https://github.com/python/cpython/issues/95243): Reduce the built-in race condition that find_unused_port() introduces in testSockName() by attempting to locate a free port several times prior to giving up. Ross Burton wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
