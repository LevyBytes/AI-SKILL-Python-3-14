# Python 3.13.0 alpha 2 / library / exceptions

[gh-109538](https://github.com/python/cpython/issues/109538): When the event loop is already shut down at `StreamWriter.__del__()`, a warning is now emitted rather than surfacing [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

[gh-103791](https://github.com/python/cpython/issues/103791): Beyond its newly added handling of [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup), [`contextlib.suppress`](https://docs.python.org/3.14/library/contextlib.html#contextlib.suppress) can now also suppress exceptions that arrive within a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
