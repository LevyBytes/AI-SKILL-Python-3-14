# Python 3.12.0 beta 1 / library / contextlib

[gh-103791](https://github.com/python/cpython/issues/103791): Now [`contextlib.suppress`](https://docs.python.org/3.14/library/contextlib.html#contextlib.suppress) can suppress exceptions that surface inside an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup). Should the group still hold other exceptions, those get re-raised in a fresh group that leaves out the suppressed ones.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
