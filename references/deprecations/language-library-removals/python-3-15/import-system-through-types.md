# Language and standard library pending removal in 3.15: import system; ctypes; http.server; importlib; pathlib; platform; sysconfig; threading; types

## Pending removal in Python 3.15

### Pending removal in Python 3.15

- The import system:

  - It is deprecated to set [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) on a module without also setting [`__spec__.cached`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.cached). Come Python 3.15, neither the import system nor the standard library will set or consult `__cached__` any longer. ([gh-97879](https://github.com/python/cpython/issues/97879))

  - It is deprecated to set [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) on a module without also setting [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent). Come Python 3.15, neither the import system nor the standard library will set or consult `__package__` any longer. ([gh-97879](https://github.com/python/cpython/issues/97879))

- [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes):

  - Since Python 3.13, the undocumented `ctypes.SetPointerType()` function has carried a deprecation.

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server):

  - Deprecated since Python 3.13, the obsolete and seldom-used [`CGIHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.CGIHTTPRequestHandler) has no direct successor. For wiring a web server to a request handler, *anything* beats CGI.

  - Since Python 3.13, the `--cgi` flag on the **python -m http.server** command-line interface has been deprecated.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - `load_module()` method: use `exec_module()` instead.

- [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib):

  - Deprecated since Python 3.13, [`PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) should give way to [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) for spotting reserved paths on Windows.

- [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform):

  - Deprecated since Python 3.13, [`java_ver()`](https://docs.python.org/3.14/library/platform.html#platform.java_ver) serves only Jython support, exposes a confusing API, and is largely untested.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - Deprecated since Python 3.12, the *check_home* argument of [`sysconfig.is_python_build()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.is_python_build).

- [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading):

  - Come Python 3.15, [`RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) accepts no arguments. Supplying any has been deprecated since Python 3.14: the Python version rejects all arguments, whereas the C version accepts any count of positional or keyword arguments and silently ignores each one.

- [`types`](https://docs.python.org/3.14/library/types.html#module-types):

  - [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType): [**PEP 626**](https://peps.python.org/pep-0626/) deprecated access to [`co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab) back in 3.10, with removal originally targeted for 3.12, yet it only received a genuine [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) in 3.12. Removal may land in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866).)

[Subject index](INDEX.md) · [Previous source section](../python-3-14/itertools-through-urllib.md) · [Next source section](typing-wave-zipimport.md)
