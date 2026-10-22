# 5.3.1. The module cache

### 5.3.1. The module cache

[`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) is the very first location consulted while the import search runs. That mapping acts as a cache holding every module imported so far, the intermediate paths included. Hence, if `foo.bar.baz` had been imported earlier, `sys.modules` holds entries for `foo`, `foo.bar`, and `foo.bar.baz`. The value stored under each key is the matching module object.

While importing, the module name is searched for inside [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules); when it is there, the stored value is the module that fulfills the import, and the procedure ends. Yet a stored value of `None` triggers a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError). And when the module name is absent, Python keeps hunting for the module.

You can write to [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules). Removing a key might not get rid of the linked module (since other modules could still reference it), yet it does wipe the cache entry for that module, prompting Python to search afresh for the named module the next time it is imported. You may also set the key to `None`, which makes the module’s next import end in a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError).

Take care, though: if you hold onto a reference to the module object, wipe its cache entry within [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), and then import the named module once more, you’ll end up with two module objects that are *not* identical. [`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload), on the other hand, keeps the *same* module object, simply re-running the module’s code to refresh its contents.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](searching.md) · [Previous source section](searching.md) · [Following source section](finders-and-loaders.md)
