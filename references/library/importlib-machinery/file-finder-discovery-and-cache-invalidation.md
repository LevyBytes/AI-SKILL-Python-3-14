# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.FileFinder(*path*, **loader_details*)

A concrete implementation of `importlib.abc.PathEntryFinder` that keeps a cache of results obtained from the file system.

The *path* argument names the directory this finder is responsible for searching.

The *loader_details* argument is some number of 2-item tuples, each pairing a loader with a sequence of the file suffixes that loader handles. Each loader is expected to be a callable taking two arguments: the module's name and the path to the file that was located.

When needed, the finder caches the directory's contents, issuing stat calls on every module search to confirm the cache has not gone stale. Since detecting staleness depends on the resolution of the operating system's file-system state data, a race condition can arise between looking up a module, writing a new file, and then looking up the module that the new file would supply. When those steps complete inside one stat-call resolution interval, the module lookup fails. So that this does not occur, remember to call `importlib.invalidate_caches()` whenever you build a module on the fly.

Added in version 3.3.

 path

The path the finder will search in.

 find_spec(*fullname*, *target=None*)

Attempt to find the spec to handle *fullname* within `path`.

Added in version 3.4.

 invalidate_caches()

Clear out the internal cache.

 *classmethod *path_hook(**loader_details*)

A class method handing back a closure meant for use on [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks). The closure produces a `FileFinder` instance, taking the path argument passed to the closure directly while using *loader_details* indirectly.

When the closure's argument does not name an existing directory, [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is raised.

[Subject index](INDEX.md) · [Previous](importlib-machinery-pathfinder-class.md) · [Continue](source-file-loader-contract.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
