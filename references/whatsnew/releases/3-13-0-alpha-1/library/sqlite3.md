# Python 3.13.0 alpha 1 / library / sqlite3

[gh-93057](https://github.com/python/cpython/issues/93057): Supplying more than a single positional argument to [`sqlite3.connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) and to the [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) constructor is now deprecated. The leftover parameters will turn keyword-only in Python 3.15. Erlend E. Aasland authored the patch.

[gh-105375](https://github.com/python/cpython/issues/105375): Corrected a defect in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) where a raised exception might get clobbered inside the [`collation`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_collation) callback.

[gh-109151](https://github.com/python/cpython/issues/109151): Turn on `readline` editing capabilities within the [sqlite3 command-line interface](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-cli) (`python -m sqlite3`).

[gh-108278](https://github.com/python/cpython/issues/108278): Mark passing the callback callable by keyword as deprecated for these [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) APIs:

  - [`set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer)

  - [`set_progress_handler()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_progress_handler)

  - [`set_trace_callback()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_trace_callback)

These parameters are set to turn positional-only in Python 3.15.

Erlend E. Aasland wrote the patch.

[gh-64662](https://github.com/python/cpython/issues/64662): Restore handling of virtual tables within [`sqlite3.Connection.iterdump()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.iterdump). Aviv Palivoda provided the patch.

[gh-108278](https://github.com/python/cpython/issues/108278): Mark passing the name, the argument count, and the callable as keyword arguments as deprecated for these [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) APIs:

  - [`create_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_function)

  - [`create_aggregate()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_aggregate)

These parameters are set to turn positional-only in Python 3.15.

Erlend E. Aasland wrote the patch.

[gh-108083](https://github.com/python/cpython/issues/108083): Corrected defects in the constructor of [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) and in [`sqlite3.Connection.close()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.close) where exceptions might leak. Erlend E. Aasland authored the patch.

[gh-105539](https://github.com/python/cpython/issues/105539): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) now raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) whenever a [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) object isn't `closed` explicitly. Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
