# What’s New In Python 3.12 / Pending removal in Python 3.15 — ctypes, http.server, importlib, os.path, pathlib, platform, sysconfig, threading, types

### Pending removal in Python 3.15

- The import system:

  - Assigning [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) on a module without also assigning [`__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached) now carries a deprecation. Come Python 3.15, the import machinery and standard library will neither assign `__cached__` nor consult it. ([gh-97879](https://github.com/python/cpython/issues/97879))

  - Assigning [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) on a module without also assigning [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent) now carries a deprecation. Come Python 3.15, the import machinery and standard library will neither assign `__package__` nor consult it. ([gh-97879](https://github.com/python/cpython/issues/97879))

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - A deprecation has covered the undocumented `ctypes.SetPointerType()` function ever since Python 3.13.

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - The outdated and seldom-touched [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) has carried a deprecation since Python 3.13. There is no drop-in successor. *Anything* beats CGI as the bridge between a web server and a request handler.

  - A deprecation has covered the `--cgi` flag of the **python -m http.server** command-line interface ever since Python 3.13.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - `load_module()` method: reach for `exec_module()` in its place.

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - A deprecation has covered [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) ever since Python 3.13. Reach for [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) to spot reserved paths under Windows.

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - A deprecation has covered [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) ever since Python 3.13. The function serves only Jython support, sports a muddled API, and goes largely untested.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - A deprecation has covered the *check_home* argument of [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build) ever since Python 3.12.

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading):

  - Come Python 3.15, [`RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) will accept no arguments at all. Supplying any has carried a deprecation since Python 3.14: the Python build forbids arguments outright, whereas the C build swallows any count of positional or keyword arguments and disregards every one of them.

- [`types`](https://docs.python.org/3.14/library/types.html#module-types):

  - [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType): Reading [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) was deprecated through [**PEP 626**](https://peps.python.org/pep-0626/) back in 3.10 with removal slated for 3.12, yet a real [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) only landed in 3.12. Could go away in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

-

[`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - The undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (say, `Point = NamedTuple("Point", x=int, y=int)`) has carried a deprecation since Python 3.13. Reach for the class-based form or the functional form in its place.

  - With the functional form of [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)s, neglecting to supply a value for the *fields* parameter (`TD = TypedDict("TD")`) or handing in `None` (`TD = TypedDict("TD", None)`) has carried a deprecation since Python 3.13. Write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})` to build a TypedDict holding zero field.

  - A deprecation has covered the [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) decorator function ever since Python 3.13. Across eight years inside the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, no major type checker has ever picked it up.

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - A deprecation has covered the [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods on the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) and [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes ever since Python 3.13.

- [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport):

  - A deprecation has covered [`load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) ever since Python 3.10. Reach for [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module) in its place. (Contributed by Jiahao Li in [gh-125746](https://github.com/python/cpython/issues/125746).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-16.md)
