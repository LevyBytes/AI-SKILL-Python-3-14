# Python 3.12.0 beta 1 / library / inspect

[gh-103193](https://github.com/python/cpython/issues/103193): Make [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static) faster. Alex Waygood authored the patch.

[gh-103556](https://github.com/python/cpython/issues/103556): It is no longer possible to build [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature) objects in which a positional-only parameter carrying a default precedes a positional-or-keyword parameter that lacks one.

[gh-75367](https://github.com/python/cpython/issues/75367): Correct the detection of data descriptors within [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
