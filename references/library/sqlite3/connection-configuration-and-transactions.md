# sqlite3: Connection autocommit and transaction control

autocommit

This attribute governs [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction behaviour. `autocommit` accepts three values:

- `False`: Pick [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction behaviour, meaning `sqlite3` keeps a transaction open at all times. Close transactions with `commit()` and `rollback()`.

This is the recommended value of `autocommit`.

- `True`: Use SQLite’s [autocommit mode](https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions). `commit()` and `rollback()` have no effect in this mode.

- `LEGACY_TRANSACTION_CONTROL`: Pre-Python 3.12 (non-[**PEP 249**](https://peps.python.org/pep-0249/)-compliant) transaction control. See `isolation_level` for more details.

This is currently the default value of `autocommit`.

Setting `autocommit` to `False` opens a fresh transaction, and setting it to `True` commits whatever transaction is pending.

See Transaction control via the autocommit attribute for more details.

Note

The `isolation_level` attribute has no effect unless `autocommit` is `LEGACY_TRANSACTION_CONTROL`.

Added in version 3.12.

 in_transaction

This read-only attribute maps to the low-level SQLite [autocommit mode](https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions).

`True` if a transaction is active (there are uncommitted changes), `False` otherwise.

Added in version 3.2.

 isolation_level

Governs the legacy transaction handling mode of `sqlite3`. When set to `None`, transactions never open implicitly. When set to one of `"DEFERRED"`, `"IMMEDIATE"`, or `"EXCLUSIVE"`, which line up with the underlying [SQLite transaction behaviour](https://www.sqlite.org/lang_transaction.html#deferred_immediate_and_exclusive_transactions), implicit transaction management takes place.

Unless the *isolation_level* parameter of `connect()` overrides it, the default is `""`, which serves as an alias for `"DEFERRED"`.

Note

Steering transaction handling through `autocommit` is preferred over relying on `isolation_level`. Unless `autocommit` carries the value `LEGACY_TRANSACTION_CONTROL` (the default), `isolation_level` does nothing.

 row_factory

The starting `row_factory` for `Cursor` objects spawned off this connection. Setting this attribute leaves the `row_factory` of existing cursors that belong to this connection untouched and applies only to new ones. Defaults to `None`, which means every row comes back as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple).

See How to create and use row factories for more details.

Changed in version 3.14.6: It is no longer permitted to delete the `row_factory` attribute.

 text_factory

A [callable](https://docs.python.org/3.14/glossary.html#term-callable) taking a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) parameter and giving back a text representation of it. SQLite values whose data type is `TEXT` cause the callable to fire. This attribute defaults to [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

See How to handle non-UTF-8 text encodings for more details.

Changed in version 3.14.6: It is no longer permitted to delete the `text_factory` attribute.

 total_changes

Return the running total of database rows that have been modified, inserted, or deleted from the moment the database connection was opened.

[Subject index](INDEX.md) · [Previous](sqlite-configuration-serialization-and-deserialization.md) · [Continue](sqlite3-cursor-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
