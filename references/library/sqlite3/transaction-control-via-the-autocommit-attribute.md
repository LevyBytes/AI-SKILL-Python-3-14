# sqlite3 - Transaction control via the `autocommit` attribute

#### Transaction control via the `autocommit` attribute

The favoured route for steering transaction behaviour runs through the `Connection.autocommit` attribute, which you ideally configure by way of the *autocommit* parameter on `connect()`.

The recommendation is to give *autocommit* the value `False`, which brings [**PEP 249**](https://peps.python.org/pep-0249/)-compliant transaction control into play. What that entails:

- `sqlite3` keeps a transaction open at all times, so `connect()`, `Connection.commit()`, and `Connection.rollback()` each silently start a fresh transaction (the latter two doing so the moment they close the pending one). To open transactions, `sqlite3` issues `BEGIN DEFERRED` statements.

- Commit each transaction yourself by calling `commit()`.

- Roll each transaction back yourself by calling `rollback()`.

- Closing the database with `close()` while changes are still pending triggers an automatic rollback.

Give *autocommit* the value `True` to switch on SQLite’s [autocommit mode](https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions). While it is active, calling `Connection.commit()` or `Connection.rollback()` does nothing. Bear in mind that this SQLite autocommit mode is a different thing from the [**PEP 249**](https://peps.python.org/pep-0249/)-compliant `Connection.autocommit` attribute; to inspect the low-level SQLite autocommit mode, consult `Connection.in_transaction`.

Assign `LEGACY_TRANSACTION_CONTROL` to *autocommit* if you want the `Connection.isolation_level` attribute to govern transaction behaviour instead. Further detail lives under Transaction control via the isolation_level attribute.

[Subject index](INDEX.md) · [Previous](transaction-control.md) · [Continue](transaction-control-via-the-isolation-level-attribute.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
