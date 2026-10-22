# sqlite3 — How to register adapter callables

#### How to register adapter callables

Alternatively, you can build a function that turns the Python object into an SQLite-compatible type. You then register that function via `register_adapter()`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return f"{point.x};{point.y}"

sqlite3.register_adapter(Point, adapt_point)

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(1.0, 2.5),))
print(cur.fetchone()[0])
con.close()

```

[Subject index](INDEX.md) · [Previous](how-to-write-adaptable-objects.md) · [Continue](how-to-convert-sqlite-values-to-custom-python-types.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
