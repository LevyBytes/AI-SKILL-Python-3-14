# What's New In Python 3.7 / importlib — importlib

### importlib

The `importlib.abc.ResourceReader` ABC arrived to enable loading resources out of packages. See also importlib.resources. (Contributed by Barry Warsaw, Brett Cannon in [bpo-32248](https://bugs.python.org/issue?@action=redirect&bpo=32248).)

[`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload) will now raise [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) when a module has no spec. (Contributed by Garvit Khatri in [bpo-29851](https://bugs.python.org/issue?@action=redirect&bpo=29851).)

[`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec) will now raise [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when the named parent module isn't a package (that is, it has no `__path__` attribute). (Contributed by Milan Oberkirch in [bpo-30436](https://bugs.python.org/issue?@action=redirect&bpo=30436).)

A new [`importlib.util.source_hash()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.source_hash) computes the hash of source you hand it. The value this function returns gets embedded inside a hash-based .pyc file.

### importlib

The `MetaPathFinder.find_module()` method (whose replacement is [`MetaPathFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec)) and the `PathEntryFinder.find_loader()` method (whose replacement is [`PathEntryFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec)), each deprecated back in Python 3.4, now raise [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). (Contributed by Matthias Bussonnier in [bpo-29576](https://bugs.python.org/issue?@action=redirect&bpo=29576).)

The [`importlib.abc.ResourceLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.ResourceLoader) ABC is now deprecated, with `importlib.abc.ResourceReader` preferred in its place.

[Subject index](INDEX.md) · [Previous source section](idlelib-and-idle.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](gettext.md) · [Next source section](locale.md)
