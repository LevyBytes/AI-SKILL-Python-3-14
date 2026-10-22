# 5.4. Loading

### 5.4. Loading

After a module spec turns up, the import machinery draws on it (together with the loader it carries) while loading the module. What follows is a rough sketch of how the loading stage of import proceeds:

```python
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
    # It is assumed 'exec_module' will also be defined on the loader.
    module = spec.loader.create_module(spec)
if module is None:
    module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)

if spec.loader is None:
    # unsupported
    raise ImportError
if spec.origin is None and spec.submodule_search_locations is not None:
    # namespace package
    sys.modules[spec.name] = module
elif not hasattr(spec.loader, 'exec_module'):
    module = spec.loader.load_module(spec.name)
else:
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        try:
            del sys.modules[spec.name]
        except KeyError:
            pass
        raise
return sys.modules[spec.name]

```

Take note of these particulars:

- Whenever a module object under the given name is already present in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), import will have handed it back already.

- Ahead of the loader running the module code, the module is already present in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules). That matters because the module code might import itself (whether directly or indirectly); placing it in `sys.modules` ahead of time guards against runaway recursion at worst and repeated loading at best.

- When loading goes wrong, it is the failing module — and that module alone — that gets pulled out of [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules). Whatever already sits in the `sys.modules` cache, plus any module that loaded successfully as a side-effect, has to stay cached. Reloading differs here, since even the module that failed stays put in `sys.modules`.

- Once the module has been created yet before it runs, the import machinery assigns the import-related module attributes (“_init_module_attrs” in the pseudo-code shown above), as recapped in a [later section](https://docs.python.org/3.14/reference/datamodel.html#import-mod-attrs).

- Running the module is the pivotal point of loading, the moment the module’s namespace fills up. That execution is handed off wholly to the loader, which gets to decide both what is filled in and the manner of it.

- Whatever module gets created during loading and passed along to exec_module() may differ from the one handed back when import finishes [2].

Changed in version 3.4: The import system absorbed the boilerplate duties that used to belong to loaders. Formerly the [`importlib.abc.Loader.load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.load_module) method carried them out.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](the-meta-path.md) · [Following source section](loaders.md)
