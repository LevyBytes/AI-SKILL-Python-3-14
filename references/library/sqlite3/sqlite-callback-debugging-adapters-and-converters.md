# sqlite3: `sqlite3.enable_callback_tracebacks()`, `sqlite3.register_adapter()`, `sqlite3.register_converter()`

sqlite3.enable_callback_tracebacks(*flag*, */*)

Turns callback tracebacks on or off. Out of the box you receive no tracebacks from user-defined functions, aggregates, converters, authorizer callbacks and so on. To debug those, call this function passing *flag* as `True`. From then on, callback tracebacks land on [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). Pass `False` to switch the feature back off.

Note

Errors arising in user-defined function callbacks get logged as unraisable exceptions. Lean on an [`unraisable hook handler`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) to introspect a callback that failed.

 sqlite3.register_adapter(*type*, *adapter*, */*)

Registers an *adapter* [callable](https://docs.python.org/3.14/glossary.html#term-callable) that adapts the Python type *type* over to an SQLite type. The adapter receives one Python object of type *type* as its single argument and has to give back a value of some type SQLite understands natively.

 sqlite3.register_converter(*typename*, *converter*, */*)

Registers the *converter* [callable](https://docs.python.org/3.14/glossary.html#term-callable) that turns SQLite objects of type *typename* into a Python object of a particular type. Every SQLite value of type *typename* triggers the converter; it receives a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object and is expected to give back an object of whatever Python type you want. See the *detect_types* parameter of `connect()` for an account of how type detection operates.

Note: matching between *typename* and the type name in your query is done case-insensitively.

[Subject index](INDEX.md) · [Previous](sqlite3-connect-to-sqlite3-complete-statement.md) · [Continue](sqlite-transaction-and-version-constants.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: Module functions](sqlite3-connect-to-sqlite3-complete-statement.md)
