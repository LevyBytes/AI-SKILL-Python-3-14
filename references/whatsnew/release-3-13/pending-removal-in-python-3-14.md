# What's New In Python 3.13 / Pending removal in Python 3.14 — argparse, ast, asyncio, asyncio-eventloop, email, email.utils, importlib, importlib.resources.abc, itertools

### Pending removal in Python 3.14

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse): On `argparse.BooleanOptionalAction`, the *type*, *choices*, and *metavar* parameters are now deprecated, with removal in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

- [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast): Documentation has flagged the items below as deprecated ever since Python 3.8; they now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) while running whenever accessed or used, and removal lands in Python 3.14:

  - `ast.Num`

  - `ast.Str`

  - `ast.Bytes`

  - `ast.NameConstant`

  - `ast.Ellipsis`

Reach for [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) in their place. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - These child watcher classes -- `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher` -- are now deprecated, with removal in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - The functions `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` are now deprecated, with removal in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - On the default event loop policy, the [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) method now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) whenever no current event loop is set and it chooses to build one. (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

- [`email`](https://docs.python.org/3.14/library/email.html#module-email): The *isdst* parameter of [`email.utils.localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime) is now deprecated. (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

- [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) deprecated classes:

  - `importlib.abc.ResourceReader`

  - `importlib.abc.Traversable`

  - `importlib.abc.TraversableResources`

Adopt the [`importlib.resources.abc`](https://docs.python.org/3.14/library/importlib.resources.abc.html#module-importlib.resources.abc) classes in their place:

  - [`importlib.resources.abc.Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable)

  - [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources)

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

- [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) carried undocumented, slow, long-buggy, and uneven handling of copy, deepcopy, and pickle. That support disappears in 3.14, sharply cutting code size and upkeep. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): On Linux, the BSDs, and the other non-macOS POSIX platforms where `'fork'` reigns today, the default start method shifts to a safer choice ([gh-84559](https://github.com/python/cpython/issues/84559)). Emitting a runtime warning over this seemed overly disruptive, since most code should not be affected. Call the [`get_context()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_context) or [`set_start_method()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_start_method) APIs to state outright wherever your code *requires* `'fork'`. Consult [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib): For [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to) and [`relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to), handing in extra arguments is now deprecated.

- [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil): Calls to `pkgutil.find_loader()` and `pkgutil.get_loader()` now trigger a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning); switch to [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec). (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

- [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty):

  - `master_open()`: call [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

  - `slave_open()`: call [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3):

  - `version` and `version_info`.

  - [`execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute) and [`executemany()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.executemany) when [named placeholders](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-placeholders) appear and *parameters* arrives as a sequence rather than a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

- [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib): `urllib.parse.Quoter` is now deprecated, as it was never meant as a public API. (Contributed by Gregory P. Smith in [gh-88168](https://github.com/python/cpython/issues/88168).)

[Subject index](INDEX.md) · [Previous source section](legacy-encoding-and-typing-deprecations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-15.md)
