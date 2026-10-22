# sqlite3: `sqlite3.connect()`, `sqlite3.complete_statement()`

### Reference

### Module functions

 sqlite3.connect(*database*, *timeout=5.0*, *detect_types=0*, *isolation_level='DEFERRED'*, *check_same_thread=True*, *factory=sqlite3.Connection*, *cached_statements=128*, *uri=False*, ***, *autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL*)

Open a connection to an SQLite database.

Parameters:

- **database** ([path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object)) – The path of the database file you want to open. Passing `":memory:"` makes an [SQLite database existing only in memory](https://sqlite.org/inmemorydb.html), and opens a connection onto it.

- **timeout** ([*float*](https://docs.python.org/3.14/library/functions.html#float)) – The number of seconds the connection holds off before it raises an `OperationalError` for a locked table. Whenever some other connection starts a transaction that alters a table, that table stays locked until its transaction commits. Default five seconds.

- **detect_types** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – Govern whether, and in what way, data types that SQLite does not natively handle get looked up so they convert to Python types, drawing on the converters registered through `register_converter()`. Turn this on by setting it to any mix (joined with `|`, bitwise or) of `PARSE_DECLTYPES` and `PARSE_COLNAMES`. When both flags are present, column names win over declared types. The default (`0`) leaves type detection off.

- **isolation_level** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*) – Govern the legacy transaction handling behaviour. Refer to `Connection.isolation_level` plus Transaction control via the isolation_level attribute for the details. It accepts `"DEFERRED"` (default), `"EXCLUSIVE"` or `"IMMEDIATE"`; pass `None` to stop transactions being opened implicitly. It does nothing unless `Connection.autocommit` carries the value `LEGACY_TRANSACTION_CONTROL` (the default).

- **check_same_thread** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True` (default), a `ProgrammingError` is raised should the database connection be touched by any thread besides the one that built it. When `False`, several threads may reach the connection; the user might have to serialize write operations to keep data from being corrupted. Refer to `threadsafety` for the details.

- **factory** (*Connection*) – A bespoke subclass of `Connection` used to build the connection, in place of the default `Connection` class.

- **cached_statements** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How many statements `sqlite3` keeps cached internally for this connection so as to skip parsing overhead. The default is 128 statements.

- **uri** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When this is `True`, *database* is read as a URI carrying a file path together with an optional query string. The scheme portion *must* read `"file:"`, while the path may be either relative or absolute. Parameters can be handed to SQLite through the query string, enabling various How to work with SQLite URIs.

- **autocommit** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – Govern the [**PEP 249**](https://peps.python.org/pep-0249/) transaction handling behaviour. Refer to `Connection.autocommit` plus Transaction control via the autocommit attribute for the details. As of now, *autocommit* defaults to `LEGACY_TRANSACTION_CONTROL`. That default is set to switch to `False` in some later Python release.

Return type:

*Connection*

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `sqlite3.connect` with argument `database`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `sqlite3.connect/handle` with argument `connection_handle`.

Changed in version 3.4: Added the *uri* parameter.

Changed in version 3.7: besides a string, *database* may now be supplied as a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) too.

Changed in version 3.10: Added the `sqlite3.connect/handle` auditing event.

Changed in version 3.12: Added the *autocommit* parameter.

Changed in version 3.13: supplying *timeout*, *detect_types*, *isolation_level*, *check_same_thread*, *factory*, *cached_statements*, and *uri* positionally is now deprecated; come Python 3.15 each turns into a keyword-only parameter.

 sqlite3.complete_statement(*statement*)

Returns `True` whenever the string *statement* looks like it holds one or more finished SQL statements. Beyond confirming that no string literals stay unclosed and that a semicolon terminates the statement, it runs no syntax verification or parsing whatsoever.

For example:

```pycon
>>> sqlite3.complete_statement("SELECT foo FROM bar;")
True
>>> sqlite3.complete_statement("SELECT foo")
False

```

You may find this function handy at a command-line prompt, to judge whether the text typed looks like a finished SQL statement, or whether more input is wanted ahead of calling `execute()`.

Refer to `runsource()` within [Lib/sqlite3/__main__.py](https://github.com/python/cpython/tree/3.14/Lib/sqlite3/__main__.py) for a real-world example.

[Subject index](INDEX.md) · [Continue](sqlite-callback-debugging-adapters-and-converters.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
