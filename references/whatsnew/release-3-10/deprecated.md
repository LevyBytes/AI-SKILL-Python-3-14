# What's New In Python 3.10 / Deprecated — importlib, random, threading, zipimport

### Deprecated

- Right now Python lets a numeric literal sit directly against a keyword, as in `0in x`, `1or x`, `0if 1else 2`. That opens the door to murky, ambiguous expressions such as `[0x1for x in y]` (readable either as `[0x1 for x in y]` or as `[0x1f or x in y]`). From this version on, a deprecation warning fires whenever a numeric literal butts up against one of the keywords [`and`](https://docs.python.org/3.14/reference/expressions.html#and), [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else), [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3.14/reference/expressions.html#in), [`is`](https://docs.python.org/3.14/reference/expressions.html#is) and [`or`](https://docs.python.org/3.14/reference/expressions.html#or). Later it becomes a syntax warning, and eventually a syntax error. (Contributed by Serhiy Storchaka in [bpo-43833](https://bugs.python.org/issue?@action=redirect&bpo=43833).)

- This release kicks off a deliberate push to retire legacy import behavior that lingered for Python 2.7 compatibility. The targets being phased out: `find_loader()`/`find_module()`, whose replacement is [`find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec); [`load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.load_module), now handled by [`exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module); `module_repr()`, which the import machinery handles automatically on your behalf; the `__package__` attribute, whose modern equivalent is `__spec__.parent`; the `__loader__` attribute, which gives way to `__spec__.loader`; and the `__cached__` attribute, replaced by `__spec__.cached`. These — plus other classes and methods within [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) — will be removed gradually. Where helpful, [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning) and/or [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) will fire so you can spot code that must change during the move.

- The whole `distutils` namespace is now deprecated and is set to disappear in Python 3.12. See the module changes section for further detail.

- Passing non-integer values to [`random.randrange()`](https://docs.python.org/3.14/library/random.html#random.randrange) is now deprecated. In place of the old [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is the deprecated successor. (Contributed by Serhiy Storchaka and Raymond Hettinger in [bpo-37319](https://bugs.python.org/issue?@action=redirect&bpo=37319).)

- Although the assorted `load_module()` methods on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) have carried deprecation notes in the docs since Python 3.6, they now emit a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) as well. Switch to [`exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module). (Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- `zimport.zipimporter.load_module()` is now deprecated; favor [`exec_module()`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter.exec_module) instead. (Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- When the import system calls [`load_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.load_module), it now raises an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning), since [`exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module) is the preferred path. (Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- Reliance on `importlib.abc.MetaPathFinder.find_module()` and `importlib.abc.PathEntryFinder.find_module()` within the import system now raises an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning), because [`importlib.abc.MetaPathFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) and [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) are the respective replacements. To ease the migration, reach for [`importlib.util.spec_from_loader()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.spec_from_loader). (Contributed by Brett Cannon in [bpo-42134](https://bugs.python.org/issue?@action=redirect&bpo=42134).)

- When the import system relies on `importlib.abc.PathEntryFinder.find_loader()`, it now emits an [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning), given that [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec) is the preferred route. [`importlib.util.spec_from_loader()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.spec_from_loader) can assist with the port. (Contributed by Brett Cannon in [bpo-43672](https://bugs.python.org/issue?@action=redirect&bpo=43672).)

- A number of concrete implementations now emit [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) and are tagged for removal in Python 3.12 (they had already been marked deprecated back in Python 3.4): the `importlib.abc.MetaPathFinder.find_module()` variants ( `importlib.machinery.BuiltinImporter.find_module()`, `importlib.machinery.FrozenImporter.find_module()`, `importlib.machinery.WindowsRegistryFinder.find_module()`, `importlib.machinery.PathFinder.find_module()`, `importlib.abc.MetaPathFinder.find_module()` ), together with `importlib.abc.PathEntryFinder.find_module()` ( `importlib.machinery.FileFinder.find_module()` ) and `importlib.abc.PathEntryFinder.find_loader()` ( `importlib.machinery.FileFinder.find_loader()` ). (Contributed by Brett Cannon in [bpo-42135](https://bugs.python.org/issue?@action=redirect&bpo=42135).)

- `importlib.abc.Finder`, along with its lone `find_module()` method, is now deprecated. Neither [`importlib.abc.MetaPathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder) nor [`importlib.abc.PathEntryFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder) derives from it any longer. Pick whichever of those two base classes fits and subclass that instead. (Contributed by Brett Cannon in [bpo-42135](https://bugs.python.org/issue?@action=redirect&bpo=42135).)

- Removal of `imp`, `importlib.find_loader()`, `importlib.util.set_package_wrapper()`, `importlib.util.set_loader_wrapper()`, `importlib.util.module_for_loader()`, `pkgutil.ImpImporter`, and `pkgutil.ImpLoader` is now pinned to Python 3.12 in their deprecation notices (each had already started emitting [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) in earlier Python releases). (Contributed by Brett Cannon in [bpo-43720](https://bugs.python.org/issue?@action=redirect&bpo=43720).)

- For a module's `__repr__()`, the import system now consults the `__spec__` attribute first and only resorts to `module_repr()` afterward. The plan is to drop the `module_repr()` fallback in Python 3.12. (Contributed by Brett Cannon in [bpo-42137](https://bugs.python.org/issue?@action=redirect&bpo=42137).)

- `importlib.abc.Loader.module_repr()`, `importlib.machinery.FrozenLoader.module_repr()`, and `importlib.machinery.BuiltinLoader.module_repr()` now carry deprecation status and are earmarked for removal in Python 3.12. (Contributed by Brett Cannon in [bpo-42136](https://bugs.python.org/issue?@action=redirect&bpo=42136).)

- Ever since Python 3.3 — when it became an alias for [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) — `sqlite3.OptimizedUnicode` has been undocumented and obsolete. It is deprecated now and due to go away in Python 3.12. (Contributed by Erlend E. Aasland in [bpo-42264](https://bugs.python.org/issue?@action=redirect&bpo=42264).)

- The undocumented built-in `sqlite3.enable_shared_cache` is deprecated as of this release and earmarked for removal in Python 3.12. The SQLite3 documentation actively warns against using it. Consult [the SQLite3 docs](https://sqlite.org/c3ref/enable_shared_cache.html) for the specifics. Should you genuinely need a shared cache, open the database in URI mode and pass the `cache=shared` query parameter. (Contributed by Erlend E. Aasland in [bpo-24464](https://bugs.python.org/issue?@action=redirect&bpo=24464).)

- These `threading` methods now carry deprecation status:

  - `threading.currentThread` => [`threading.current_thread()`](https://docs.python.org/3.14/library/threading.html#threading.current_thread)

  - `threading.activeCount` => [`threading.active_count()`](https://docs.python.org/3.14/library/threading.html#threading.active_count)

  - `threading.Condition.notifyAll` => [`threading.Condition.notify_all()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.notify_all)

  -

`threading.Event.isSet` => [`threading.Event.is_set()`](https://docs.python.org/3.14/library/threading.html#threading.Event.is_set)

  - `threading.Thread.setName` => [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name)

  - `threading.thread.getName` => [`threading.Thread.name`](https://docs.python.org/3.14/library/threading.html#threading.Thread.name)

  - `threading.Thread.isDaemon` => [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon)

  - `threading.Thread.setDaemon` => [`threading.Thread.daemon`](https://docs.python.org/3.14/library/threading.html#threading.Thread.daemon)

(Contributed by Jelle Zijlstra in [gh-87889](https://github.com/python/cpython/issues/87889).)

- `pathlib.Path.link_to()` is now deprecated, with removal targeted for Python 3.12. Reach for [`pathlib.Path.hardlink_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.hardlink_to) in its place. (Contributed by Barney Gale in [bpo-39950](https://bugs.python.org/issue?@action=redirect&bpo=39950).)

- `cgi.log()` is now deprecated and lined up for removal in Python 3.12. (Contributed by Inada Naoki in [bpo-41139](https://bugs.python.org/issue?@action=redirect&bpo=41139).)

- These [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) capabilities, deprecated since Python 3.6, Python 3.7, or OpenSSL 1.1.0, are slated to be dropped in 3.11:

  - `OP_NO_SSLv2`, `OP_NO_SSLv3`, `OP_NO_TLSv1`, `OP_NO_TLSv1_1`, `OP_NO_TLSv1_2`, and `OP_NO_TLSv1_3` give way to [`minimum_version`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.minimum_version) and [`maximum_version`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.maximum_version).

  - `PROTOCOL_SSLv2`, `PROTOCOL_SSLv3`, `PROTOCOL_SSLv23`, `PROTOCOL_TLSv1`, `PROTOCOL_TLSv1_1`, `PROTOCOL_TLSv1_2`, and `PROTOCOL_TLS` are superseded by [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3.14/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT) and [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3.14/library/ssl.html#ssl.PROTOCOL_TLS_SERVER)

  - `wrap_socket()` gives way to [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_socket)

  - `match_hostname()`

  - `RAND_pseudo_bytes()`, `RAND_egd()`

  - NPN-related members such as [`ssl.SSLSocket.selected_npn_protocol()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket.selected_npn_protocol) and [`ssl.SSLContext.set_npn_protocols()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.set_npn_protocols) give way to ALPN.

- Threading debug mode (the `PYTHONTHREADDEBUG` environment variable) became deprecated in Python 3.10 and is scheduled to vanish in Python 3.12. It only works with a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build). (Contributed by Victor Stinner in [bpo-44584](https://bugs.python.org/issue?@action=redirect&bpo=44584).)

- Pulling things in from the `typing.io` and `typing.re` submodules now produces a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). A later Python version will drop these submodules entirely. Import whatever lives in them straight from [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) instead. (Contributed by Sebastian Rittau in [bpo-38291](https://bugs.python.org/issue?@action=redirect&bpo=38291).)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](removed.md)
