# sqlite3 — How to create and use row factories

### How to create and use row factories

Out of the box, `sqlite3` hands you every row in the form of a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). Should a `tuple` not fit what you are after, reach for either the `sqlite3.Row` class or a `row_factory` of your own.

Although `row_factory` appears as an attribute on both the `Cursor` and the `Connection`, the advised approach is to assign `Connection.row_factory` so that every cursor spawned from that connection shares one row factory.

`Row` lets you reach columns either by index or by case-insensitive name, adding very little memory cost or slowdown compared with a `tuple`. To put `Row` to work as a row factory, set it on the `row_factory` attribute:

```pycon
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = sqlite3.Row

```

From this point, queries hand back `Row` objects:

```pycon
>>> res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
>>> row = res.fetchone()
>>> row.keys()
['name', 'radius']
>>> row[0]         # Access by index.
'Earth'
>>> row["name"]    # Access by name.
'Earth'
>>> row["RADIUS"]  # Column names are case-insensitive.
6378
>>> con.close()

```

Note

As the example above shows, the `SELECT` statement may leave out the `FROM` clause. When it does, SQLite yields one row whose columns come from the supplied expressions — literals, say — under whatever aliases you provide via `expr AS alias`.

It is possible to write your own `row_factory` that delivers each row as a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) in which column names are keyed to their values:

```python
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

```

With that in place, a query hands back a `dict` rather than a `tuple`:

```pycon
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = dict_factory
>>> for row in con.execute("SELECT 1 AS a, 2 AS b"):
...     print(row)
{'a': 1, 'b': 2}
>>> con.close()

```

Here is a row factory that yields a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple):

```python
from collections import namedtuple

def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)

```

Here is how you would put `namedtuple_factory()` to use:

```pycon
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = namedtuple_factory
>>> cur = con.execute("SELECT 1 AS a, 2 AS b")
>>> row = cur.fetchone()
>>> row
Row(a=1, b=2)
>>> row[0]  # Indexed access.
1
>>> row.b   # Attribute access.
2
>>> con.close()

```

A handful of tweaks lets you rework the recipe above so it builds a [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) — or any class you define — in place of a [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple).

[Subject index](INDEX.md) · [Previous](how-to-work-with-sqlite-uris.md) · [Continue](how-to-handle-non-utf-8-text-encodings.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
