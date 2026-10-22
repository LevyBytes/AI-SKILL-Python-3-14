# Python 3.13.0 alpha 6 / core and builtins / cycle gc sizes increments according overall heap size rather

[gh-117108](https://github.com/python/cpython/issues/117108): The cycle GC now sizes its increments according to overall heap size rather than how quickly objects are allocated. That keeps it able to track heaps as they expand.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
