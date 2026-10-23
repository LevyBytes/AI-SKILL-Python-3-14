# importlib.util - Approximating `importlib.import_module()`

### Approximating `importlib.import_module()`

Because import is itself written in Python, the bulk of the import machinery can be surfaced by way of importlib. What follows clarifies the assorted APIs that importlib makes available, doing so through a rough reconstruction of `importlib.import_module()`:

```python
import importlib.util
import sys

def import_module(name, package=None):
    """An approximate implementation of import."""
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass

    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)
    if path is not None:
        setattr(parent_module, child_name, module)
    return module

```

[Subject index](INDEX.md) · [Previous](setting-up-an-importer.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
