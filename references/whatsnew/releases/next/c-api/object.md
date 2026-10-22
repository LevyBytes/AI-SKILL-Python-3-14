# Python next / c api / object

[gh-123619](https://github.com/python/cpython/issues/123619): [`PyUnstable_Object_EnableDeferredRefcount()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_EnableDeferredRefcount) now hands back `0` whenever the garbage collector is not tracking the object: that is, whenever [`gc.is_tracked()`](https://docs.python.org/3.14/library/gc.html#gc.is_tracked) returns false. Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
