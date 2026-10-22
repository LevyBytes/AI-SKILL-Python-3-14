# sqlite3.Connection: `setconfig()`, `serialize()`, `deserialize()`

setconfig(*op*, *enable=True*, */*)

Set a boolean connection configuration option.

Parameters:

- **op** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – A SQLITE_DBCONFIG code.

- **enable** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – `True` to switch the configuration option on (default); `False` to switch it off.

Added in version 3.12.

 serialize(***, *name='main'*)

Serialize a database into a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. With an ordinary on-disk database file, the serialization amounts to nothing more than a copy of that disk file. When the database is held in memory or is a “temp” one, what you get back matches exactly the bytes that backing that database up to disk would write.

Parameters:

**name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The database name to be serialized. Defaults to `"main"`.

Return type:

[bytes](https://docs.python.org/3.14/library/stdtypes.html#bytes)

Note

You can only use this method when the underlying SQLite library exposes the serialize API.

Added in version 3.11.

 deserialize(*data*, */*, ***, *name='main'*)

Deserialize a `serialized` database into a `Connection`. The effect of this method is that the database connection detaches from database *name* and reopens *name* as an in-memory database built from the serialization held in *data*.

Parameters:

- **data** ([*bytes*](https://docs.python.org/3.14/library/stdtypes.html#bytes)) – A serialized database.

- **name** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The database name to deserialize into. Defaults to `"main"`.

Raises:

- **OperationalError** – If, at that moment, the database connection has a read transaction or a backup operation underway.

- **DatabaseError** – If *data* does not contain a valid SQLite database.

- [**OverflowError**](https://docs.python.org/3.14/library/exceptions.html#OverflowError) – If [`len(data)`](https://docs.python.org/3.14/library/functions.html#len) is larger than `2**63 - 1`.

Note

You can only use this method when the underlying SQLite library exposes the deserialize API.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](sqlite3-connection-getlimit-to-sqlite3-connection-getconfig.md) · [Continue](connection-configuration-and-transactions.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Connection](sqlite3-connection-class.md) · [Owning module, declaration or section: Connection objects](sqlite3-connection-class.md)
