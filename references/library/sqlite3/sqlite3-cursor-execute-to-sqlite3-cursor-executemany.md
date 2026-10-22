# sqlite3.Cursor: `execute()`, `executemany()`

execute(*sql*, *parameters=()*, */*)

Run a single SQL statement, optionally binding Python values through placeholders.

Parameters:

- **sql** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A single SQL statement.

- **parameters** ([`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) | [sequence](https://docs.python.org/3.14/glossary.html#term-sequence)) – The Python values that get bound to the placeholders within *sql*. Supply a `dict` for named placeholders, or a sequence for unnamed placeholders. See How to use placeholders to bind values in SQL queries.

Raises:

**ProgrammingError** – When more than one SQL statement sits inside *sql*. Also when named placeholders appear yet *parameters* arrives as a sequence rather than a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

If `autocommit` is `LEGACY_TRANSACTION_CONTROL`, `isolation_level` is not `None`, *sql* is an `INSERT`, `UPDATE`, `DELETE`, or `REPLACE` statement, and no transaction is open, then a transaction opens implicitly ahead of running *sql*.

Changed in version 3.14: A `ProgrammingError` now gets raised whenever named placeholders appear while *parameters* comes in as a sequence rather than a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

Use `executescript()` to execute multiple SQL statements.

 executemany(*sql*, *parameters*, */*)

For each item found in *parameters*, run the parameterized DML SQL statement *sql* over and over.

Uses the same implicit transaction handling as `execute()`.

Parameters:

- **sql** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A single SQL DML statement.

- **parameters** ([iterable](https://docs.python.org/3.14/glossary.html#term-iterable)) – An iterable whose parameters bind to the placeholders held within *sql*. Consult How to use placeholders to bind values in SQL queries.

Raises:

**ProgrammingError** – When *sql* holds more than one SQL statement or isn't a DML statement, When named placeholders appear and the entries in *parameters* are sequences in place of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)s.

Example:

```python
rows = [
    ("row1",),
    ("row2",),
]
# cur is an sqlite3.Cursor object
cur.executemany("INSERT INTO data VALUES(?)", rows)

```

Note

Any resulting rows are discarded, including DML statements with [RETURNING clauses](https://www.sqlite.org/lang_returning.html).

[Subject index](INDEX.md) · [Previous](sqlite3-cursor-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Cursor](sqlite3-cursor-class.md) · [Owning module, declaration or section: Cursor objects](sqlite3-cursor-class.md) · [Required continuation of the source contract](sqlite3-cursor-executescript-to-sqlite3-cursor-setoutputsize.md)
