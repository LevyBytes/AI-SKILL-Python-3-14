# sqlite3: `sqlite3.Row`

### Row objects

 *class *sqlite3.Row

A `Row` instance works as a heavily optimized `row_factory` for `Connection` objects. It allows iteration, equality comparison, [`len()`](https://docs.python.org/3.14/library/functions.html#len), and [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) lookups by both column name and index.

A pair of `Row` objects are equal when their column names and values both match.

See How to create and use row factories for more details.

[Subject index](INDEX.md) · [Previous](cursor-objects.md) · [Continue](sqlite3-row-keys.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
