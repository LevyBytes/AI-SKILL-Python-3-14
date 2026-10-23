# sqlite3 - Default adapters and converters (deprecated)

### Default adapters and converters (deprecated)

Note

As of Python 3.12 the default adapters and converters are deprecated. Use the Adapter and converter recipes instead and adjust them to fit your situation.

These deprecated default adapters and converters comprise:

- An adapter turning [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) objects into [`strings`](https://docs.python.org/3.14/library/stdtypes.html#str) following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

- An adapter turning [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) objects into strings following ISO 8601 format.

- A converter mapping declared "date" types onto [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) objects.

- A converter mapping declared "timestamp" types onto [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) objects. Fractional parts will be truncated to 6 digits (microsecond precision).

Note

The default "timestamp" converter disregards UTC offsets stored in the database and invariably hands back a naive [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) object. To hold onto UTC offsets within timestamps, either keep converters turned off, or register an offset-aware converter through `register_converter()`.

Deprecated since version 3.12.

[Subject index](INDEX.md) · [Previous](sqlite-and-python-types.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
