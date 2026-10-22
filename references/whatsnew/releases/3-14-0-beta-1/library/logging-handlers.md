# Python 3.14.0 beta 1 / library / logging handlers

[gh-132106](https://github.com/python/cpython/issues/132106): [`logging.handlers.QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) now satisfies the context manager protocol, so you can place it inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[gh-132106](https://github.com/python/cpython/issues/132106): [`QueueListener.start`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener.start) will now throw a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) whenever the listener has already been started.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
