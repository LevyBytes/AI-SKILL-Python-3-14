# 5.3.4. The meta path

### 5.3.4. The meta path

Whenever the requested module is absent from [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), Python turns next to [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path), which holds a list of meta path finder objects. Each of those finders is asked in turn whether it knows how to deal with the requested module. A meta path finder is required to provide a method named [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) that accepts three arguments: a name, an import path, and (optionally) a target module. To decide whether it can deal with the requested module, the meta path finder may apply whatever strategy it pleases.

Should the meta path finder know how to deal with the requested module, it hands back a spec object. When it cannot, it hands back `None`. If [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) handling runs off the end of its list without yielding a spec, a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) results. Every other raised exception simply travels upward, cutting the import process short.

A meta path finder’s [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) method receives either two or three arguments. The first of them is the fully qualified name of the module under import, such as `foo.bar.baz`. The second supplies the path entries to draw on for the module search. With top-level modules, that second argument comes in as `None`, whereas with submodules or subpackages it carries the value of the parent package’s `__path__` attribute. Should the relevant `__path__` attribute prove unreachable, a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) results. The third argument holds an already-existing module object slated to be the target of a later load. Only on reload does the import system supply a target module.

A single import request may walk the meta path more than once. Take, for instance, importing `foo.bar.baz` when none of the relevant modules sit in the cache yet: Python begins with a top level import, calling `mpf.find_spec("foo", None, None)` against every meta path finder (`mpf`). Once `foo` is imported, `foo.bar` follows via a second walk of the meta path, this time calling `mpf.find_spec("foo.bar", foo.__path__, None)`. With `foo.bar` imported, the closing walk issues `mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)`.

A handful of meta path finders handle only top level imports. Such importers invariably hand back `None` whenever the second argument is anything besides `None`.

Three meta path finders make up Python’s default [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path): one understands importing built-in modules, another understands importing frozen modules, and the last understands importing modules off an [import path](https://docs.python.org/3.14/glossary.html#term-import-path) (that is, the [path based finder](https://docs.python.org/3.14/glossary.html#term-path-based-finder)).

Changed in version 3.4: A meta path finder’s [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) method took over from `find_module()`, which now carries deprecated status. Even though it still functions unchanged, the import machinery will fall back on it only when the finder lacks a `find_spec()` implementation.

Changed in version 3.10: When the import system uses `find_module()`, it now emits an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning).

Changed in version 3.12: `find_module()` is gone. Reach for [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) in its place.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](searching.md) · [Previous source section](import-hooks.md) · [Following source section](loading.md)
