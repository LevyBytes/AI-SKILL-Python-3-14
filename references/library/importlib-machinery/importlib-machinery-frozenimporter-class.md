# importlib.machinery`importlib.machinery` – Importers and path hooks

*class *importlib.machinery.FrozenImporter

An [importer](https://docs.python.org/3.14/glossary.html#term-importer) for frozen modules. This class implements the `importlib.abc.MetaPathFinder` and `importlib.abc.InspectLoader` ABCs.

The class exposes only class methods, removing any requirement to instantiate it.

Changed in version 3.4: Gained `create_module()` and `exec_module()` methods.

[Subject index](INDEX.md) · [Previous](importlib-machinery-builtinimporter-class.md) · [Continue](importlib-machinery-windowsregistryfinder-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
