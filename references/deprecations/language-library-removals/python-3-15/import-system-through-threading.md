# Language and standard library pending removal in 3.15: import system; ctypes; http.server; importlib; pathlib; platform; sysconfig; threading

### Deprecations

### Pending removal in Python 3.15

- The import system:

  - Assigning [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) on a module without also assigning [`__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached) is now deprecated. Beginning with Python 3.15, neither the import machinery nor the standard library will set or consult `__cached__`. ([gh-97879](https://github.com/python/cpython/issues/97879))

  - Assigning [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) on a module without also assigning [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent) is now deprecated. Beginning with Python 3.15, neither the import machinery nor the standard library will set or consult `__package__`. ([gh-97879](https://github.com/python/cpython/issues/97879))

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - Since Python 3.13, the undocumented `ctypes.SetPointerType()` function has carried a deprecation.

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - Deprecated since Python 3.13, the seldom-used and outdated [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) has no drop-in successor. For wiring a web server to a request handler, *anything* beats CGI.

  - Deprecated since Python 3.13, the `--cgi` option of the **python -m http.server** command-line interface.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - `load_module()` method: use `exec_module()` instead.

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - Deprecated since Python 3.13, [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) should give way to [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) when checking for reserved paths on Windows.

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - Deprecated since Python 3.13, [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) serves only Jython, carries a puzzling API, and is mostly untested.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - Since Python 3.12, the *check_home* argument of [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build) has carried a deprecation.

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading):

  - Starting in Python 3.15, [`RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) accepts no arguments. Supplying any has been deprecated since Python 3.14: the pure-Python version rejects all arguments, whereas the C version tolerates any count of positional or keyword arguments and simply discards each one.

[Subject index](INDEX.md) · [Next source section](types-through-zipimport.md)
