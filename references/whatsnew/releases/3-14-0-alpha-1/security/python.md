# Python 3.14.0 alpha 1 / security / python

[gh-121957](https://github.com/python/cpython/issues/121957): Restored the audit events that had gone missing during interactive Python use; they now fire correctly for `python -i` as well as for `python -m asyncio`. Those events are `cpython.run_stdin` and `cpython.run_startup`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
