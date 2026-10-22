# sqlite3 — How to use placeholders to bind values in SQL queries

### How-to guides

### How to use placeholders to bind values in SQL queries

SQL operations frequently rely on values held in Python variables. Steer clear, however, of stitching queries together with Python's string operations, since that opens the door to [SQL injection attacks](https://en.wikipedia.org/wiki/SQL_injection). To illustrate, an attacker need only close the single quote and slip in `OR TRUE` so that every row gets selected:

```python
>>> # Never do this -- insecure!
>>> symbol = input()
' OR TRUE; --
>>> sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
>>> print(sql)
SELECT * FROM stocks WHERE symbol = '' OR TRUE; --'
>>> cur.execute(sql)

```

Rely instead on the DB-API's parameter substitution. To drop a variable into a query string, place a placeholder there, then feed the real values into the query by handing them as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) of values to the cursor's `execute()` method as its second argument.

A given SQL statement can rely on either of two placeholder kinds: question marks (qmark style) or named placeholders (named style). In the qmark style, *parameters* has to be a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) whose length lines up with the placeholder count, otherwise a `ProgrammingError` results. In the named style, *parameters* has to be a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) instance (or a subclass) holding keys for each named parameter; surplus entries are disregarded. The following example demonstrates both styles:

```python
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

# This is the named style used with executemany():
data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()

```

Note

[**PEP 249**](https://peps.python.org/pep-0249/) numeric placeholders are *not* supported. Supplying them causes them to be read as named placeholders.

[Subject index](INDEX.md) · [Continue](how-to-adapt-custom-python-types-to-sqlite-values.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
