# importlib.util: `importlib.util.LazyLoader`, `factory()`

*class *importlib.util.LazyLoader(*loader*)

A class that holds off running a module's loader right up until some attribute on the module gets read.

This class functions **only** alongside loaders supplying `exec_module()`, since deciding which module type the module receives has to be possible. By the same logic, the loader's `create_module()` method has to give back either `None` or a type whose `__class__` attribute is mutable and that steers clear of [slots](https://docs.python.org/3.14/glossary.html#term-__slots__). And lastly, any module that swaps out the object stored in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) cannot function here, because nothing can safely swing every module reference across the interpreter; spotting such a swap triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Note

When a project treats startup time as crucial, this class can shave the expense of loading a module that ends up never being touched. When startup time carries little weight, reaching for this class is **heavily** discouraged, since any error messages raised while loading get deferred and therefore land detached from their context.

Added in version 3.5.

Changed in version 3.6: Started invoking `create_module()`, which dropped the compatibility warning tied to `importlib.machinery.BuiltinImporter` and `importlib.machinery.ExtensionFileLoader`.

 *classmethod *factory(*loader*)

A class method handing back a callable that builds a lazy loader. Its purpose is the case where the loader arrives as a class rather than as an instance.

```python
suffixes = importlib.machinery.SOURCE_SUFFIXES
loader = importlib.machinery.SourceFileLoader
lazy_loader = importlib.util.LazyLoader.factory(loader)
finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))

```

[Subject index](INDEX.md) · [Previous](module-spec-creation-and-extension-restrictions.md) · [Continue](importing-programmatically.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md)
