# What’s New In Python 3.12 / Pending removal in Python 3.14 - argparse, ast, asyncio, asyncio-eventloop, email, email.utils, importlib, importlib.resources.abc, itertools

### Pending removal in Python 3.14

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse): For `argparse.BooleanOptionalAction`, the *type*, *choices*, and *metavar* parameters now carry deprecations and get dropped in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

- [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast): The items below, which the docs have flagged as deprecated ever since Python 3.8, will now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) at runtime upon access or use, and Python 3.14 drops them:

  - `ast.Num`

  - `ast.Str`

  - `ast.Bytes`

  - `ast.NameConstant`

  - `ast.Ellipsis`

Switch to [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) in their place. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - The child-watcher types `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher` now carry deprecations and get dropped in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` now carry deprecations and get dropped in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - On the default event loop policy, the [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) method now fires a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) whenever no current event loop exists and it opts to spin one up. (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

- [`email`](https://docs.python.org/3.14/library/email.html#module-email): A deprecation now covers the *isdst* parameter within [`email.utils.localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime). (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

- [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) classes now deprecated:

  - `importlib.abc.ResourceReader`

  - `importlib.abc.Traversable`

  - `importlib.abc.TraversableResources`

Reach for the [`importlib.resources.abc`](https://docs.python.org/3.14/library/importlib.resources.abc.html#module-importlib.resources.abc) classes in their place:

  - [`importlib.resources.abc.Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable)

  - [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources)

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

- [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) carried undocumented, inefficient, historically buggy, and inconsistent handling of copy, deepcopy, and pickle operations. The 3.14 release strips this out, yielding a sizable cut in code volume and upkeep. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): On Linux, the BSDs, and the remaining non-macOS POSIX systems where `'fork'` currently reigns as the default, the default start method moves to something safer ([gh-84559](https://github.com/python/cpython/issues/84559)). Bolting a runtime warning onto this was judged overly disruptive, given that most code is not expected to be affected. Lean on the [`get_context()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_context) or [`set_start_method()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_start_method) APIs to spell out when your code *requires* `'fork'`. Refer to [Contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib): For [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to) and [`relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to), handing in extra arguments now carries a deprecation.

- [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil): A [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is now raised by `pkgutil.find_loader()` and `pkgutil.get_loader()`; reach for [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec) in their place. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

- [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty):

  - `master_open()`: reach for [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

  - `slave_open()`: reach for [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty).

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3):

  - `version` and `version_info`.

  - [`execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute) and [`executemany()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.executemany) whenever [named placeholders](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-placeholders) appear and *parameters* arrives as a sequence rather than a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

- [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib): `urllib.parse.Quoter` now carries a deprecation, since it was never meant as a public API. (Contributed by Gregory P. Smith in [gh-88168](https://github.com/python/cpython/issues/88168).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-13.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-15.md)
