# importlib.util — Implementing lazy imports

### Implementing lazy imports

The snippet that follows demonstrates one way to put lazy imports into practice:

```python
>>> import importlib.util
>>> import sys
>>> def lazy_import(name):
...     spec = importlib.util.find_spec(name)
...     loader = importlib.util.LazyLoader(spec.loader)
...     spec.loader = loader
...     module = importlib.util.module_from_spec(spec)
...     sys.modules[name] = module
...     loader.exec_module(module)
...     return module
...
>>> lazy_typing = lazy_import("typing")
>>> #lazy_typing is a real module object,
>>> #but it is not loaded in memory yet.
>>> lazy_typing.TYPE_CHECKING
False

```

[Subject index](INDEX.md) · [Previous](importing-a-source-file-directly.md) · [Continue](setting-up-an-importer.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
