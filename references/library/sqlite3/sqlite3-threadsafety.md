# sqlite3: `sqlite3.threadsafety`

sqlite3.threadsafety

An integer constant the DB-API 2.0 demands, declaring the thread safety level the `sqlite3` module offers. The value of this attribute follows the default [threading mode](https://sqlite.org/threadsafe.html) that the underlying SQLite library was built with. SQLite has these threading modes:

1.

**Single-thread**: Here every mutex is disabled, so using SQLite from more than one thread at a time is unsafe.

2.

**Multi-thread**: Here SQLite is safe across many threads as long as no individual database connection is shared by two or more threads simultaneously.

3.

**Serialized**: Under serialized mode, many threads may use SQLite together with no restriction.

Here is how SQLite's threading modes map onto the DB-API 2.0 threadsafety levels:

| SQLite threading mode | **threadsafety** | SQLITE_THREADSAFE | DB-API 2.0 meaning |
| --- | --- | --- | --- |
| single-thread | 0 | 0 | Threads may not share the module |
| multi-thread | 1 | 2 | Threads may share the module, but not connections |
| serialized | 3 | 1 | Threads may share the module, connections and cursors |

Changed in version 3.11: rather than being pinned to `1`, *threadsafety* is now computed dynamically.

[Subject index](INDEX.md) · [Previous](sqlite-transaction-and-version-constants.md) · [Continue](sqlite-database-configuration-flags.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: Module constants](sqlite-transaction-and-version-constants.md)
