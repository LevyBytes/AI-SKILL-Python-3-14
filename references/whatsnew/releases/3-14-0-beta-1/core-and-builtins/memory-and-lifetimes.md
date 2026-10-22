# Python 3.14.0 beta 1 / core and builtins / memory and lifetimes

[gh-132508](https://github.com/python/cpython/issues/132508): When reraising an exception, the evaluation stack now uses tagged integers to hold instruction offsets. This removes the need to box the integer, an operation that could fail when memory is scarce.

[gh-126703](https://github.com/python/cpython/issues/126703): A possible use after free is fixed in situations where the lifetime of a method's definition matches that of its `self`.

[gh-133261](https://github.com/python/cpython/issues/133261): A bug is fixed in which the cycle GC could untrack trashcan objects because they appeared immortal. Now, when objects enter the trashcan, care is taken so that a mortal reference count is preserved.

[gh-132917](https://github.com/python/cpython/issues/132917): On the free-threaded build, the process memory usage growth is now checked before a full automatic garbage collection is launched. The collection is deferred whenever memory has grown by less than 10% since the previous one.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
