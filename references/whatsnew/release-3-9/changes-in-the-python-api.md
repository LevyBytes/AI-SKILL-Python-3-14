# What's New In Python 3.9 / Changes in the Python API — __future__, asyncio-eventloop, bz2, codecs, errno, ftplib, importlib, ipaddress, logging, pathlib, select, socket, venv

### Changes in the Python API

- [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) and [`importlib.util.resolve_name()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.resolve_name) now raise [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) in place of the [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) raised before. Code that catches the precise exception type while still supporting Python 3.9 alongside earlier versions must catch both, with `except (ImportError, ValueError):`.

- The [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) activation scripts no longer treat `__VENV_PROMPT__` being set to `""` as a special case.

- The [`select.epoll.unregister()`](https://docs.python.org/3.14/library/select.html#select.epoll.unregister) method now stops ignoring the [`EBADF`](https://docs.python.org/3.14/library/errno.html#errno.EBADF) error. (Contributed by Victor Stinner in [bpo-39239](https://bugs.python.org/issue?@action=redirect&bpo=39239).)

- The *compresslevel* parameter of [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) is now keyword-only, given that the *buffering* parameter was removed. (Contributed by Victor Stinner in [bpo-39357](https://bugs.python.org/issue?@action=redirect&bpo=39357).)

- The AST for subscription was simplified. A simple index is represented by its own value, while extended slices appear as tuples. `Index(value)` returns a `value` itself, and `ExtSlice(slices)` returns `Tuple(slices, Load())`. (Contributed by Serhiy Storchaka in [bpo-34822](https://bugs.python.org/issue?@action=redirect&bpo=34822).)

- The [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) module now disregards the [`PYTHONCASEOK`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCASEOK) environment variable whenever the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) or [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line options are in effect.

- An *encoding* parameter was added to the [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) and [`ftplib.FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) classes as a keyword-only parameter, and its default moved from Latin-1 to UTF-8 to conform with [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

- [`asyncio.loop.shutdown_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor) was added to [`AbstractEventLoop`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.AbstractEventLoop), so alternative event loops deriving from it ought to define this method too. (Contributed by Kyle Stanley in [bpo-34037](https://bugs.python.org/issue?@action=redirect&bpo=34037).)

- The constant values of future flags within the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) module were updated so that they no longer collide with compiler flags. Earlier, `PyCF_ALLOW_TOP_LEVEL_AWAIT` collided with `CO_FUTURE_DIVISION`. (Contributed by Batuhan Taskaya in [bpo-39562](https://bugs.python.org/issue?@action=redirect&bpo=39562))

- `array('u')` now relies on `wchar_t` for its C type rather than `Py_UNICODE`. Behavior is unaffected by this change, since `Py_UNICODE` has been an alias of `wchar_t` ever since Python 3.3. (Contributed by Inada Naoki in [bpo-34538](https://bugs.python.org/issue?@action=redirect&bpo=34538).)

- The [`logging.getLogger()`](https://docs.python.org/3.14/library/logging.html#logging.getLogger) API now hands back the root logger when given the name `'root'`, where formerly it returned a non-root logger named `'root'`. That may matter when user code deliberately wants a non-root logger named `'root'`, or builds a logger via `logging.getLogger(__name__)` inside some top-level module named `'root.py'`. (Contributed by Vinay Sajip in [bpo-37742](https://bugs.python.org/issue?@action=redirect&bpo=37742).)

- Division handling on [`PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) now hands back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) rather than raising a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when given anything other than an instance of `str` or `PurePath`. That makes it possible to build compatible classes which do not derive from the listed types. (Contributed by Roger Aiudi in [bpo-34775](https://bugs.python.org/issue?@action=redirect&bpo=34775)).

- From Python 3.9.5 onward, the [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module stops accepting any leading zeros within IPv4 address strings. Such leading zeros are ambiguous, and some libraries read them as octal notation. As an illustration, the legacy function [`socket.inet_aton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_aton) handles leading zeros as octal notatation. The glibc implementation of the modern [`inet_pton()`](https://docs.python.org/3.14/library/socket.html#socket.inet_pton) rejects any leading zeros. (Contributed by Christian Heimes in [bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384)).

- [`codecs.lookup()`](https://docs.python.org/3.14/library/codecs.html#codecs.lookup) now normalizes an encoding name in the same fashion as [`encodings.normalize_encoding()`](https://docs.python.org/3.14/library/codecs.html#encodings.normalize_encoding), the difference being that `codecs.lookup()` additionally lowercases the name. As an example, the `"latex+latin1"` encoding name is now normalized into `"latex_latin1"`. (Contributed by Jordon Xu in [bpo-37751](https://bugs.python.org/issue?@action=redirect&bpo=37751).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-9.md) · [Next source section](porting-to-python-3-9-changes-in-the-c-api.md) · [Release/subject declaration](summary-release-highlights.md)
