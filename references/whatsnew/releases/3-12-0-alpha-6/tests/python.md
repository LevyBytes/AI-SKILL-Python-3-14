# Python 3.12.0 alpha 6 / tests / python

[gh-89792](https://github.com/python/cpython/issues/89792): During the `freeze` test, `test_tools` now transfers as much as 10x less source data into a scratch directory because it skips git metadata along with other artifacts. Its python build parallelism is likewise capped according to os.cpu_count rather than a fixed value of 8 cores.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
