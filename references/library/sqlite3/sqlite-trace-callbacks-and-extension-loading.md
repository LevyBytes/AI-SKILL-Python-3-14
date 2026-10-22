# sqlite3.Connection: `set_trace_callback()`, `enable_load_extension()`, `load_extension()`

set_trace_callback(*trace_callback*)

Register [callable](https://docs.python.org/3.14/glossary.html#term-callable) *trace_callback* so that it fires for every SQL statement that the SQLite backend genuinely runs.

The callback receives a single argument: the statement (as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) currently being run. Whatever the callback returns is discarded. Be aware that the backend executes more than just the statements handed to the `Cursor.execute()` methods. Additional origins include the transaction management of the `sqlite3` module and the firing of triggers declared in the present database.

Supplying `None` for *trace_callback* turns the trace callback off.

Note

Exceptions thrown inside the trace callback do not propagate. To aid development and debugging, turn on `enable_callback_tracebacks()` so tracebacks from exceptions thrown in the trace callback get printed.

Added in version 3.3.

Changed in version 3.13: Supplying *trace_callback* by keyword is deprecated. The parameter is slated to become positional-only in Python 3.15.

 enable_load_extension(*enabled*, */*)

Allow the SQLite engine to pull in SQLite extensions from shared libraries when *enabled* is `True`; otherwise, block the loading of SQLite extensions. SQLite extensions are able to add new functions, aggregates, or entirely new virtual table implementations. A widely known one is the fulltext-search extension shipped alongside SQLite.

Note

By default the `sqlite3` module is built without loadable extension support, since certain platforms (macOS in particular) ship SQLite libraries compiled without that capability. To obtain loadable extension support, you have to hand the [`--enable-loadable-sqlite-extensions`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-loadable-sqlite-extensions) option to **configure**.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `sqlite3.enable_load_extension` with arguments `connection`, `enabled`.

Added in version 3.2.

Changed in version 3.10: Added the `sqlite3.enable_load_extension` auditing event.

```python
con.enable_load_extension(True)

# Load the fulltext search extension
con.execute("select load_extension('./fts3.so')")

# alternatively you can load the extension using an API call:
# con.load_extension("./fts3.so")

# disable extension loading again
con.enable_load_extension(False)

# example from SQLite wiki
con.execute("CREATE VIRTUAL TABLE recipe USING fts3(name, ingredients)")
con.executescript("""
    INSERT INTO recipe (name, ingredients) VALUES('broccoli stew', 'broccoli peppers cheese tomatoes');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin stew', 'pumpkin onions garlic celery');
    INSERT INTO recipe (name, ingredients) VALUES('broccoli pie', 'broccoli cheese onions flour');
    INSERT INTO recipe (name, ingredients) VALUES('pumpkin pie', 'pumpkin sugar flour butter');
    """)
for row in con.execute("SELECT rowid, name, ingredients FROM recipe WHERE name MATCH 'pie'"):
    print(row)

```

 load_extension(*path*, */*, ***, *entrypoint=None*)

Pull in a SQLite extension out of a shared library. Turn extension loading on with `enable_load_extension()` ahead of invoking this method.

Parameters:

- **path** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The path to the SQLite extension.

- **entrypoint** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)* | **None*) – Entry point name. When `None` (the default), SQLite picks its own entry point name; consult the SQLite docs [Loading an Extension](https://www.sqlite.org/loadext.html#loading_an_extension) for the details.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `sqlite3.load_extension` with arguments `connection`, `path`.

Added in version 3.2.

Changed in version 3.10: Added the `sqlite3.load_extension` auditing event.

Changed in version 3.12: Added the *entrypoint* parameter.

[Subject index](INDEX.md) · [Previous](sqlite-collations-interrupt-and-progress-handlers.md) · [Continue](sqlite3-connection-iterdump.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
