# importlib: `importlib.abc.PathEntryFinder`, `find_spec()`, `invalidate_caches()`

*class *importlib.abc.PathEntryFinder

An abstract base class that stands for a [path entry finder](https://docs.python.org/3.14/glossary.html#term-path-entry-finder). While it has a certain resemblance to `MetaPathFinder`, `PathEntryFinder` is intended solely for the path-based import subsystem that `importlib.machinery.PathFinder` supplies.

Added in version 3.3.

Changed in version 3.10: No longer a subclass of `Finder`.

 find_spec(*fullname*, *target=None*)

An abstract method that locates a [spec](https://docs.python.org/3.14/glossary.html#term-module-spec) for the named module. The finder confines its search for the module to the single [path entry](https://docs.python.org/3.14/glossary.html#term-path-entry) it has been handed. Where no spec turns up, `None` comes back. The `target`, when supplied, is a module object the finder can lean on to better guess which spec to hand back. For building concrete `PathEntryFinders`, `importlib.util.spec_from_loader()` can come in handy.

Added in version 3.4.

 invalidate_caches()

An optional method that, once invoked, ought to clear whatever internal cache the finder keeps. `importlib.machinery.PathFinder.invalidate_caches()` calls it while clearing the caches of every cached finder.

[Subject index](INDEX.md) · [Previous](meta-path-finder-spec-and-cache-contract.md) · [Continue](importlib-abc-loader-class-to-module-loader.md) · [Owning module, declaration or section: `importlib.abc` ? Abstract base classes related to import](importlib-abc-metapathfinder-class.md)
