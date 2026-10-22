# What’s New In Python 3.12 / Deprecated — argparse, ast, asyncio, asyncio-eventloop, calendar, collections.abc, datetime, email, email.utils, importlib

### Deprecated

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse): On `argparse.BooleanOptionalAction`, the *type*, *choices*, and *metavar* parameters are now deprecated, slated for removal in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248).)

- [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast): The `ast` features listed below, deprecated in documentation ever since Python 3.8, will now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) at runtime whenever they are accessed or used, and they are due for removal in Python 3.14:

  - `ast.Num`

  - `ast.Str`

  - `ast.Bytes`

  - `ast.NameConstant`

  - `ast.Ellipsis`

Reach for [`ast.Constant`](https://docs.python.org/3.14/library/ast.html#ast.Constant) in their place. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953).)

- [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio):

  - The child watcher classes `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher` are now deprecated, with removal planned for Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` are now deprecated, with removal planned for Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597).)

  - When no current event loop is set and the default event loop policy elects to create one, its [`get_event_loop()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop) method now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): The `calendar.January` and `calendar.February` constants are now deprecated, superseded by [`calendar.JANUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.JANUARY) and [`calendar.FEBRUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.FEBRUARY). (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

- [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc): [`collections.abc.ByteString`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.ByteString) has been deprecated.

To check at runtime whether `obj` implements the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects), use `isinstance(obj, collections.abc.Buffer)`. Within type annotations, reach for [`Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) or spell out a union covering the types your code handles (e.g., `bytes | bytearray | memoryview`).

The original aim for `ByteString` was an abstract class acting as a supertype over both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray). Yet because the ABC carried no methods, learning that an object was a `ByteString` instance never conveyed anything useful about it. Further widespread buffer types such as [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) were likewise never recognized as subtypes of `ByteString`, whether at runtime or by static type checkers.

Refer to [**PEP 688**](https://peps.python.org/pep-0688/#current-options) for fuller detail. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896).)

- [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime): The [`utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow) and [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp) methods on [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) are now deprecated and will go away in a later version. To express UTC datetimes, switch to timezone-aware objects instead: call [`now()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.now) and [`fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromtimestamp) respectively, passing the *tz* parameter as [`datetime.UTC`](https://docs.python.org/3.14/library/datetime.html#datetime.UTC). (Contributed by Paul Ganssle in [gh-103857](https://github.com/python/cpython/issues/103857).)

- [`email`](https://docs.python.org/3.14/library/email.html#module-email): Within [`email.utils.localtime()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.localtime), the *isdst* parameter has been deprecated. (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346).)

- [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc): The classes below are now deprecated and set for removal in Python 3.14:

  - `importlib.abc.ResourceReader`

  - `importlib.abc.Traversable`

  -

`importlib.abc.TraversableResources`

Turn to the [`importlib.resources.abc`](https://docs.python.org/3.14/library/importlib.resources.abc.html#module-importlib.resources.abc) classes in their stead:

  - [`importlib.resources.abc.Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable)

  - [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources)

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

- [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools): Support for copy, deepcopy, and pickle operations is now deprecated; it was undocumented, inefficient, historically buggy, and inconsistent. Removing it in 3.14 will cut code volume and maintenance burden substantially. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588).)

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): On Linux, the BSDs, and the other non-macOS POSIX platforms where `'fork'` currently serves as the default, Python 3.14 will switch the default `multiprocessing` start method to a safer choice ([gh-84559](https://github.com/python/cpython/issues/84559)). A runtime warning about it was judged too disruptive, given that the bulk of code should not care. To state plainly that your code *requires* `'fork'`, reach for the [`get_context()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.get_context) or [`set_start_method()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_start_method) APIs. Refer to [contexts and start methods](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods).

- [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil): Both `pkgutil.find_loader()` and `pkgutil.get_loader()` are now deprecated and bound for removal in Python 3.14; turn to [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec) instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850).)

- [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty): This module carries two undocumented functions, `master_open()` and `slave_open()`, deprecated since Python 2 yet only given a proper [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) in 3.12. They go away in 3.14. (Contributed by Soumendra Ganguly and Gregory P. Smith in [gh-85984](https://github.com/python/cpython/issues/85984).)

- [`os`](https://docs.python.org/3.14/library/os.html#module-os):

  - On Windows, the `st_ctime` fields handed back by [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) and [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) are now deprecated. A later release will have them hold the most recent metadata change time, matching other platforms. For the moment they keep reporting the creation time, which the new `st_birthtime` field exposes as well. (Contributed by Steve Dower in [gh-99726](https://github.com/python/cpython/issues/99726).)

  - When it can tell that the call came from a multithreaded process, [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) on POSIX platforms can now raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Doing so has always carried a basic incompatibility with the POSIX platform, even where such code *appeared* to function. The warning exists to raise awareness, since the problems hit by code that does this keep growing more common. Consult the `os.fork()` documentation for further detail, plus [this discussion on fork being incompatible with threads](https://discuss.python.org/t/concerns-regarding-deprecation-of-fork-with-alive-threads/33555) covering *why* this longstanding platform compatibility problem is now being surfaced to developers.

When this warning shows up because of [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) or [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) usage, the remedy is to pick a different `multiprocessing` start method, for instance `"spawn"` or `"forkserver"`.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): On [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree), the *onerror* argument is now deprecated; reach for *onexc* instead. (Contributed by Irit Katriel in [gh-102828](https://github.com/python/cpython/issues/102828).)

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3):

  - The [default adapters and converters](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-default-converters) are now deprecated. In their place, draw on the [Adapter and converter recipes](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-adapter-converter-recipes) and adjust them to fit your needs. (Contributed by Erlend E. Aasland in [gh-90016](https://github.com/python/cpython/issues/90016).)

  - Within [`execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute), a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) now fires whenever [named placeholders](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-placeholders) appear alongside parameters handed in as a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) rather than as a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). Beginning with Python 3.14, mixing named placeholders and sequence-supplied parameters will instead raise a [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). Erlend E. Aasland contributed this in [gh-101698](https://github.com/python/cpython/issues/101698).

-

[Subject index](INDEX.md) · [Previous source section](demos-and-tools.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](archive-filters-and-library-deprecations.md)
