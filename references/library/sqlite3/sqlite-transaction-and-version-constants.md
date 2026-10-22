# sqlite3: SQLite transaction-control and version constants

### Module constants

 sqlite3.LEGACY_TRANSACTION_CONTROL

Assign `autocommit` to this constant if you want the legacy (pre-Python 3.12) style of transaction control. The details live under Transaction control via the isolation_level attribute.

 sqlite3.PARSE_DECLTYPES

Hand this flag value to the *detect_types* parameter of `connect()` so a converter function is looked up from each column's declared types. Those types get declared at the time the database table is built. `sqlite3` takes the first word of the declared type as the key into the converter dictionary when looking up a converter function. As an example:

```sql
CREATE TABLE test(
   i integer primary key,  ! will look up a converter named "integer"
   p point,                ! will look up a converter named "point"
   n number(10)            ! will look up a converter named "number"
 )

```

You can combine this flag with `PARSE_COLNAMES` through the `|` (bitwise or) operator.

Note

Generated fields (`MAX(p)` for instance) come back as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). Reach for `PARSE_COLNAMES` to impose types on such queries.

 sqlite3.PARSE_COLNAMES

Hand this flag value to the *detect_types* parameter of `connect()` so a converter function is looked up by the type name — parsed out of the query column name — used as the key into the converter dictionary. The query column name has to be enclosed in double quotes (`"`) while the type name has to be enclosed in square brackets (`[]`).

```sql
SELECT MAX(p) as "p [point]" FROM test;  ! will look up converter "point"

```

You can combine this flag with `PARSE_DECLTYPES` through the `|` (bitwise or) operator.

 sqlite3.SQLITE_OK

 sqlite3.SQLITE_DENY

 sqlite3.SQLITE_IGNORE

These are the flags the *authorizer_callback* [callable](https://docs.python.org/3.14/glossary.html#term-callable) handed to `Connection.set_authorizer()` should return, signalling whether:

- Access is allowed (`SQLITE_OK`),

- The SQL statement should be aborted with an error (`SQLITE_DENY`)

- The column should be treated as a `NULL` value (`SQLITE_IGNORE`)

 sqlite3.apilevel

A string constant declaring which DB-API level is supported. The DB-API demands it. Hard-coded to `"2.0"`.

 sqlite3.paramstyle

A string constant declaring the style of parameter marker formatting the `sqlite3` module looks for. The DB-API demands it. Hard-coded to `"qmark"`.

Note

The `named` DB-API parameter style works as well.

 sqlite3.sqlite_version

The version number of the SQLite library in use at runtime, given as a [`string`](https://docs.python.org/3.14/library/stdtypes.html#str).

 sqlite3.sqlite_version_info

The version number of the SQLite library in use at runtime, given as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) of [`integers`](https://docs.python.org/3.14/library/functions.html#int).

[Subject index](INDEX.md) · [Previous](sqlite-callback-debugging-adapters-and-converters.md) · [Continue](sqlite3-threadsafety.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
