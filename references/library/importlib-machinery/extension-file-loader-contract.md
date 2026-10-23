# importlib.machinery`importlib.machinery` – Importers and path hooks

*class *importlib.machinery.ExtensionFileLoader(*fullname*, *path*)

A concrete implementation of `importlib.abc.ExecutionLoader` aimed at extension modules.

The *fullname* argument names the module this loader is meant to handle. The *path* argument gives the path to the extension module's file.

Be aware that, by default, an extension module that does not provide multi-phase init (see [**PEP 489**](https://peps.python.org/pep-0489/)) will fail to import within subinterpreters, even where it would import without trouble elsewhere.

Added in version 3.3.

Changed in version 3.12: Subinterpreters now demand multi-phase init before such a module can be used.

 name

Name of the module the loader supports.

 path

Path to the extension module.

 create_module(*spec*)

Builds the module object out of the supplied specification, following [**PEP 489**](https://peps.python.org/pep-0489/).

Added in version 3.5.

 exec_module(*module*)

Sets up the supplied module object, following [**PEP 489**](https://peps.python.org/pep-0489/).

Added in version 3.5.

 is_package(*fullname*)

Returns `True` when the file path designates a package's `__init__` module, judged by `EXTENSION_SUFFIXES`.

 get_code(*fullname*)

Returns `None`, because extension modules have no code object.

 get_source(*fullname*)

Returns `None`, because extension modules carry no source code.

 get_filename(*fullname*)

Returns `path`.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](bytecode-only-file-loader-contract.md) · [Continue](importlib-machinery-namespaceloader-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
