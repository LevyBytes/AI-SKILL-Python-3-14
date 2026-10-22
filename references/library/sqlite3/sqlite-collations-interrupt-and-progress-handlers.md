# sqlite3.Connection: `create_collation()`, `interrupt()`, `set_authorizer()`, `set_progress_handler()`

create_collation(*name*, *callable*, */*)

Build a collation called *name* from the collating function *callable*. Two [`string`](https://docs.python.org/3.14/library/stdtypes.html#str) arguments are handed to *callable*, which ought to return an [`integer`](https://docs.python.org/3.14/library/functions.html#int):

- `1` if the first is ordered higher than the second

- `-1` if the first is ordered lower than the second

- `0` if they are ordered equal

Here is an example that performs a reverse sorting collation:

```python
def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse", collate_reverse)

cur = con.execute("CREATE TABLE test(x)")
cur.executemany("INSERT INTO test(x) VALUES(?)", [("a",), ("b",)])
cur.execute("SELECT x FROM test ORDER BY x COLLATE reverse")
for row in cur:
    print(row)
con.close()

```

To drop a collation function, set *callable* to `None`.

Changed in version 3.11: Any Unicode character is now permitted in the collation name. Previously the name accepted only ASCII characters.

 interrupt()

Invoke this method from another thread to cancel any queries that may be running on the connection. Cancelled queries will raise an `OperationalError`.

 set_authorizer(*authorizer_callback*)

Register [callable](https://docs.python.org/3.14/glossary.html#term-callable) *authorizer_callback* so that it fires on each attempt to reach a column of a table within the database. The callback ought to return one of `SQLITE_OK`, `SQLITE_DENY`, or `SQLITE_IGNORE` to indicate to the underlying SQLite library how access to the column ought to be treated.

The callback's first argument indicates which kind of operation needs authorizing. Whether the second and third argument carry values or are `None` depends on that first argument. The 4th argument holds the name of the database (“main”, “temp”, etc.) where relevant. The 5th argument carries the name of the innermost trigger or view that triggered the access attempt, or `None` when the attempt arises directly out of input SQL code.

Refer to the SQLite documentation for the permitted values of the first argument and for what the second and third argument denote given a particular first one. Every required constant lives within the `sqlite3` module.

Supplying `None` for *authorizer_callback* turns the authorizer off.

Changed in version 3.11: Added support for disabling the authorizer using `None`.

Changed in version 3.13: Supplying *authorizer_callback* by keyword is deprecated. The parameter is slated to become positional-only in Python 3.15.

 set_progress_handler(*progress_handler*, *n*)

Register [callable](https://docs.python.org/3.14/glossary.html#term-callable) *progress_handler* so that it fires after every *n* instructions of the SQLite virtual machine. This helps when you want SQLite to call you back during lengthy operations, say to refresh a GUI.

To wipe out whatever progress handler was set before, invoke the method passing `None` for *progress_handler*.

If the handler function returns a non-zero value, the query currently running ends and is made to raise a `DatabaseError` exception.

Changed in version 3.13: Supplying *progress_handler* by keyword is deprecated. The parameter is slated to become positional-only in Python 3.15.

[Subject index](INDEX.md) · [Previous](connection-objects-code-example-class-windowsumint.md) · [Continue](sqlite-trace-callbacks-and-extension-loading.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
