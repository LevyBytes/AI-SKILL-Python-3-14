# sqlite3 - How to work with SQLite URIs

### How to work with SQLite URIs

A few handy things you can do with URIs:

- Open a database for reading only:

```pycon
>>> con = sqlite3.connect("file:tutorial.db?mode=ro", uri=True)
>>> con.execute("CREATE TABLE readonly(data)")
Traceback (most recent call last):
OperationalError: attempt to write a readonly database
>>> con.close()

```

- Avoid silently creating a fresh database file when one is not already present; an `OperationalError` is raised should the new file fail to be created:

```pycon
>>> con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
Traceback (most recent call last):
OperationalError: unable to open database file

```

- Set up a named in-memory database that can be shared:

```python
db = "file:mem1?mode=memory&cache=shared"
con1 = sqlite3.connect(db, uri=True)
con2 = sqlite3.connect(db, uri=True)
with con1:
    con1.execute("CREATE TABLE shared(data)")
    con1.execute("INSERT INTO shared VALUES(28)")
res = con2.execute("SELECT data FROM shared")
assert res.fetchone() == (28,)

con1.close()
con2.close()

```

Further details on this capability, along with the full set of parameters, are available in the [SQLite URI documentation](https://www.sqlite.org/uri.html).

[Subject index](INDEX.md) · [Previous](how-to-use-the-connection-context-manager.md) · [Continue](how-to-create-and-use-row-factories.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
