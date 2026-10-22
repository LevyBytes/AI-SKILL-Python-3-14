# Python 3.14.0 alpha 3 / core and builtins / correct bookkeeping object reference count increments notably whenever single operation

[gh-127599](https://github.com/python/cpython/issues/127599): Correct the bookkeeping for object reference-count increments, notably whenever a single operation bumps a count by something larger than 1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
