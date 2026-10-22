# sqlite3: SQLite connection row and text factories

Register or delete a user-defined SQL aggregate function.

Parameters:

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the SQL aggregate function.

- **n_arg** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How many arguments the SQL aggregate function will accept. A value of `-1` lets it accept an arbitrary count of arguments.

- **aggregate_class** ([class](https://docs.python.org/3.14/glossary.html#term-class) | None) –

A class that has to provide these methods:

  - `step()`: Add a row to the aggregate.

  - `finalize()`: Hand back the aggregate's final result as a type that SQLite natively understands.

The count of arguments the `step()` method has to take is governed by *n_arg*.

Pass `None` here to delete a SQL aggregate function that already exists.

Example:

```python
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.execute("CREATE TABLE test(i)")
cur.execute("INSERT INTO test(i) VALUES(1)")
cur.execute("INSERT INTO test(i) VALUES(2)")
cur.execute("SELECT mysum(i) FROM test")
print(cur.fetchone()[0])

con.close()

```

Changed in version 3.13: Supplying *name*, *n_arg*, and *aggregate_class* by keyword is deprecated. In Python 3.15 these parameters are slated to become positional-only.

[Subject index](INDEX.md) · [Continue](sqlite3-connection-create-window-function.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md) · [Owning module, declaration or section: create_aggregate](sqlite-custom-functions-and-aggregates.md) · [Preceding source contract and version conditions](sqlite-custom-functions-and-aggregates.md)
