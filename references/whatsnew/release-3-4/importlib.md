# What's New In Python 3.4 / importlib — importlib

### importlib

The [`InspectLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader) ABC adds a fresh method, [`source_to_code()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader.source_to_code), which takes source data plus a path and yields a code object. By default it behaves like `compile(data, path, 'exec', dont_inherit=True)`. (Contributed by Eric Snow and Brett Cannon in [bpo-15627](https://bugs.python.org/issue?@action=redirect&bpo=15627).)

[`InspectLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader) additionally ships a default body for the [`get_code()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader.get_code) method. That said, replacing the supplied default is usually worthwhile for the sake of speed. (Contributed by Brett Cannon in [bpo-18072](https://bugs.python.org/issue?@action=redirect&bpo=18072).)

The [`reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload) function has migrated out of `imp` and into [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) as the `imp` module winds toward deprecation. (Contributed by Berker Peksag in [bpo-18193](https://bugs.python.org/issue?@action=redirect&bpo=18193).)

[`importlib.util`](https://docs.python.org/3.14/library/importlib.html#module-importlib.util) now exposes a [`MAGIC_NUMBER`](https://docs.python.org/3.14/library/importlib.html#importlib.util.MAGIC_NUMBER) attribute that surfaces the bytecode version number. It stands in for the `get_magic()` function from the deprecated `imp` module. (Contributed by Brett Cannon in [bpo-18192](https://bugs.python.org/issue?@action=redirect&bpo=18192).)

Fresh [`importlib.util`](https://docs.python.org/3.14/library/importlib.html#module-importlib.util) helpers [`cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source) and [`source_from_cache()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.source_from_cache) take over from the identically named functions inside the deprecated `imp` module. (Contributed by Brett Cannon in [bpo-18194](https://bugs.python.org/issue?@action=redirect&bpo=18194).)

The [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) bootstrap [`NamespaceLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.NamespaceLoader) now satisfies the [`InspectLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader) ABC, so `runpy` together with `python -m` work against namespace packages. (Contributed by Brett Cannon in [bpo-18058](https://bugs.python.org/issue?@action=redirect&bpo=18058).)

[`importlib.util`](https://docs.python.org/3.14/library/importlib.html#module-importlib.util) adds a [`decode_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.decode_source) function that turns byte source into text with universal newline handling. It comes in handy when writing [`InspectLoader.get_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader.get_source) methods.

[`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ExtensionFileLoader) gains a [`get_filename()`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_filename) method. It had been left out by mistake when the loader was first written. (Contributed by Eric Snow in [bpo-19152](https://bugs.python.org/issue?@action=redirect&bpo=19152).)

[Subject index](INDEX.md) · [Previous source section](idlelib-and-idle.md) · [Next source section](inspect.md) · [Release/subject declaration](release-highlights.md)
