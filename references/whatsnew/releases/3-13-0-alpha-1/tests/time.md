# Python 3.13.0 alpha 1 / tests / time

[gh-109974](https://github.com/python/cpython/issues/109974): Eliminated race conditions among the test_threading lock tests. Block until some condition holds rather than calling [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) with a fixed second count. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
