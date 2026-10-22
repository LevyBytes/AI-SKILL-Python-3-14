# Python 3.12.0 alpha 2 / core and builtins / global c variables tracking allocators state moved into pyruntimestate

[gh-81057](https://github.com/python/cpython/issues/81057): The 18 global C variables tracking the allocators' state have moved into `_PyRuntimeState`. This is purely an internal change that leaves behavior unchanged.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
