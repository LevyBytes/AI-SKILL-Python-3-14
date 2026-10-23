# What’s New In Python 3.12 / importlib - importlib

### importlib

- A range of cleanups long deprecated within [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) are now finished:

  - Mentions of, plus support for, `module_repr()` are gone. (Contributed by Barry Warsaw in [gh-97850](https://github.com/python/cpython/issues/97850).)

  - `importlib.util.set_package`, `importlib.util.set_loader` and `importlib.util.module_for_loader` are every one removed. (Contributed by Brett Cannon and Nikita Sobolev in [gh-65961](https://github.com/python/cpython/issues/65961) and [gh-97850](https://github.com/python/cpython/issues/97850).)

  - The `find_loader()` and `find_module()` APIs are no longer supported. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

  - `importlib.abc.Finder`, `pkgutil.ImpImporter`, and `pkgutil.ImpLoader` are gone. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

[Subject index](INDEX.md) · [Previous source section](hashlib.md) · [Next source section](imp.md) · [Release/subject declaration](summary-release-highlights.md)
