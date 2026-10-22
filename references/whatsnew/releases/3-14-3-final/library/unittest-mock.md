# Python 3.14.3 final / library / unittest mock

[gh-142651](https://github.com/python/cpython/issues/142651): [`unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html#module-unittest.mock): resolves a thread-safety problem in which [`Mock.call_count`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.call_count) could report wrong totals once the mock was invoked at the same time from several threads.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
