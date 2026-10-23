# What's New In Python 3.3 / New APIs - importlib, sys

### New APIs

A major payoff here is that the inner workings making the import statement function are now on display. Each of the importers that used to stay implicit is therefore wholly surfaced within the [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) package.

The abstract base classes living in [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) gained additions that cleanly separate [meta path finders](https://docs.python.org/3.14/glossary.html#term-meta-path-finder) from [path entry finders](https://docs.python.org/3.14/glossary.html#term-path-entry-finder), via the new [`importlib.abc.MetaPathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder) and [`importlib.abc.PathEntryFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder) classes respectively. The former ABC named `importlib.abc.Finder` survives purely for backwards-compatibility and mandates no methods at all.

Among the finders, [`importlib.machinery.FileFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.FileFinder) reveals the routine that hunts for a module’s source and bytecode files. That class formerly sat implicitly inside [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks).

On the loader side, the freshly introduced abstract base class [`importlib.abc.FileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.FileLoader) aids in authoring a loader that treats the file system as where a module’s code is kept. You may now directly employ the loader handling source files ([`importlib.machinery.SourceFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.SourceFileLoader)), the one for sourceless bytecode files ([`importlib.machinery.SourcelessFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.SourcelessFileLoader)), and the one for extension modules ([`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ExtensionFileLoader)).

[`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) gained `name` and `path` attributes, populated whenever pertinent data exists to supply. A failed import’s message will likewise report the module’s complete name from now on rather than merely the trailing portion of it.

Whenever needed to tidy up retained state, the [`importlib.invalidate_caches()`](https://docs.python.org/3.14/library/importlib.html#importlib.invalidate_caches) function now invokes the identically named method across every finder held in [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache).

[Subject index](INDEX.md) · [Previous source section](using-importlib-as-the-implementation-of-import.md) · [Next source section](visible-changes.md) · [Release/subject declaration](summary-release-highlights.md)
