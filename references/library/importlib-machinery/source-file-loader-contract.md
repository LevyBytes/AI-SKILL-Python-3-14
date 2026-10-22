# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.SourceFileLoader(*fullname*, *path*)

A concrete implementation of `importlib.abc.SourceLoader` that derives from `importlib.abc.FileLoader` and supplies concrete versions of additional methods.

Added in version 3.3.

 name

The name of the module that this loader will handle.

 path

The path to the source file.

 is_package(*fullname*)

Return `True` if `path` appears to be for a package.

 path_stats(*path*)

Concrete implementation of `importlib.abc.SourceLoader.path_stats()`.

 set_data(*path*, *data*)

Concrete implementation of `importlib.abc.SourceLoader.set_data()`.

 load_module(*name=None*)

A concrete implementation of `importlib.abc.Loader.load_module()` in which naming the module to be loaded is optional.

Deprecated since version 3.6, scheduled for removal in 3.15: turn to `importlib.abc.Loader.exec_module()` from now on.

[Subject index](INDEX.md) · [Previous](file-finder-discovery-and-cache-invalidation.md) · [Continue](bytecode-only-file-loader-contract.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
