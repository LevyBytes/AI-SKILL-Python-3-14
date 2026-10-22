# sqlite3 — Transaction control via the `isolation_level` attribute

#### Transaction control via the `isolation_level` attribute

Note

The advised approach to managing transactions goes through the `autocommit` attribute. Refer to Transaction control via the autocommit attribute.

When `Connection.autocommit` holds `LEGACY_TRANSACTION_CONTROL` (its default), the `Connection.isolation_level` attribute is what drives transaction behaviour. In any other case, `isolation_level` does nothing.

Whenever the connection’s `isolation_level` attribute is something other than `None`, a fresh transaction is silently begun ahead of any `INSERT`, `UPDATE`, `DELETE`, or `REPLACE` statement run through `execute()` and `executemany()`; for statements outside that set, no automatic transaction handling kicks in. Commit and roll back pending transactions with the `commit()` and `rollback()` methods, respectively. The `isolation_level` attribute lets you pick the underlying [SQLite transaction behaviour](https://www.sqlite.org/lang_transaction.html#deferred_immediate_and_exclusive_transactions) — namely whether, and which kind of, `BEGIN` statements `sqlite3` issues behind the scenes.

Should `isolation_level` carry `None`, nothing opens a transaction automatically. That keeps the underlying SQLite library in [autocommit mode](https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions) while still letting you drive transactions yourself through explicit SQL. To check the SQLite library’s autocommit mode, read the `in_transaction` attribute.

No matter what `isolation_level` is set to, the `executescript()` method quietly commits whatever transaction is pending before it runs the SQL script you hand it.

Changed in version 3.6: In earlier releases `sqlite3` would quietly commit an open transaction ahead of DDL statements; that behaviour has been removed.

Changed in version 3.12: Managing transactions through the `autocommit` attribute is now the advised approach.

[Subject index](INDEX.md) · [Previous](transaction-control-via-the-autocommit-attribute.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
