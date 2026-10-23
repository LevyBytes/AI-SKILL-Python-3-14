# Persistence

# Persistence

### Data Persistence

The modules covered in this chapter make it possible to keep Python data on disk in a persistent form. With the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) modules, many Python data types can be serialized into a byte stream and later reconstructed back into objects from those bytes. The assorted DBM-related modules back a family of hash-based file formats, each of which keeps a mapping from strings to other strings.

Here are the modules covered in this chapter:

- [`pickle` - Python object serialization](https://docs.python.org/3.14/library/pickle.html)
  - [Relationship to other Python modules](https://docs.python.org/3.14/library/pickle.html#relationship-to-other-python-modules)
    - [Comparison with `marshal`](https://docs.python.org/3.14/library/pickle.html#comparison-with-marshal)
    - [Comparison with `json`](https://docs.python.org/3.14/library/pickle.html#comparison-with-json)

  - [Data stream format](https://docs.python.org/3.14/library/pickle.html#data-stream-format)
  - [Module Interface](https://docs.python.org/3.14/library/pickle.html#module-interface)
  - [What can be pickled and unpickled?](https://docs.python.org/3.14/library/pickle.html#what-can-be-pickled-and-unpickled)
  - [Pickling Class Instances](https://docs.python.org/3.14/library/pickle.html#pickling-class-instances)
    - [Persistence of External Objects](https://docs.python.org/3.14/library/pickle.html#persistence-of-external-objects)
    - [Dispatch Tables](https://docs.python.org/3.14/library/pickle.html#dispatch-tables)
    - [Handling Stateful Objects](https://docs.python.org/3.14/library/pickle.html#handling-stateful-objects)

  - [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3.14/library/pickle.html#custom-reduction-for-types-functions-and-other-objects)
  - [Out-of-band Buffers](https://docs.python.org/3.14/library/pickle.html#out-of-band-buffers)
    - [Provider API](https://docs.python.org/3.14/library/pickle.html#provider-api)
    - [Consumer API](https://docs.python.org/3.14/library/pickle.html#consumer-api)
    - [Example](https://docs.python.org/3.14/library/pickle.html#example)

  - [Restricting Globals](https://docs.python.org/3.14/library/pickle.html#restricting-globals)
  - [Performance](https://docs.python.org/3.14/library/pickle.html#performance)
  - [Examples](https://docs.python.org/3.14/library/pickle.html#examples)
  - [Command-line interface](https://docs.python.org/3.14/library/pickle.html#command-line-interface)

- [`copyreg` - Register `pickle` support functions](https://docs.python.org/3.14/library/copyreg.html)
  - [Example](https://docs.python.org/3.14/library/copyreg.html#example)

- [`shelve` - Python object persistence](https://docs.python.org/3.14/library/shelve.html)
  - [Restrictions](https://docs.python.org/3.14/library/shelve.html#restrictions)
  - [Example](https://docs.python.org/3.14/library/shelve.html#example)

- [`marshal` - Internal Python object serialization](https://docs.python.org/3.14/library/marshal.html)
- [`dbm` - Interfaces to Unix “databases”](https://docs.python.org/3.14/library/dbm.html)
  - [`dbm.sqlite3` - SQLite backend for dbm](https://docs.python.org/3.14/library/dbm.html#module-dbm.sqlite3)
  - [`dbm.gnu` - GNU database manager](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu)
  - [`dbm.ndbm` - New Database Manager](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm)
  - [`dbm.dumb` - Portable DBM implementation](https://docs.python.org/3.14/library/dbm.html#module-dbm.dumb)

- [`sqlite3` - DB-API 2.0 interface for SQLite databases](https://docs.python.org/3.14/library/sqlite3.html)
  - [Tutorial](https://docs.python.org/3.14/library/sqlite3.html#tutorial)
  - [Reference](https://docs.python.org/3.14/library/sqlite3.html#reference)
    - [Module functions](https://docs.python.org/3.14/library/sqlite3.html#module-functions)
    - [Module constants](https://docs.python.org/3.14/library/sqlite3.html#module-constants)
    - [Connection objects](https://docs.python.org/3.14/library/sqlite3.html#connection-objects)
    - [Cursor objects](https://docs.python.org/3.14/library/sqlite3.html#cursor-objects)
    - [Row objects](https://docs.python.org/3.14/library/sqlite3.html#row-objects)
    - [Blob objects](https://docs.python.org/3.14/library/sqlite3.html#blob-objects)
    - [PrepareProtocol objects](https://docs.python.org/3.14/library/sqlite3.html#prepareprotocol-objects)
    - [Exceptions](https://docs.python.org/3.14/library/sqlite3.html#exceptions)
    - [SQLite and Python types](https://docs.python.org/3.14/library/sqlite3.html#sqlite-and-python-types)
    - [Default adapters and converters (deprecated)](https://docs.python.org/3.14/library/sqlite3.html#default-adapters-and-converters-deprecated)
    - [Command-line interface](https://docs.python.org/3.14/library/sqlite3.html#command-line-interface)

  - [How-to guides](https://docs.python.org/3.14/library/sqlite3.html#how-to-guides)
    - [How to use placeholders to bind values in SQL queries](https://docs.python.org/3.14/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
    - [How to adapt custom Python types to SQLite values](https://docs.python.org/3.14/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values)
      - [How to write adaptable objects](https://docs.python.org/3.14/library/sqlite3.html#how-to-write-adaptable-objects)
      - [How to register adapter callables](https://docs.python.org/3.14/library/sqlite3.html#how-to-register-adapter-callables)

    - [How to convert SQLite values to custom Python types](https://docs.python.org/3.14/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types)
    - [Adapter and converter recipes](https://docs.python.org/3.14/library/sqlite3.html#adapter-and-converter-recipes)
    - [How to use connection shortcut methods](https://docs.python.org/3.14/library/sqlite3.html#how-to-use-connection-shortcut-methods)
    - [How to use the connection context manager](https://docs.python.org/3.14/library/sqlite3.html#how-to-use-the-connection-context-manager)
    - [How to work with SQLite URIs](https://docs.python.org/3.14/library/sqlite3.html#how-to-work-with-sqlite-uris)
    - [How to create and use row factories](https://docs.python.org/3.14/library/sqlite3.html#how-to-create-and-use-row-factories)
    - [How to handle non-UTF-8 text encodings](https://docs.python.org/3.14/library/sqlite3.html#how-to-handle-non-utf-8-text-encodings)

  - [Explanation](https://docs.python.org/3.14/library/sqlite3.html#explanation)
    - [Transaction control](https://docs.python.org/3.14/library/sqlite3.html#transaction-control)
      - [Transaction control via the `autocommit` attribute](https://docs.python.org/3.14/library/sqlite3.html#transaction-control-via-the-autocommit-attribute)
      - [Transaction control via the `isolation_level` attribute](https://docs.python.org/3.14/library/sqlite3.html#transaction-control-via-the-isolation-level-attribute)

[Subject index](INDEX.md)
