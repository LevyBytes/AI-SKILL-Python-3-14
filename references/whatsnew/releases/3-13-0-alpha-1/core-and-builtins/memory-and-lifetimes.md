# Python 3.13.0 alpha 1 / core and builtins / memory and lifetimes

[gh-105235](https://github.com/python/cpython/issues/105235): Stop out-of-bounds memory reads from happening over the course of `mmap.find()` calls.

[gh-106092](https://github.com/python/cpython/issues/106092): Resolve a segmentation fault stemming from a use-after-free defect inside `frame_dealloc` once the trashcan postpones freeing a `PyFrameObject`.

[gh-104584](https://github.com/python/cpython/issues/104584): A reference leak that appeared when `PYTHONUOPS` or [`-X uops`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) was turned on is now fixed.

[gh-84436](https://github.com/python/cpython/issues/84436): Reference count changes are now skipped for many objects that are known to be immortal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
