# sqlite3 - SQLite and Python types

### SQLite and Python types

Out of the box, SQLite supports these types: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`.

Consequently, the Python types below can be handed to SQLite without any trouble:

| Python type | SQLite type |
| --- | --- |
| `None` | `NULL` |
| `int` | `INTEGER` |
| `float` | `REAL` |
| `str` | `TEXT` |
| `bytes` | `BLOB` |

By default, SQLite types map onto Python types in this way:

| SQLite type | Python type |
| --- | --- |
| `NULL` | `None` |
| `INTEGER` | `int` |
| `REAL` | `float` |
| `TEXT` | depends on `text_factory`, `str` by default |
| `BLOB` | `bytes` |

You can extend the `sqlite3` module's type system along two lines: object adapters let you keep extra Python types inside an SQLite database, while converters let the `sqlite3` module turn SQLite types into Python types.

[Subject index](INDEX.md) · [Previous](sqlite3-warning-to-sqlite3-notsupportederror.md) · [Continue](default-adapters-and-converters-deprecated.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
