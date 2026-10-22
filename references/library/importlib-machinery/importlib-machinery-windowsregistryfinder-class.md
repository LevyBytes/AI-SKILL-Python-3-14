# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.WindowsRegistryFinder

[Finder](https://docs.python.org/3.14/glossary.html#term-finder) for modules registered in the Windows registry. This class implements the `importlib.abc.MetaPathFinder` ABC.

The class exposes only class methods, removing any requirement to instantiate it.

Added in version 3.3.

Deprecated since version 3.6: Prefer [`site`](https://docs.python.org/3.14/library/site.html#module-site) configuration. Later Python releases might leave this finder disabled out of the box.

[Subject index](INDEX.md) · [Previous](importlib-machinery-frozenimporter-class.md) · [Continue](importlib-machinery-pathfinder-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
