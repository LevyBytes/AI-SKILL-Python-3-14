# sqlite3.Connection: `create_function()`, `create_aggregate()`

create_function(*name*, *narg*, *func*, ***, *deterministic=False*)

Create or remove a user-defined SQL function.

Parameters:

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name of the SQL function.

- **narg** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How many arguments the SQL function accepts. A value of `-1` lets it take any number of arguments.

- **func** ([callback](https://docs.python.org/3.14/glossary.html#term-callback) | None) – A [callable](https://docs.python.org/3.14/glossary.html#term-callable) run whenever the SQL function fires. That callable has to return a type SQLite natively supports. Pass `None` to drop an existing SQL function.

- **deterministic** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True`, the created SQL function is flagged as [deterministic](https://sqlite.org/deterministic.html), letting SQLite apply extra optimizations.

Changed in version 3.8: Added the *deterministic* parameter.

Example:

```pycon
>>> import hashlib
>>> def md5sum(t):
...     return hashlib.md5(t).hexdigest()
>>> con = sqlite3.connect(":memory:")
>>> con.create_function("md5", 1, md5sum)
>>> for row in con.execute("SELECT md5(?)", (b"foo",)):
...     print(row)
('acbd18db4cc2f85cedef654fccc4a4d8',)
>>> con.close()

```

Changed in version 3.13: handing *name*, *narg*, and *func* across as keyword arguments is now deprecated; come Python 3.15 these become positional-only.

 create_aggregate(*name*, *n_arg*, *aggregate_class*)

[Subject index](INDEX.md) · [Previous](sqlite3-connection-cursor-to-sqlite3-connection-executescript.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md) · [Required continuation of the source contract](connection-context-and-shortcut-methods.md)
