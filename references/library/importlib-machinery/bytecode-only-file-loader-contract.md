# importlib.machinery`importlib.machinery` – Importers and path hooks

*class *importlib.machinery.SourcelessFileLoader(*fullname*, *path*)

A concrete implementation of `importlib.abc.FileLoader` capable of importing bytecode files (that is, where no source code files are present).

Be aware that relying on bytecode files directly (and therefore not on source code files) prevents your modules from working across all Python implementations, or under newer Python releases that alter the bytecode format.

Added in version 3.3.

 name

The name of the module the loader will handle.

 path

The path to the bytecode file.

 is_package(*fullname*)

Determines if the module is a package based on `path`.

 get_code(*fullname*)

Returns the code object for `name` created from `path`.

 get_source(*fullname*)

Returns `None`, since bytecode files carry no source under this loader.

 load_module(*name=None*)

A concrete implementation of `importlib.abc.Loader.load_module()` in which naming the module to be loaded is optional.

Deprecated since version 3.6, scheduled for removal in 3.15: switch over to `importlib.abc.Loader.exec_module()` instead.

[Subject index](INDEX.md) · [Previous](source-file-loader-contract.md) · [Continue](extension-file-loader-contract.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
