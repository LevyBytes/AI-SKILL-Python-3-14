# Python 3.11.0 alpha 1 / library / exceptions

[bpo-44471](https://bugs.python.org/issue?@action=redirect&bpo=44471): A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), rather than an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError), is now produced by [`contextlib.ExitStack.enter_context()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.ExitStack.enter_context) and [`contextlib.AsyncExitStack.enter_async_context()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AsyncExitStack.enter_async_context) when given objects that fail to implement the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) or [asynchronous context manager](https://docs.python.org/3.14/glossary.html#term-asynchronous-context-manager) protocols respectively.

[bpo-37880](https://bugs.python.org/issue?@action=redirect&bpo=37880): The argparse actions store_const and append_const now each get a default of `None` whenever the `const` kwarg is omitted. That formerly raised a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[bpo-43650](https://bugs.python.org/issue?@action=redirect&bpo=43650): Fix [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) in [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive) which fails inside `shutil._unpack_zipfile()` on large files. Patch by Igor Bolshakov.

[bpo-44839](https://bugs.python.org/issue?@action=redirect&bpo=44839): A [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) thrown by user-defined functions will now yield a `MemoryError` inside [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3). An [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) will now turn into [`DataError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.DataError). These situations formerly produced an [`OperationalError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.OperationalError).

[bpo-42854](https://bugs.python.org/issue?@action=redirect&bpo=42854): Cleared a defect in the `_ssl` module that raised [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) while calling `_ssl._SSLSocket.write()` and `_ssl._SSLSocket.read()` for a large `len` parameter. Pablo Galindo wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
