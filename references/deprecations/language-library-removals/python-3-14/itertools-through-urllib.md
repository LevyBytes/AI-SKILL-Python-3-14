# Language and standard library pending removal in 3.14: itertools; multiprocessing; pathlib; pkgutil; pty; sqlite3; urllib

- [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) carried undocumented, inefficient, historically buggy, and inconsistent handling of copy, deepcopy, and pickle operations. Dropping it in 3.14 yields a meaningful cut in code volume and upkeep. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): On Linux, the BSDs, and other non-macOS POSIX systems where `'fork'` is presently the default, the default start method will switch to a safer one ([gh-84559](https://github.com/python/cpython/issues/84559)). A runtime warning was judged too disruptive to add here, since most code is not expected to be affected. When your code genuinely *requires* `'fork'`, declare that explicitly through the [`get_context()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_context) or [`set_start_method()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_start_method) APIs. See [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib): For [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to) and [`relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to), supplying extra arguments is now deprecated.

- [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil): Both `pkgutil.find_loader()` and `pkgutil.get_loader()` now raise [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning); reach for [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec) instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

- [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty):

  - `master_open()`: use [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

  - `slave_open()`: use [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3):

  - `version` and `version_info`.

  - [`execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute) and [`executemany()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.executemany) when [named placeholders](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-placeholders) appear and *parameters* arrives as a sequence rather than a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

- [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib): `urllib.parse.Quoter` is deprecated, since it was never meant to serve as a public API. (Contributed by Gregory P. Smith in [gh-88168](https://github.com/python/cpython/issues/88168).)

[Subject index](INDEX.md) · [Previous source section](argparse-through-importlib-abc-deprecated-classes.md) · [Next source section](../python-3-15/import-system-through-types.md)
