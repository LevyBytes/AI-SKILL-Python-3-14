# Python 3.14.0 beta 4 / core and builtins / trashcan mechanism confined gc ed objects untracked while sitting

[gh-135106](https://github.com/python/cpython/issues/135106): The trashcan mechanism is now confined to GC’ed objects, which are untracked while sitting in the trashcan; this stops the GC and trashcan mechanisms from conflicting.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
