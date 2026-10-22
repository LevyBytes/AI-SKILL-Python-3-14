# Python 3.13.0 alpha 1 / library / exceptions

[gh-105002](https://github.com/python/cpython/issues/105002): Correct a wrong result out of the `PurePath.relative_to()` method while trying to walk a "`..`" segment in *other* under *walk_up*. From now on a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception gets raised here.

[gh-107913](https://github.com/python/cpython/issues/107913): Corrected potential losses of the `errno` and `winerror` values in [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exceptions when the cleanup code cleared or altered them ahead of building the exception object.

[gh-80480](https://github.com/python/cpython/issues/80480): Now emits a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) for the `'u'` type code of [`array`](https://docs.python.org/3.14/library/array.html#module-array), which the docs have marked deprecated since Python 3.3.

[gh-108682](https://github.com/python/cpython/issues/108682): Enum: raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) whenever `super().__new__()` gets called out of a custom `__new__`.

[gh-102541](https://github.com/python/cpython/issues/102541): Let `pydoc.doc()` trap a bad module [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) whenever the output stream is something other than `None`.

[gh-110590](https://github.com/python/cpython/issues/110590): Corrected a defect in `_sre.compile()` whereby [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) ended up replaced by [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) whenever the *code* argument arrived as a list containing non-ints.

[gh-110036](https://github.com/python/cpython/issues/110036): Under Windows, the multiprocessing `Popen.terminate()` now intercepts [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError) and retrieves the process exit code. Should the process keep running, the `PermissionError` is re-raised. Otherwise the process exited as anticipated and its exit code gets stored. Victor Stinner contributed this patch.

[gh-70303](https://github.com/python/cpython/issues/70303): Issue a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) out of [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) whenever the supplied pattern closes with "`**`". Within a later Python release, such patterns will match files together with directories. Append a trailing slash to restrict matching to directories alone.

[gh-106684](https://github.com/python/cpython/issues/106684): Emit [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) whenever an [`asyncio.StreamWriter`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter) is left unclosed, which otherwise causes memory leaks. Kumar Aditya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
