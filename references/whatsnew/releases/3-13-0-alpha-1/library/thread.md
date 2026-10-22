# Python 3.13.0 alpha 1 / library / thread

[gh-108987](https://github.com/python/cpython/issues/108987): Resolved a [`_thread.start_new_thread()`](https://docs.python.org/3.14/library/_thread.html#thread.start_new_thread) race condition. When a thread is spawned during Python finalization, the freshly created thread now quits straight away rather than reaching for freed memory and triggering a crash. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
