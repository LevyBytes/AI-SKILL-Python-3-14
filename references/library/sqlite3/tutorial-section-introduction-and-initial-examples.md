# sqlite3 — Tutorial — Section introduction and initial examples

### Tutorial

Across this tutorial you build a catalog of Monty Python films by leaning on core `sqlite3` features. The text presumes you already grasp the basics of databases, [cursors](https://en.wikipedia.org/wiki/Cursor_(databases)) and [transactions](https://en.wikipedia.org/wiki/Database_transaction) among them.

To begin, a fresh database has to be made and a connection opened so `sqlite3` can operate on it. Invoke `sqlite3.connect()` to obtain a connection to the `tutorial.db` database within the working directory you are in, which is created on the fly when it is absent:

```python
import sqlite3
con = sqlite3.connect("tutorial.db")

```

That `Connection` object `con` you get back stands for the link to the on-disk database.

To run SQL statements and gather the output of SQL queries, a database cursor is required. Invoke `con.cursor()` to make the `Cursor`:

```python
cur = con.cursor()

```

With both a connection and a cursor in hand, we can build a database table `movie` holding columns for the title, the release year, and a review score. To keep things simple, the table declaration can list bare column names — SQLite's [flexible typing](https://www.sqlite.org/flextypegood.html) means declaring data types is not mandatory. Run the `CREATE TABLE` statement through `cur.execute(...)`:

```python
cur.execute("CREATE TABLE movie(title, year, score)")

```

To confirm the new table exists, query SQLite's built-in `sqlite_master` table, which should by now hold a record for the `movie` table definition (consult [The Schema Table](https://www.sqlite.org/schematab.html) for the specifics). Run that query via `cur.execute(...)`, bind the outcome to `res`, then invoke `res.fetchone()` to grab the row that comes back:

```pycon
>>> res = cur.execute("SELECT name FROM sqlite_master")
>>> res.fetchone()
('movie',)

```

The table clearly exists, because the query yields a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) holding the name of the table. Querying `sqlite_master` for a table named `spam` that doesn't exist makes `res.fetchone()` give back `None`:

```pycon
>>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
>>> res.fetchone() is None
True

```

Next, insert two data rows given directly as SQL literals by running an `INSERT` statement, again through `cur.execute(...)`:

```python
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

```

Running an `INSERT` statement quietly begins a transaction, and that transaction must be committed before the changes land in the database (the Transaction control section has the specifics). Invoke `con.commit()` on the connection object to commit the transaction:

```python
con.commit()

```

To check that the rows landed properly, run a `SELECT` query. Reach for the by-now-familiar `cur.execute(...)` to bind the outcome to `res`, then invoke `res.fetchall()` to hand back every row that resulted:

```pycon
>>> res = cur.execute("SELECT score FROM movie")
>>> res.fetchall()
[(8.2,), (7.5,)]

```

What comes back is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) holding two `tuple`s — one for each row — and every tuple carries that row's `score` value.

Next, append three further rows by invoking `cur.executemany(...)`:

[Subject index](INDEX.md) · [Previous](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Continue](tutorial-code-example-data.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
