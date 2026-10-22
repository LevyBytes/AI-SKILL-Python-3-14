# importlib.util — Checking if a module can be imported

### Checking if a module can be imported

Should you want to learn whether a module is importable while stopping short of performing the import itself, lean on `importlib.util.find_spec()`.

Bear in mind that when `name` refers to a submodule (it holds a dot), `importlib.util.find_spec()` goes ahead and imports the parent module.

```python
import importlib.util
import sys

# For illustrative purposes.
name = 'itertools'

if name in sys.modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    # If you chose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")

```

[Subject index](INDEX.md) · [Previous](importing-programmatically.md) · [Continue](importing-a-source-file-directly.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
