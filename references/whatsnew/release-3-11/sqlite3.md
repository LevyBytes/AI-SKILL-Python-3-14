# What's New In Python 3.11 / sqlite3 - sqlite3

### sqlite3

- The authorizer can now be turned off by handing [`None`](https://docs.python.org/3.14/library/constants.html#None) to [`set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer). (Contributed by Erlend E. Aasland in [bpo-44491](https://bugs.python.org/issue?@action=redirect&bpo=44491).)

- A collation name passed to [`create_collation()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_collation) may now hold any Unicode character. When a collation name carries invalid characters, [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) is now raised in place of [`sqlite3.ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). (Contributed by Erlend E. Aasland in [bpo-44688](https://bugs.python.org/issue?@action=redirect&bpo=44688).)

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) exceptions now expose the SQLite extended error code via [`sqlite_errorcode`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Error.sqlite_errorcode) and the SQLite error name via [`sqlite_errorname`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Error.sqlite_errorname). (Contributed by Aviv Palivoda, Daniel Shahaf, and Erlend E. Aasland in [bpo-16379](https://bugs.python.org/issue?@action=redirect&bpo=16379) and [bpo-24139](https://bugs.python.org/issue?@action=redirect&bpo=24139).)

- [`setlimit()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.setlimit) and [`getlimit()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.getlimit) were added to [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) for reading and writing SQLite limits per connection. (Contributed by Erlend E. Aasland in [bpo-45243](https://bugs.python.org/issue?@action=redirect&bpo=45243).)

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) now derives [`sqlite3.threadsafety`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.threadsafety) from whichever default threading mode the bundled SQLite library was compiled with. (Contributed by Erlend E. Aasland in [bpo-45613](https://bugs.python.org/issue?@action=redirect&bpo=45613).)

-

When callback tracebacks are switched on, [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) C callbacks have moved over to unraisable exceptions. To sharpen the debug workflow, an [`unraisable hook handler`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) may now be registered. (Contributed by Erlend E. Aasland in [bpo-45828](https://bugs.python.org/issue?@action=redirect&bpo=45828).)

- A fetch that crosses a rollback no longer triggers [`InterfaceError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.InterfaceError); the underlying SQLite library is left to deal with such situations instead. (Contributed by Erlend E. Aasland in [bpo-44092](https://bugs.python.org/issue?@action=redirect&bpo=44092).)

- For serializing plus deserializing databases, [`serialize()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.serialize) and [`deserialize()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.deserialize) were added onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection). (Contributed by Erlend E. Aasland in [bpo-41930](https://bugs.python.org/issue?@action=redirect&bpo=41930).)

- To build aggregate window functions, [`create_window_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_window_function) was added onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection). (Contributed by Erlend E. Aasland in [bpo-34916](https://bugs.python.org/issue?@action=redirect&bpo=34916).)

- [`blobopen()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.blobopen) was added onto [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection). Incremental I/O against blobs is made possible by [`sqlite3.Blob`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Blob). (Contributed by Aviv Palivoda and Erlend E. Aasland in [bpo-24905](https://bugs.python.org/issue?@action=redirect&bpo=24905).)

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](string.md)
