# What's New In Python 3.13 / Pending removal in Python 3.15 — ctypes, http.server, importlib, os.path, pathlib, platform, sysconfig, threading, types

### Pending removal in Python 3.15

- The import system:

  - Assigning [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) on a module without also assigning [`__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached) is now deprecated. Come Python 3.15, neither the import system nor the standard library will set or consult `__cached__` any longer. ([gh-97879](https://github.com/python/cpython/issues/97879))

  - Assigning [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) on a module without also assigning [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent) is now deprecated. Come Python 3.15, neither the import system nor the standard library will set or consult `__package__` any longer. ([gh-97879](https://github.com/python/cpython/issues/97879))

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - The undocumented `ctypes.SetPointerType()` function has carried a deprecation since Python 3.13.

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - The dated, scarcely used [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) has carried a deprecation since Python 3.13. Nothing serves as a one-to-one substitute. *Anything* beats CGI for wiring a web server to a request handler.

  - The `--cgi` flag of the **python -m http.server** command-line interface has carried a deprecation since Python 3.13.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - `load_module()` method: switch to `exec_module()`.

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) has carried a deprecation since Python 3.13. Call [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) to spot reserved paths on Windows.

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) has carried a deprecation since Python 3.13. Its sole purpose serves Jython, the interface confuses callers, and it has barely any test coverage.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - For [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build), the *check_home* argument has carried a deprecation since Python 3.12.

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading):

  - [`RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) accepts no arguments starting in Python 3.15. Handing it any argument has carried a deprecation since Python 3.14, because the Python implementation forbids arguments while the C implementation swallows any count of positional or keyword arguments and ignores each one.

- [`types`](https://docs.python.org/3.14/library/types.html#module-types):

  - [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType): Reading [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) became deprecated under [**PEP 626**](https://peps.python.org/pep-0626/) starting at 3.10, with removal intended for 3.12, yet a genuine [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) only arrived in 3.12. Removal may land in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

-

[`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - The undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (for example, `Point = NamedTuple("Point", x=int, y=int)`) has carried a deprecation since Python 3.13. Pick either the class-based form or the functional form.

  - With the functional form of [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict)s, leaving the *fields* parameter unset (`TD = TypedDict("TD")`) or supplying `None` (`TD = TypedDict("TD", None)`) has carried a deprecation since Python 3.13. Write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})` to build a TypedDict holding no field.

  - The [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) decorator function has carried a deprecation since Python 3.13. Despite eight years living in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, no significant type checker has ever adopted it.

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - The [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods of the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) and [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes have carried a deprecation since Python 3.13.

- [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport):

  - [`load_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.load_module) has carried a deprecation since Python 3.10. Switch to [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module). (Contributed by Jiahao Li in [gh-125746](https://github.com/python/cpython/issues/125746).)

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](pending-removal-in-python-3-16.md)
