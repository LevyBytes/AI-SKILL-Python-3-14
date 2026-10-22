# What's new in Python 3.14 / Pending removal in Python 3.15 — ctypes, http.server, importlib, os.path, pathlib, platform, sysconfig, threading, types

### Pending removal in Python 3.15

- The import system:

  - A deprecation applies when [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) gets set on a module yet [`__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached) does not. As of Python 3.15, the import system and standard library will no longer set or consult `__cached__`. ([gh-97879](https://github.com/python/cpython/issues/97879))

  - A deprecation applies when [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) gets set on a module yet [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent) does not. As of Python 3.15, the import system and standard library will no longer set or consult `__package__`. ([gh-97879](https://github.com/python/cpython/issues/97879))

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - A deprecation has covered the undocumented `ctypes.SetPointerType()` function since Python 3.13.

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - A deprecation has covered the dated and seldom-used [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) since Python 3.13. Nothing replaces it directly. *Anything* beats CGI for wiring a web server to a request handler.

  - The `--cgi` flag on the **python -m http.server** command-line interface has carried a deprecation since Python 3.13.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - `load_module()` method: use `exec_module()` instead.

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - A deprecation has covered [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) since Python 3.13. Spot reserved Windows paths with [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved).

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - A deprecation has covered [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) since Python 3.13. The function matters only for Jython, presents a muddled API, and goes mostly untested.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - A deprecation has covered the *check_home* argument of [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build) since Python 3.12.

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading):

  - As of Python 3.15, [`RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) accepts nothing. Supplying any arguments has carried a deprecation since Python 3.14, because the Python version rejects all arguments while the C version swallows however many positional or keyword arguments you pass, ignoring each one.

- [`types`](https://docs.python.org/3.14/library/types.html#module-types):

  - [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType): Reading [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) was deprecated through [**PEP 626**](https://peps.python.org/pep-0626/) as of 3.10 with removal scheduled for 3.12, yet a real [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) arrived only in 3.12. Removal could come in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

-

[`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - A deprecation has covered the undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (say, `Point = NamedTuple("Point", x=int, y=int)`) since Python 3.13. Pick the class-based form or the functional form instead.

  - With the functional form of [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)s, omitting a value for the *fields* parameter (`TD = TypedDict("TD")`) or handing in `None` (`TD = TypedDict("TD", None)`) has carried a deprecation since Python 3.13. To make a TypedDict carrying zero field, write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

  - A deprecation has covered the [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) decorator function since Python 3.13. Eight years on in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, no leading type checker has yet picked it up.

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - A deprecation has covered the [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods on the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) plus [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes since Python 3.13.

- [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport):

  - A deprecation has covered [`load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) since Python 3.10. Reach for [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module) instead. (Contributed by Jiahao Li in [gh-125746](https://github.com/python/cpython/issues/125746).)

[Subject index](INDEX.md) · [Previous source section](new-deprecations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-16.md)
