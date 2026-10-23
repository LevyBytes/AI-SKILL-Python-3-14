# sqlite3 - How to use the connection context manager

### How to use the connection context manager

You can employ a `Connection` object as a context manager that, on exit from the context manager body, commits or rolls back any open transactions automatically. When the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement body completes without raising, the transaction commits. Should that commit fail, or should the `with` statement body raise an uncaught exception, the transaction rolls back. When `autocommit` is `False`, committing or rolling back implicitly starts a fresh transaction.

Whenever no transaction is open as the `with` statement body is exited, or when `autocommit` is `True`, the context manager takes no action.

Note

Neither does the context manager implicitly start a new transaction nor does it close the connection. Should you require a closing context manager, look to [`contextlib.closing()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.closing).

```python
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))

# con.rollback() is called after the with block finishes with an exception,
# the exception is still raised and must be caught
try:
    with con:
        con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
except sqlite3.IntegrityError:
    print("couldn't add Python twice")

# Connection object used as context manager only commits or rollbacks transactions,
# so the connection object should be closed manually
con.close()

```

[Subject index](INDEX.md) · [Previous](how-to-use-connection-shortcut-methods.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Continue](how-to-work-with-sqlite-uris.md)
