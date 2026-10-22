# sqlite3 — How to write adaptable objects

#### How to write adaptable objects

Imagine a `Point` class standing for a pair of coordinates, `x` and `y`, within a Cartesian coordinate system. The pair of coordinates will live in the database as a text string, with a semicolon dividing the two coordinates. You can build this by adding a `__conform__(self, protocol)` method that returns the adapted value. Whatever gets passed as *protocol* will carry the type `PrepareProtocol`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.x};{self.y}"

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(4.0, -3.2),))
print(cur.fetchone()[0])
con.close()

```

[Subject index](INDEX.md) · [Previous](how-to-adapt-custom-python-types-to-sqlite-values.md) · [Continue](how-to-register-adapter-callables.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
