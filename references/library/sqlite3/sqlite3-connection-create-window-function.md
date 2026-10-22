# sqlite3 — Connection objects — Signature and initial contract

create_window_function(*name*, *num_params*, *aggregate_class*, */*)

Register or delete a user-defined aggregate window function.

Parameters:

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The name under which to register or delete the SQL aggregate window function.

- **num_params** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How many arguments the SQL aggregate window function will accept. A value of `-1` lets it accept an arbitrary count of arguments.

- **aggregate_class** ([class](https://docs.python.org/3.14/glossary.html#term-class) | None) –

A class that must provide the following methods:

  - `step()`: Add a row to the current window.

  - `value()`: Return the current value of the aggregate.

  - `inverse()`: Remove a row from the current window.

  - `finalize()`: Hand back the aggregate's final result as a type that SQLite natively understands.

The count of arguments the `step()` and `value()` methods have to take is governed by *num_params*.

Pass `None` here to delete a SQL aggregate window function that already exists.

Raises:

**NotSupportedError** – When used against a SQLite version earlier than 3.25.0, where aggregate window functions are unsupported.

Added in version 3.11.

Example:

[Subject index](INDEX.md) · [Previous](connection-context-and-shortcut-methods.md) · [Continue](connection-objects-code-example-class-windowsumint.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
