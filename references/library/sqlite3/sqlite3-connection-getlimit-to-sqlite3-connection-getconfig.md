# sqlite3.Connection: `getlimit()`, `setlimit()`, `getconfig()`

getlimit(*category*, */*)

Get a connection runtime limit.

Parameters:

**category** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The [SQLite limit category](https://www.sqlite.org/c3ref/c_limit_attached.html) to be queried.

Return type:

[int](https://docs.python.org/3.14/library/functions.html#int)

Raises:

**ProgrammingError** – If *category* is not recognised by the underlying SQLite library.

Example that fetches, for `Connection` `con`, the longest an SQL statement may be (the default is 1000000000):

```pycon
>>> con.getlimit(sqlite3.SQLITE_LIMIT_SQL_LENGTH)
1000000000

```

Added in version 3.11.

 setlimit(*category*, *limit*, */*)

Set a connection runtime limit. Any attempt to raise a limit past its hard upper bound is quietly clamped down to that hard upper bound. Whether or not the limit ended up changing, the limit's previous value is returned.

Parameters:

- **category** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The [SQLite limit category](https://www.sqlite.org/c3ref/c_limit_attached.html) to be set.

- **limit** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – What the new limit should be. A negative value leaves the existing limit as it is.

Return type:

[int](https://docs.python.org/3.14/library/functions.html#int)

Raises:

**ProgrammingError** – If *category* is not recognised by the underlying SQLite library.

Example that caps the count of attached databases at 1 for `Connection` `con` (the default limit is 10):

```pycon
>>> con.setlimit(sqlite3.SQLITE_LIMIT_ATTACHED, 1)
10
>>> con.getlimit(sqlite3.SQLITE_LIMIT_ATTACHED)
1

```

Added in version 3.11.

 getconfig(*op*, */*)

Query a boolean connection configuration option.

Parameters:

**op** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – A SQLITE_DBCONFIG code.

Return type:

[bool](https://docs.python.org/3.14/library/functions.html#bool)

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](sqlite3-connection-backup.md) · [Continue](sqlite-configuration-serialization-and-deserialization.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
