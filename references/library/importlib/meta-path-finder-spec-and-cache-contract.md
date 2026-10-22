# importlib: `find_spec()`, `invalidate_caches()`

find_spec(*fullname*, *path*, *target=None*)

An abstract method that locates a [spec](https://docs.python.org/3.14/glossary.html#term-module-spec) for the named module. For a top-level import, *path* comes through as `None`. Otherwise the call represents a lookup for a subpackage or module, with *path* carrying the [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) value from the parent package. Where no spec turns up, `None` comes back. The `target`, when supplied, is a module object the finder can lean on to better guess which spec to hand back. For building concrete `MetaPathFinders`, `importlib.util.spec_from_loader()` can come in handy.

Added in version 3.4.

 invalidate_caches()

An optional method that, once invoked, ought to clear whatever internal cache the finder keeps. `importlib.invalidate_caches()` calls it while clearing the caches of every finder sitting on [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path).

Changed in version 3.4: Returns `None` when called instead of [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented).

[Subject index](INDEX.md) · [Previous](importlib-abc-metapathfinder-class.md) · [Continue](path-entry-finder-contract.md) · [Owning module, declaration or section: importlib.abc.MetaPathFinder](importlib-abc-metapathfinder-class.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
