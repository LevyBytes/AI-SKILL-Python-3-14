# sqlite3.Connection: `cursor()`, `blobopen()`, `commit()`, `rollback()`, `close()`, `execute()`, `executemany()`, `executescript()`

cursor(*factory=Cursor*)

Builds and returns a `Cursor` object. The cursor method takes one optional parameter, *factory*. When you pass it, it has to be a [callable](https://docs.python.org/3.14/glossary.html#term-callable) that returns an instance of `Cursor` or one of its subclasses.

 blobopen(*table*, *column*, *rowid*, */*, ***, *readonly=False*, *name='main'*)

Open a `Blob` handle to an existing BLOB.

Parameters:

- **table** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the table holding the blob.

- **column** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the column holding the blob.

- **rowid** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The row id at which the blob sits.

- **readonly** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – Pass `True` to open the blob with no write permissions. The default is `False`.

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the database holding the blob. The default is `"main"`.

Raises:

**OperationalError** – When trying to open a blob in a `WITHOUT ROWID` table.

Return type:

Blob

Note

You cannot resize the blob through the `Blob` class. Reach for the SQL function `zeroblob` to make a blob of a set size.

Added in version 3.11.

 commit()

Commits whatever transaction is pending into the database. When `autocommit` is `True`, or no transaction is open, this method does nothing. When `autocommit` is `False`, this method implicitly opens a fresh transaction once it commits a pending one.

 rollback()

Rolls back to where any pending transaction began. When `autocommit` is `True`, or no transaction is open, this method does nothing. When `autocommit` is `False`, this method implicitly opens a fresh transaction once it rolls back a pending one.

 close()

Closes the database connection. When `autocommit` is `False`, any pending transaction is rolled back implicitly. When `autocommit` is `True` or `LEGACY_TRANSACTION_CONTROL`, no implicit transaction control happens. Be sure to `commit()` ahead of closing so you don't drop pending changes.

 execute(*sql*, *parameters=()*, */*)

Builds a new `Cursor` object and runs `execute()` on it using the supplied *sql* and *parameters*. Returns that new cursor object.

 executemany(*sql*, *parameters*, */*)

Builds a new `Cursor` object and runs `executemany()` on it using the supplied *sql* and *parameters*. Returns that new cursor object.

 executescript(*sql_script*, */*)

Builds a new `Cursor` object and runs `executescript()` on it using the supplied *sql_script*. Returns that new cursor object.

[Subject index](INDEX.md) · [Previous](sqlite3-connection-class.md) · [Continue](sqlite-custom-functions-and-aggregates.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
