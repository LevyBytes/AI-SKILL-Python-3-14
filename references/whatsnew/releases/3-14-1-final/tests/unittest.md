# Python 3.14.1 final / tests / unittest

[gh-140082](https://github.com/python/cpython/issues/140082): Adjust `python -m test` to set `FORCE_COLOR=1` whenever it runs with color enabled, so that [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest), executed by it with redirected output, still emits color.

[gh-136442](https://github.com/python/cpython/issues/136442): Return exitcode `1` rather than `5` whenever [`unittest.TestCase.setUpClass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.setUpClass) raises an exception

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
