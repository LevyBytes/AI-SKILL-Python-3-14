# importlib.machinery`importlib.machinery` – Importers and path hooks

*class *importlib.machinery.PathFinder

A [Finder](https://docs.python.org/3.14/glossary.html#term-finder) for [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) and package `__path__` attributes. This class implements the `importlib.abc.MetaPathFinder` ABC.

The class exposes only class methods, removing any requirement to instantiate it.

 *classmethod *find_spec(*fullname*, *path=None*, *target=None*)

A class method that tries to locate a [spec](https://docs.python.org/3.14/glossary.html#term-module-spec) for the module named by *fullname*, looking on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) or, when supplied, on *path*. As each searched path entry is considered, [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) is consulted. When the lookup yields a non-false object, that object becomes the [path entry finder](https://docs.python.org/3.14/glossary.html#term-path-entry-finder) used to hunt for the requested module. When `sys.path_importer_cache` holds no such entry, [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) is scanned for a finder matching the path entry; any finder discovered is recorded in `sys.path_importer_cache` and then asked about the module. Should no finder turn up at all, `None` is stored in the cache and also handed back.

Added in version 3.4.

Changed in version 3.5: Where the current working directory – standing in as an empty string – has become invalid, `None` comes back yet nothing gets cached into [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache).

 *classmethod *invalidate_caches()

Invokes `importlib.abc.PathEntryFinder.invalidate_caches()` for every finder held in [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) that supplies that method. Any `sys.path_importer_cache` entries whose value is `None` are otherwise removed.

Changed in version 3.7: Entries of `None` in [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache) are deleted.

Changed in version 3.4: Invokes objects in [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks), passing the current working directory in place of `''` (that is, the empty string).

[Subject index](INDEX.md) · [Previous](importlib-machinery-windowsregistryfinder-class.md) · [Continue](file-finder-discovery-and-cache-invalidation.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
