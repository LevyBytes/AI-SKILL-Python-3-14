# Python 2.5 changes: SQLite package introduction and connection example

### The sqlite3 package

The pysqlite module ([https://www.pysqlite.org](https://www.pysqlite.org)), which wraps the SQLite embedded database, is now in the standard library under the package name [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3).

SQLite is a C library furnishing a lightweight disk-based database that needs no separate server process and lets you reach the database through a nonstandard flavour of the SQL query language. Certain applications may turn to SQLite for their internal data storage. You can equally prototype an application on SQLite and afterward move the code to a heftier database such as PostgreSQL or Oracle.

pysqlite is the work of Gerhard Häring and supplies a SQL interface that conforms to the DB-API 2.0 specification set out in [**PEP 249**](https://peps.python.org/pep-0249/).

Should you build the Python source on your own, be aware that the source tree carries only the wrapper module, not the SQLite code itself. The SQLite libraries and headers must already be installed before you compile Python, and the build will compile the module once the needed headers are present.

Using the module begins with creating a `Connection` object standing for the database. In this case the data lands in the `/tmp/example` file:

```python
conn = sqlite3.connect('/tmp/example')

```

The special name `:memory:` is also accepted, which builds a database in RAM.

Holding a `Connection`, you can build a `Cursor` object and invoke its `execute()` method to run SQL commands:

```python
c = conn.cursor()

# Create table
c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')

# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")

```

Most of the time your SQL operations will rely on values drawn from Python variables. Don't build your query with Python's string operations, as that is insecure; it leaves your program open to an SQL injection attack.

Reach instead for the DB-API's parameter substitution. Drop a `?` anywhere a value belongs, then hand a tuple of values as the cursor's `execute()` method's second argument. (A different placeholder, such as `%s` or `:1`, may be used by other database modules.) For instance:

```python
# Never do this -- insecure!
symbol = 'IBM'
c.execute("... where symbol = '%s'" % symbol)

# Do this instead
t = (symbol,)
c.execute('select * from stocks where symbol=?', t)

# Larger example
for t in (('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
         ):
    c.execute('insert into stocks values (?,?,?,?,?)', t)

```

To retrieve data after a SELECT statement runs, you have a few choices: treat the cursor as an iterator, call the cursor's `fetchone()` method to grab a single matching row, or call `fetchall()` to get a list of all the matching rows.

The following example shows the iterator approach:

```python
>>> c = conn.cursor()
>>> c.execute('select * from stocks order by price')
>>> for row in c:
...    print row
...
(u'2006-01-05', u'BUY', u'RHAT', 100, 35.140000000000001)
(u'2006-03-28', u'BUY', u'IBM', 1000, 45.0)
(u'2006-04-06', u'SELL', u'IBM', 500, 53.0)
(u'2006-04-05', u'BUY', u'MSOFT', 1000, 72.0)
>>>

```

To learn more about the SQL dialect that SQLite supports, see [https://www.sqlite.org](https://www.sqlite.org).

See also

[https://www.pysqlite.org](https://www.pysqlite.org)

The pysqlite web page.

[Subject index](INDEX.md) · [Previous source section](the-hashlib-package.md) · [Next source section](sqlite-query-language-and-type-adapters.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
