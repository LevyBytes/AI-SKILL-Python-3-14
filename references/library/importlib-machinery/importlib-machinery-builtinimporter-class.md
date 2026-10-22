# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.BuiltinImporter

An [importer](https://docs.python.org/3.14/glossary.html#term-importer) for built-in modules. Every built-in module that is known appears in [`sys.builtin_module_names`](https://docs.python.org/3.14/library/sys.html#sys.builtin_module_names). This class implements the `importlib.abc.MetaPathFinder` and `importlib.abc.InspectLoader` ABCs.

The class exposes only class methods, removing any requirement to instantiate it.

Changed in version 3.5: Under [**PEP 489**](https://peps.python.org/pep-0489/), this builtin importer gained implementations of `Loader.create_module()` plus `Loader.exec_module()`

[Subject index](INDEX.md) · [Previous](importable-file-suffixes.md) · [Continue](importlib-machinery-frozenimporter-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
