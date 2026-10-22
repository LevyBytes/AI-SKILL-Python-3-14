# Language and standard library pending removal in 3.16: functools; logging; mimetypes; shutil; symtable; sys; sysconfig; tarfile

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools):

  - Since Python 3.14, invoking the Python implementation of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) with *function* or *sequence* passed as keyword arguments has been deprecated.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging):

Passing the *strm* argument to custom logging handlers is deprecated and set for removal in Python 3.16. Build handlers with the *stream* argument in its place. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  - For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), a valid extension is empty or begins with a ?.?. Extensions lacking a dot are deprecated and, in Python 3.16, will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil):

  - Deprecated since Python 3.14, the `ExecError` exception has gone unused by every `shutil` function since Python 3.4 and is now simply an alias for [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable):

  - Since Python 3.14, the [`Class.get_methods`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) method has carried a deprecation.

- [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - Deprecated since Python 3.13, the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function should be replaced by the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - Deprecated since Python 3.14, the `sysconfig.expand_makefile_vars()` function should give way to the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths).

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - Since Python 3.13, the undocumented and unused `TarFile.tarfile` attribute has carried a deprecation.

- [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools):

  - Passing *function* or *sequence* as keyword arguments to the Python implementation of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) has been deprecated since Python 3.14.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging):

Custom logging handlers that rely on the *strm* argument are deprecated, with removal scheduled for Python 3.16. When defining handlers, supply the *stream* argument in its place. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032).)

- [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes):

  - For [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes.add_type), valid extensions either begin with a ‘.’ or are empty. Undotted extensions are deprecated and, in Python 3.16, will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223).)

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil):

  - Deprecated since Python 3.14, the `ExecError` exception has gone unused by any `shutil` function since Python 3.4 and is now an alias of [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

- [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable):

  - Since Python 3.14, the [`Class.get_methods`](https://docs.python.org/3.14/library/symtable.html#symtable.Class.get_methods) method has been deprecated.

- [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - Deprecated since Python 3.13, the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function should be replaced by the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable.

- [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig):

  - Deprecated since Python 3.14, the `sysconfig.expand_makefile_vars()` function should give way to the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_paths).

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - Since Python 3.13, the undocumented and unused `TarFile.tarfile` attribute has been deprecated.

[Subject index](INDEX.md) · [Previous source section](import-system-through-builtins.md) · [Next source section](../python-3-17/collections-abc-typing.md)
