# Python 3.14.6 final / library / sys

[gh-150157](https://github.com/python/cpython/issues/150157): Repair a segfault within free-threaded builds that arises while pickling by name objects lacking a `__module__` attribute as [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) is being altered concurrently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
