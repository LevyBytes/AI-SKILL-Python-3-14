# sqlite3.Cursor: `executescript()`, `fetchone()`, `fetchmany()`, `fetchall()`, `close()`, `setinputsizes()`, `setoutputsize()`

Changed in version 3.14: `ProgrammingError` is now raised when you supply named placeholders but the entries in *parameters* are sequences rather than [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)s.

 executescript(*sql_script*, */*)

Run the SQL statements contained in *sql_script*. When `autocommit` holds `LEGACY_TRANSACTION_CONTROL` and a transaction is still pending, an implicit `COMMIT` runs beforehand. Beyond that, no further implicit transaction handling occurs; you must place any needed transaction control inside *sql_script* yourself.

*sql_script* has to be a [`string`](https://docs.python.org/3.14/library/stdtypes.html#str).

Example:

```python
# cur is an sqlite3.Cursor object
cur.executescript("""
    BEGIN;
    CREATE TABLE person(firstname, lastname, age);
    CREATE TABLE book(title, author, published);
    CREATE TABLE publisher(name, address);
    COMMIT;
""")

```

 fetchone()

When `row_factory` is `None`, hand back the upcoming row of the query result set as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). Otherwise, forward it through the row factory and yield that result. Yields `None` once nothing further remains.

 fetchmany(*size=cursor.arraysize*)

Hand back the following batch of rows from a query result as a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list). An empty list comes back when no additional rows remain.

The *size* parameter sets how many rows each invocation pulls. When *size* is omitted, the count of rows retrieved follows `arraysize`. Should the available rows total less than *size*, only that smaller number gets returned.

Keep in mind that the *size* parameter carries performance trade-offs. The arraysize attribute is generally the better choice for top performance. When you do pass the *size* parameter, holding it constant across successive `fetchmany()` invocations works best.

Changed in version 3.14.1: Supplying negative *size* values now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 fetchall()

Hand back every remaining row from a query result as a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list). An empty list comes back when no rows remain. Bear in mind the `arraysize` attribute may influence how this operation performs.

 close()

Shut the cursor immediately, instead of waiting until `__del__` runs.

From here on the cursor cannot be used; attempting any operation through it raises a `ProgrammingError` exception.

 setinputsizes(*sizes*, */*)

Mandated by the DB-API. Performs no action in `sqlite3`.

 setoutputsize(*size*, *column=None*, */*)

Mandated by the DB-API. Performs no action in `sqlite3`.

 arraysize

A read/write attribute governing how many rows `fetchmany()` hands back. Its default is 1, meaning each invocation pulls just one row.

Changed in version 3.14.1: Negative values now trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 connection

A read-only attribute exposing the SQLite database `Connection` that owns the cursor. Any `Cursor` produced by `con.cursor()` carries a `connection` attribute pointing at *con*:

```pycon
>>> con = sqlite3.connect(":memory:")
>>> cur = con.cursor()
>>> cur.connection == con
True
>>> con.close()

```

 description

A read-only attribute exposing the column names from the most recent query. For compatibility with the Python DB API, each column comes back as a 7-tuple whose final six elements are all `None`.

This is populated for `SELECT` statements too, even when no rows matched.

[Subject index](INDEX.md) · [Continue](cursor-objects.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Cursor](sqlite3-cursor-class.md) · [Owning module, declaration or section: Cursor objects](sqlite3-cursor-class.md) · [Owning module, declaration or section: executemany](sqlite3-cursor-execute-to-sqlite3-cursor-executemany.md) · [Preceding source contract and version conditions](sqlite3-cursor-execute-to-sqlite3-cursor-executemany.md)
