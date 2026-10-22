# Python 3.14.0 beta 1 / library / traceback

[gh-132385](https://github.com/python/cpython/issues/132385): Stop instance error suggestions from raising unexpected exceptions inside [`object.__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) within [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback).

[gh-132308](https://github.com/python/cpython/issues/132308): A [`traceback.TracebackException`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException) now properly renders the `__context__` plus `__cause__` attributes drawn from a [falsey](https://docs.python.org/3.14/library/stdtypes.html#truth) [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception), along with the `exceptions` attribute taken from a falsey [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
