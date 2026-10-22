# sqlite3: `sqlite3.Cursor`

### Cursor objects

>

A `Cursor` object stands for a [database cursor](https://en.wikipedia.org/wiki/Cursor_(databases)) used to run SQL statements and to track the state of a fetch operation. You create cursors with `Connection.cursor()` or through any of the connection shortcut methods.

Cursor objects are [iterators](https://docs.python.org/3.14/glossary.html#term-iterator); that means once you `execute()` a `SELECT` query, you can iterate straight over the cursor to retrieve the resulting rows:

```python
for row in cur.execute("SELECT t FROM data"):
    print(row)

```

 *class *sqlite3.Cursor

A `Cursor` instance has the following attributes and methods.

[Subject index](INDEX.md) · [Previous](connection-configuration-and-transactions.md) · [Continue](sqlite3-cursor-execute-to-sqlite3-cursor-executemany.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
