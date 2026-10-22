# What's New In Python 3.6 / Porting to Python 3.6 / Changes in the C API

### Changes in the C API

- Rather than the system `malloc()`, the [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) allocator family now relies on the [pymalloc allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc). Code that calls `PyMem_Malloc()` while not holding the GIL can now crash. To check how your application uses memory allocators, set the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable to `debug`. See [bpo-26249](https://bugs.python.org/issue?@action=redirect&bpo=26249).

- When flushing buffered data fails, [`Py_Exit()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_Exit) (along with the main interpreter) now forces the exit status to 120. See [bpo-5319](https://bugs.python.org/issue?@action=redirect&bpo=5319).

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](bytecode-migration-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-6.md)
