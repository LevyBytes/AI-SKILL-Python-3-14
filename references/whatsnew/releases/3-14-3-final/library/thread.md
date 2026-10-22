# Python 3.14.3 final / library / thread

[gh-143191](https://github.com/python/cpython/issues/143191): [`_thread.stack_size()`](https://docs.python.org/3.14/library/_thread.html#thread.stack_size) now raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the stack size is too small. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
