# Python 3.14.0 alpha 6 / library / traceback

[gh-96092](https://github.com/python/cpython/issues/96092): Repairs a bug where [`traceback.walk_stack()`](https://docs.python.org/3.14/library/traceback.html#traceback.walk_stack) invoked with None was bypassing more frames than earlier versions did. The same fix also makes walk_stack traverse the stack starting in the frame where it was called instead of where it first sees use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
