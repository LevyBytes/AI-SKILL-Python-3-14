# sqlite3.Connection: `iterdump()`

iterdump(***, *filter=None*)

Return an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) that dumps the database out as SQL source code. Handy for persisting an in-memory database to restore later. Comparable to the `.dump` command found in the **sqlite3** shell.

Parameters:

**filter** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*) – An optional `LIKE` pattern for database objects to dump, e.g. `prefix_%`. When `None` (the default), every database object is included.

Example:

```python
# Convert file example.db to SQL dump file dump.sql
con = sqlite3.connect('example.db')
with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()

```

See also

How to handle non-UTF-8 text encodings

Changed in version 3.13: Added the *filter* parameter.

[Subject index](INDEX.md) · [Previous](sqlite-trace-callbacks-and-extension-loading.md) · [Continue](sqlite3-connection-backup.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
