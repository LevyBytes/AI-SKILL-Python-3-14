# importlib.util — Importing a source file directly

### Importing a source file directly

Treat this recipe carefully: it stands in for an import statement in which you name the file path outright instead of letting [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) be searched. Weigh other options beforehand, such as adjusting `sys.path` when what you really need is a proper module, or turning to [`runpy.run_path()`](https://docs.python.org/3.14/library/runpy.html#runpy.run_path) when the global namespace produced by executing a Python file is what suits you.

To pull in a Python source file straight from a path, apply the recipe below:

```python
import importlib.util
import sys

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# For illustrative purposes only (use of `json` is arbitrary).
import json
file_path = json.__file__
module_name = json.__name__

# Similar outcome as `import json`.
json = import_from_path(module_name, file_path)

```

[Subject index](INDEX.md) · [Previous](checking-if-a-module-can-be-imported.md) · [Continue](implementing-lazy-imports.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
