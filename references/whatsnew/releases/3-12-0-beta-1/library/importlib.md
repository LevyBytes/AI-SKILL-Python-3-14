# Python 3.12.0 beta 1 / library / importlib

[gh-97850](https://github.com/python/cpython/issues/97850): Mark `pkgutil.find_loader()` and `pkgutil.get_loader()` as deprecated, steering callers toward [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec).

[gh-98040](https://github.com/python/cpython/issues/98040): Strip out further deprecated importlib APIs: `find_loader()`, `find_module()`, `importlib.abc.Finder`, `pkgutil.ImpImporter`, `pkgutil.ImpLoader`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
