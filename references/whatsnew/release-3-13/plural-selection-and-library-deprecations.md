# What's New In Python 3.13 / New Deprecations — glob, http.server, mimetypes, os.path, pathlib, platform, pydoc, re, sqlite3

> Whatsnew reference. Wording rephrased; identifiers held byte-for-byte.

Within the `gettext` module, supplying non-integer numbers to functions and methods that select a plural form is now deprecated, and this holds true even when no matching translation exists. (Contributed by Serhiy Storchaka in [gh-88434](https://github.com/python/cpython/issues/88434).)

- [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob):

  - The undocumented helpers `glob0()` and `glob1()` are now deprecated. Switch to [`glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob), handing a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) that names the root directory through the *root_dir* parameter. (Contributed by Barney Gale in [gh-117337](https://github.com/python/cpython/issues/117337).)

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) is now deprecated and is slated for removal in Python 3.15. Serving CGI through separate processes fell out of fashion ages ago. The implementation was stale, no longer maintained, and seldom invoked. There is a strong likelihood of both security holes and correctness problems. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096).)

  - The `--cgi` flag of the **python -m http.server** command-line interface is now deprecated as well, scheduled for removal in Python 3.15. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  - Passing file paths to [`guess_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_type) is now [Soft-deprecate](https://docs.python.org/3.14/glossary.html#term-soft-deprecated)d; reach for [`guess_file_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.guess_file_type) in that situation. (Contributed by Serhiy Storchaka in [gh-66543](https://github.com/python/cpython/issues/66543).)

- [`re`](https://docs.python.org/3.14/library/re.html#module-re):

  - Handing the optional *maxsplit*, *count*, or *flags* values positionally to the module-level [`split()`](https://docs.python.org/3.14/library/re.html#re.split), [`sub()`](https://docs.python.org/3.14/library/re.html#re.sub), and [`subn()`](https://docs.python.org/3.14/library/re.html#re.subn) functions is now deprecated. A later Python release will make these arguments [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter). (Contributed by Serhiy Storchaka in [gh-56166](https://github.com/python/cpython/issues/56166).)

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) is now deprecated and will go away in Python 3.15. To spot reserved paths on Windows, call [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved). (Contributed by Barney Gale in [gh-88569](https://github.com/python/cpython/issues/88569).)

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) is now deprecated and is set for removal in Python 3.15. Its sole purpose serves Jython, the interface confuses callers, and it has barely any test coverage. (Contributed by Nikita Sobolev in [gh-116349](https://github.com/python/cpython/issues/116349).)

- [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc):

  - The undocumented `ispackage()` helper is now deprecated. (Contributed by Zackery Spytz in [gh-64020](https://github.com/python/cpython/issues/64020).)

- [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3):

  - Supplying more than a single positional argument to the [`connect()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.connect) function or to the [`Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) constructor is now deprecated. Those leftover parameters turn keyword-only as of Python 3.15. (Contributed by Erlend E. Aasland in [gh-107948](https://github.com/python/cpython/issues/107948).)

  - Supplying the name, the argument count, and the callable as keyword arguments to [`Connection.create_function()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_function) and [`Connection.create_aggregate()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.create_aggregate) is now deprecated. Those parameters turn positional-only as of Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278).)

  - Supplying the callback callable as a keyword to the [`set_authorizer()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_authorizer), [`set_progress_handler()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_progress_handler), and [`set_trace_callback()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.set_trace_callback) [`Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) methods is now deprecated. Each callback callable turns positional-only as of Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278).)

-

[Subject index](INDEX.md) · [Next source section](legacy-encoding-and-typing-deprecations.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](new-deprecations.md) · [Preceding release/subject continuation](new-deprecations.md)
