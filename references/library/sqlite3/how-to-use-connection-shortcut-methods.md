# sqlite3 — How to use connection shortcut methods

### How to use connection shortcut methods

By calling the `execute()`, `executemany()`, and `executescript()` methods on the `Connection` class, you can keep your code more compact, since there's no need to spin up the (frequently needless) `Cursor` objects yourself. The `Cursor` objects come into being implicitly instead, and these shortcut methods return them. In this fashion, a single call on the `Connection` object lets you run a `SELECT` statement and walk over it straight away.

```python
# Create and fill the table.
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(name, first_appeared)")
data = [
    ("C++", 1985),
    ("Objective-C", 1984),
]
con.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

# Print the table contents
for row in con.execute("SELECT name, first_appeared FROM lang"):
    print(row)

print("I just deleted", con.execute("DELETE FROM lang").rowcount, "rows")

# close() is not a shortcut method and it's not called automatically;
# the connection object should be closed manually
con.close()

```

[Subject index](INDEX.md) · [Previous](adapter-and-converter-recipes.md) · [Continue](how-to-use-the-connection-context-manager.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
