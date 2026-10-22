# Python 3.11.0 beta 1 / tests / multiprocessing

[gh-84461](https://github.com/python/cpython/issues/84461): With multiprocessing turned on, libregrtest is now able to run a Python executable besides `sys.executable` by way of the `--python` flag.

[gh-91607](https://github.com/python/cpython/issues/91607): Repair `test_concurrent_futures` so it exercises the right multiprocessing start method context in the several spots where the test logic had confused this.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
