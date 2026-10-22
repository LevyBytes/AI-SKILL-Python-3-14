# dbm — **flag** (*str*) –

**flag** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) –
  - `'r'` (default): read-only access to a database that already exists.

  - `'w'`: read-and-write access to a database that already exists.

  - `'c'`: read-and-write access, building the database when it is not yet present.

  - `'n'`: always start a fresh, empty database with read-and-write access.

- **mode** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The file’s Unix access mode (octal `0o666` by default), applied solely at the moment a database must be created.

Changed in version 3.11: *file* accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

What `open()` hands back provides the core behavior of mutable [mappings](https://docs.python.org/3.14/glossary.html#term-mapping): you can store, fetch, and remove keys together with their values, and iteration, the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator, and the `keys()`, `get()`, `setdefault()` and `clear()` methods are all on hand. Note that `keys()` hands back a list rather than a view object, and `setdefault()` expects two arguments.

Keys and values are invariably held as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). Consequently, any strings supplied get silently encoded with the default encoding prior to storage.

These objects can additionally serve inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, which closes them for you once you’re finished.

Changed in version 3.2: every `dbm` backend now offers the `get()` and `setdefault()` methods.

Changed in version 3.4: the objects `open()` returns gained built-in support for the context management protocol.

Changed in version 3.8: removing a key from a read-only database now raises a database-module-specific exception rather than [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

Changed in version 3.13: every `dbm` backend now offers the `clear()` method.

In the example below, a handful of hostnames are paired with a title, after which the database contents are printed:

```python
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.

```

See also

Module [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve)

Persistence module which stores non-string data.

Each of the submodules gets its own treatment in the sections that follow.

[Subject index](INDEX.md) · [Previous](dbm-sqlite3-to-dbm-open.md) · [Continue](../dbm-sqlite3/dbm-sqlite3-open.md) · [Owning module, declaration or section: dbm](dbm-sqlite3-to-dbm-open.md)
