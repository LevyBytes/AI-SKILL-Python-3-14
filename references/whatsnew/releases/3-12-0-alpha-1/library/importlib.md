# Python 3.12.0 alpha 1 / library / importlib

[gh-97850](https://github.com/python/cpython/issues/97850): Drops the deprecated `importlib.util.set_loader()` and `importlib.util.module_for_loader()` from [`importlib.util`](https://docs.python.org/3.14/library/importlib.html#module-importlib.util).

[gh-93461](https://github.com/python/cpython/issues/93461): [`importlib.invalidate_caches()`](https://docs.python.org/3.14/library/importlib.html#importlib.invalidate_caches) now removes any [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) entry whose name is a relative path. That fixes a caching problem arising when a process switches its current working directory.

`FileFinder` stops inserting a dot into the path, so for instance `/egg/./spam` becomes `/egg/spam`.

[gh-94619](https://github.com/python/cpython/issues/94619): The long-deprecated `module_repr()` is dropped from [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib).

[bpo-38693](https://bugs.python.org/issue?@action=redirect&bpo=38693): Internally, [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) has switched to f-strings in place of `str.format`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
