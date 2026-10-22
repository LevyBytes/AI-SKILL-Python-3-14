# Python 3.11.0 alpha 1 / library / sqlite3

[bpo-44491](https://bugs.python.org/issue?@action=redirect&bpo=44491): The [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) authorizer callback can now be cleared by handing [`None`](https://docs.python.org/3.14/library/constants.html#None) to [`set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer). Erlend E. Aasland wrote the patch.

[bpo-43853](https://bugs.python.org/issue?@action=redirect&bpo=43853): String handling improved for [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) user-defined functions and aggregates:

  - Strings carrying embedded null characters may now be passed to UDFs

  - Failed conversions now properly raise [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError)

Patch by Erlend E. Aasland.

[bpo-44304](https://bugs.python.org/issue?@action=redirect&bpo=44304): Fixed a crash inside the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module that arose when the garbage collector cleared `sqlite.Statement` objects. Pablo Galindo wrote the patch.

[bpo-16379](https://bugs.python.org/issue?@action=redirect&bpo=16379): The SQLite error code and its name are now attached to [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) exceptions. Aviv Palivoda, Daniel Shahaf, and Erlend E. Aasland authored the change.

[bpo-44859](https://bugs.python.org/issue?@action=redirect&bpo=44859): Strengthened the error handling inside [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) to surface more precise exceptions.

  - [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) now surfaces in place of [`sqlite3.Warning`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Warning) whenever there is not enough memory to encode a statement into UTF-8 within `Connection.__call__()` and `Cursor.execute()`.

  - `UnicodEncodeError` now surfaces in place of [`sqlite3.Warning`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Warning) whenever the statement carries surrogate characters within `Connection.__call__()` and `Cursor.execute()`.

  - [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) now surfaces in place of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) for a non-string script argument within `Cursor.executescript()`.

  - [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) now surfaces for a script holding the null character rather than chopping it off within `Cursor.executescript()`.

  - Properly deal with exceptions thrown while computing the boolean value of whatever the progress handler returns.

  - Add a great many tests spanning various corner cases.

[bpo-44822](https://bugs.python.org/issue?@action=redirect&bpo=44822): When [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) user-defined functions and aggregators hand back [`strings`](https://docs.python.org/3.14/library/stdtypes.html#str) that embed NUL characters, those strings are no longer cut short. Erlend E. Aasland authored this patch.

[bpo-27334](https://bugs.python.org/issue?@action=redirect&bpo=27334): Should a commit fail, the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) context manager now issues a rollback, thereby freeing the database lock. Luca Citi and Erlend E. Aasland wrote the patch.

[bpo-44688](https://bugs.python.org/issue?@action=redirect&bpo=44688): [`sqlite3.Connection.create_collation()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_collation) will now take collation names that are non-ASCII. Erlend E. Aasland authored this patch.

[bpo-42862](https://bugs.python.org/issue?@action=redirect&bpo=42862): The connection statement cache of [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) is now backed by [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache). For a minor speedup, the cache’s default size grew from 100 to 128. Erlend E. Aasland authored the change.

[bpo-40956](https://bugs.python.org/issue?@action=redirect&bpo=40956): Argument Clinic is now applied within [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3). Erlend E. Aasland authored these patches.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
