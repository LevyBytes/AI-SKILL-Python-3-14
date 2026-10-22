# sqlite3.Row: `keys()`

keys()

Hand back a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of column names as [`strings`](https://docs.python.org/3.14/library/stdtypes.html#str). Right after a query, this corresponds to the first element of every tuple within `Cursor.description`.

Changed in version 3.5: Added support of slicing.

[Subject index](INDEX.md) · [Previous](sqlite3-row-class.md) · [Continue](sqlite3-blob-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Row](sqlite3-row-class.md) · [Owning module, declaration or section: Row objects](sqlite3-row-class.md)
