# sqlite3 — How to convert SQLite values to custom Python types

### How to convert SQLite values to custom Python types

An adapter handles going *from* custom Python types *to* SQLite values. For the reverse direction, *from* SQLite values *to* custom Python types, we turn to *converters*.

Returning to the `Point` class: we kept the x and y coordinates as strings divided by semicolons inside SQLite.

To begin, we'll write a converter function that takes the string as a parameter and builds a `Point` object out of it.

Note

A [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object is **always** what converter functions receive, regardless of the underlying SQLite data type.

```python
def convert_point(s):
    x, y = map(float, s.split(b";"))
    return Point(x, y)

```

At this point we must let `sqlite3` know when a particular SQLite value should be converted. You arrange this while connecting to a database, by way of the *detect_types* parameter on `connect()`. Three choices are available:

- Implicit: set *detect_types* to `PARSE_DECLTYPES`

- Explicit: set *detect_types* to `PARSE_COLNAMES`

- Both: set *detect_types* to `sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES`. Column names take precedence over declared types.

Below, the example walks through both the implicit and explicit approaches:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def adapt_point(point):
    return f"{point.x};{point.y}"

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)

# Register the adapter and converter
sqlite3.register_adapter(Point, adapt_point)
sqlite3.register_converter("point", convert_point)

# 1) Parse using declared types
p = Point(4.0, -3.2)
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.execute("CREATE TABLE test(p point)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute("SELECT p FROM test")
print("with declared types:", cur.fetchone()[0])
cur.close()
con.close()

# 2) Parse using column names
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.execute("CREATE TABLE test(p)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute('SELECT p AS "p [point]" FROM test')
print("with column names:", cur.fetchone()[0])
cur.close()
con.close()

```

[Subject index](INDEX.md) · [Previous](how-to-register-adapter-callables.md) · [Continue](adapter-and-converter-recipes.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
