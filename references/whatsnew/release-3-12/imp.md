# What’s New In Python 3.12 / imp

### imp

- The `imp` module is gone. (Contributed by Barry Warsaw in [gh-98040](https://github.com/python/cpython/issues/98040).)

For migration, refer to the correspondence table below:

>
| imp | importlib |
| --- | --- |
| `imp.NullImporter` | Insert `None` into `sys.path_importer_cache` |
| `imp.cache_from_source()` | `importlib.util.cache_from_source()` |
| `imp.find_module()` | `importlib.util.find_spec()` |
| `imp.get_magic()` | `importlib.util.MAGIC_NUMBER` |
| `imp.get_suffixes()` | `importlib.machinery.SOURCE_SUFFIXES`, `importlib.machinery.EXTENSION_SUFFIXES`, and `importlib.machinery.BYTECODE_SUFFIXES` |
| `imp.get_tag()` | `sys.implementation.cache_tag` |
| `imp.load_module()` | `importlib.import_module()` |
| `imp.new_module(name)` | `types.ModuleType(name)` |
| `imp.reload()` | `importlib.reload()` |
| `imp.source_from_cache()` | `importlib.util.source_from_cache()` |
| `imp.load_source()` | *See below* |

Swap `imp.load_source()` out for:

```python
import importlib.util
import importlib.machinery

def load_source(modname, filename):
    loader = importlib.machinery.SourceFileLoader(modname, filename)
    spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
    module = importlib.util.module_from_spec(spec)
    # The module is always executed and not cached in sys.modules.
    # Uncomment the following line to cache the module.
    # sys.modules[module.__name__] = module
    loader.exec_module(module)
    return module

```

- Drop `imp` functions and attributes that have no replacement:

  - Undocumented functions:

    - `imp.init_builtin()`

    - `imp.load_compiled()`

    - `imp.load_dynamic()`

    - `imp.load_package()`

  - `imp.lock_held()`, `imp.acquire_lock()`, `imp.release_lock()`: per-module locks replaced the locking scheme back in Python 3.3.

  - `imp.find_module()` constants: `SEARCH_ERROR`, `PY_SOURCE`, `PY_COMPILED`, `C_EXTENSION`, `PY_RESOURCE`, `PKG_DIRECTORY`, `C_BUILTIN`, `PY_FROZEN`, `PY_CODERESOURCE`, `IMP_HOOK`.

[Subject index](INDEX.md) · [Previous source section](importlib.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md)
