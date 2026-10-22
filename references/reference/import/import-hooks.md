# 5.3.3. Import hooks

### 5.3.3. Import hooks

Extensibility is built into the import machinery; the chief means of achieving it are the *import hooks*. Import hooks come in two varieties: *meta hooks* and *import path hooks*.

The point at which meta hooks fire is the very beginning of import handling, ahead of any other import handling apart from the [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) cache lookup. That timing lets meta hooks take over [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) handling, frozen modules, or even the built-in modules. You register meta hooks by appending new finder objects onto [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path), in the manner shown below.

Import path hooks fire during [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) (or `package.__path__`) handling, right when their related path item gets reached. You register import path hooks by appending new callables onto [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks), as shown below.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](searching.md) · [Previous source section](finders-and-loaders.md) · [Following source section](the-meta-path.md)
