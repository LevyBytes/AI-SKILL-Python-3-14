# importlib.machinery`importlib.machinery` – Importers and path hooks

*class *importlib.machinery.NamespaceLoader(*name*, *path*, *path_finder*)

A concrete implementation of `importlib.abc.InspectLoader` for namespace packages. It aliases a private class, exposed publicly solely so the `__loader__` attribute on namespace packages can be introspected:

```python
>>> from importlib.machinery import NamespaceLoader
>>> import my_namespace
>>> isinstance(my_namespace.__loader__, NamespaceLoader)
True
>>> import importlib.abc
>>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
True

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](extension-file-loader-contract.md) · [Continue](importlib-machinery-modulespec-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
