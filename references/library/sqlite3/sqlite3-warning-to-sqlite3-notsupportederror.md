# sqlite3 — Exceptions

### Exceptions

The DB-API 2.0 ([**PEP 249**](https://peps.python.org/pep-0249/)) lays out the exception hierarchy.

 *exception *sqlite3.Warning

The `sqlite3` module never raises this exception itself at present, though programs built on `sqlite3` might, for instance when a user-defined function truncates data during an insert. `Warning` subclasses [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception).

 *exception *sqlite3.Error

This is the parent class for the module's other exceptions. Rely on it to trap every error using one [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statement. `Error` subclasses [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception).

When the exception traces back to the SQLite library itself, these two extra attributes are attached to it:

 sqlite_errorcode

The numeric error code drawn from the [SQLite API](https://sqlite.org/rescode.html)

Added in version 3.11.

 sqlite_errorname

The symbolic name corresponding to that numeric error code from the [SQLite API](https://sqlite.org/rescode.html)

Added in version 3.11.

 *exception *sqlite3.InterfaceError

Raised when the low-level SQLite C API is misused. Put differently, encountering this exception most likely points to a bug inside the `sqlite3` module. `InterfaceError` subclasses `Error`.

 *exception *sqlite3.DatabaseError

Raised for errors tied to the database. It acts as the parent exception for various kinds of database errors. It surfaces only indirectly via the specialised subclasses. `DatabaseError` subclasses `Error`.

 *exception *sqlite3.DataError

Raised when issues with the processed data cause errors, such as numeric values exceeding their range, or overly long strings. `DataError` subclasses `DatabaseError`.

 *exception *sqlite3.OperationalError

Raised for errors connected to how the database operates, which need not be within the programmer's control. As examples, the database path may be missing, or a transaction might fail to process. `OperationalError` subclasses `DatabaseError`.

 *exception *sqlite3.IntegrityError

Raised whenever the database's relational integrity is compromised, for example a failed foreign key check. It is a subclass of `DatabaseError`.

 *exception *sqlite3.InternalError

Raised when SQLite runs into an internal error. Its appearance can signal trouble with the runtime SQLite library. `InternalError` subclasses `DatabaseError`.

 *exception *sqlite3.ProgrammingError

Raised for `sqlite3` API programming mistakes, such as passing the wrong number of bindings to a query, or attempting to work with a closed `Connection`. `ProgrammingError` subclasses `DatabaseError`.

 *exception *sqlite3.NotSupportedError

Raised whenever the underlying SQLite library does not support a given method or database API. For instance, passing `True` for *deterministic* in `create_function()` when the underlying SQLite library lacks deterministic function support. `NotSupportedError` subclasses `DatabaseError`.

[Subject index](INDEX.md) · [Previous](sqlite3-prepareprotocol-class.md) · [Continue](sqlite-and-python-types.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
