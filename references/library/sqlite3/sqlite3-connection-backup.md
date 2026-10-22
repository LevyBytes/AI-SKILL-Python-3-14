# sqlite3.Connection: `backup()`

backup(*target*, ***, *pages=-1*, *progress=None*, *name='main'*, *sleep=0.250*)

Produce a backup of a SQLite database.

Functions even while the database is in use by other clients or by the same connection at the same time.

Parameters:

- **target** (*Connection*) – The database connection to save the backup to.

- **pages** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How many pages to copy per step. When `0` or less, the whole database is copied in one step. Defaults to `-1`.

- **progress** ([callback](https://docs.python.org/3.14/glossary.html#term-callback) | None) – When given a [callable](https://docs.python.org/3.14/glossary.html#term-callable), it gets called with three integer arguments on each backup iteration: the *status* of the last iteration, the *remaining* count of pages yet to copy, and the *total* count of pages. Defaults to `None`.

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Which database to back up. Use either `"main"` (the default) for the main database, `"temp"` for the temporary database, or, for a custom database attached via the `ATTACH DATABASE` SQL statement, that database's name.

- **sleep** ([*float*](https://docs.python.org/3.14/library/functions.html#float)) – How many seconds to pause between consecutive attempts at backing up the leftover pages.

Example 1, copy an existing database into another:

```python
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

src = sqlite3.connect('example.db')
dst = sqlite3.connect('backup.db')
with dst:
    src.backup(dst, pages=1, progress=progress)
dst.close()
src.close()

```

Example 2, copy an existing database into a transient copy:

```python
src = sqlite3.connect('example.db')
dst = sqlite3.connect(':memory:')
src.backup(dst)
dst.close()
src.close()

```

Added in version 3.7.

See also

How to handle non-UTF-8 text encodings

[Subject index](INDEX.md) · [Previous](sqlite3-connection-iterdump.md) · [Continue](sqlite3-connection-getlimit-to-sqlite3-connection-getconfig.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
