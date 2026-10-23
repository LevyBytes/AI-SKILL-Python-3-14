# What's New In Python 3.6 / importlib - importlib

### importlib

Whenever a module cannot be located, import now throws the fresh [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) exception, which subclasses [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError). Existing code that tests for `ImportError` inside try-except keeps functioning. (Contributed by Eric Snow in [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)

On the loader it wraps, [`importlib.util.LazyLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.util.LazyLoader) now invokes [`create_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.create_module), which lifts the limitation that had kept [`importlib.machinery.BuiltinImporter`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.BuiltinImporter) and [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ExtensionFileLoader) from pairing with `importlib.util.LazyLoader`.

A [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) is now an acceptable argument to [`importlib.util.cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source), [`importlib.util.source_from_cache()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.source_from_cache), and [`importlib.util.spec_from_file_location()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.spec_from_file_location).

[Subject index](INDEX.md) · [Previous source section](idlelib-and-idle.md) · [Next source section](inspect.md) · [Release/subject declaration](summary-release-highlights.md)
