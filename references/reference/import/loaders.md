# 5.4.1. Loaders

### 5.4.1. Loaders

The pivotal service module loaders deliver in loading is running the module. With a lone argument — the module object meant to run — the import machinery invokes the [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module) method. Anything `exec_module()` returns is disregarded.

These requirements must be met by loaders:

- Provided the module is a Python module (rather than a built-in module or an extension loaded dynamically), the loader ought to run the module’s code within the module’s global name space (`module.__dict__`).

- Should the loader be unable to run the module, it ought to raise an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError), though any other exception thrown while [`exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module) runs will travel onward.

Quite often a single object serves as both finder and loader; in that scenario the [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) method would merely hand back a spec whose loader is set to `self`.

By providing a [`create_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.create_module) method, module loaders can choose to take charge of producing the module object during loading. That method accepts a single argument, the module spec, and gives back the fresh module object to be used while loading. There is no need for `create_module()` to set any attributes on the module object. Should the method give back `None`, the import machinery will produce the new module on its own.

Added in version 3.4: The [`create_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.create_module) method of loaders.

Changed in version 3.4: The [`exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module) method took the place of the [`load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.load_module) method, and the import machinery took on every one of the boilerplate duties of loading.

To stay compatible with loaders already out there, the import machinery will call a loader’s `load_module()` method when that method is present and the loader does not additionally supply `exec_module()`. That said, `load_module()` now carries deprecated status, and loaders ought to supply `exec_module()` in its place.

Beyond running the module, the `load_module()` method has to carry out all the boilerplate loading work outlined earlier. Every one of the same constraints still holds, plus a bit more clarification:

- Whenever a module object under the given name is already present in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), the loader is obliged to reuse that existing module. (If it doesn’t, [`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload) will misbehave.) Should the named module be absent from `sys.modules`, the loader has to build a fresh module object and insert it into `sys.modules`.

-

To guard against runaway recursion or duplicate loading, the module *must* already be registered in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) by the time the loader runs the module's code.

- When loading does not succeed, the loader is required to back out any modules it added to [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules); however, it should drop **only** the module(s) that failed, and only those the loader itself put there on purpose.

Changed in version 3.5: where `exec_module()` is present but `create_module()` is missing, a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) gets emitted.

Changed in version 3.6: where `exec_module()` is present but `create_module()` is missing, an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) gets emitted.

Changed in version 3.10: calling `load_module()` now triggers [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning).

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](loading.md) · [Following source section](submodules.md)
