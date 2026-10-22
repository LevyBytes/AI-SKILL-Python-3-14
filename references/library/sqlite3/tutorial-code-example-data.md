# sqlite3 — Tutorial — Code example: data = [

```python
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

```

Observe how the `?` placeholders serve to bind `data` into the query. Reach for placeholders rather than [string formatting](https://docs.python.org/3.14/tutorial/inputoutput.html#tut-formatting) whenever you bind Python values into SQL statements, so you head off [SQL injection attacks](https://en.wikipedia.org/wiki/SQL_injection) (the How to use placeholders to bind values in SQL queries section goes deeper).

We can confirm the fresh rows landed by running a `SELECT` query once more, this time looping over what the query returns:

```pycon
>>> for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
...     print(row)
(1971, 'And Now for Something Completely Different')
(1975, 'Monty Python and the Holy Grail')
(1979, "Monty Python's Life of Brian")
(1982, 'Monty Python Live at the Hollywood Bowl')
(1983, "Monty Python's The Meaning of Life")

```

Every row arrives as a two-item [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) holding `(year, title)`, lining up with the columns the query picked out.

Lastly, confirm that the database really hit disk: invoke `con.close()` to shut the current connection, open a second one, spin up a fresh cursor, and then query the database:

```pycon
>>> con.close()
>>> new_con = sqlite3.connect("tutorial.db")
>>> new_cur = new_con.cursor()
>>> res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
>>> title, year = res.fetchone()
>>> print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
The highest scoring Monty Python movie is 'Monty Python and the Holy Grail', released in 1975
>>> new_con.close()

```

At this point you have built an SQLite database through the `sqlite3` module, loaded data into it, and pulled values back out by several different routes.

See also

- The How-to guides offer more to explore:

  - How to use placeholders to bind values in SQL queries

  - How to adapt custom Python types to SQLite values

  - How to convert SQLite values to custom Python types

  - How to use the connection context manager

  - How to create and use row factories

- The Explanation for deeper background on transaction control.

[Subject index](INDEX.md) · [
Context: Python 3.14; sqlite3 — Tutorial. Preserve the linked declaration, version, platform, error and ownership conditions.
[Source context](../INDEX.md) · [Previous](tutorial-section-introduction-and-initial-examples.md) · [Continue](sqlite3-connect-to-sqlite3-complete-statement.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: Tutorial](tutorial-section-introduction-and-initial-examples.md)
