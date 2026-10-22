# 5.3. Searching

### 5.3. Searching

Kicking off the search requires Python to know the [fully qualified](https://docs.python.org/3.14/glossary.html#term-qualified-name) name of the module being imported (or of the package — but here that distinction doesn’t matter). Such a name might originate from one of several arguments to the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement, or from the parameters handed to [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) or [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__).

That name gets used across the several stages of the import search, and it can take the form of a dotted route to a submodule, such as `foo.bar.baz`. When that happens, Python imports `foo` first, then `foo.bar`, and lastly `foo.bar.baz`. Failure of any of those intervening imports yields a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError).

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](namespace-packages.md) · [Following source section](the-module-cache.md)
