# What's New In Python 3.3 / Porting Python code — datetime, decimal, email.header, email.parser, email.utils, importlib, pkgutil, poplib, smtplib, socket, sys, time

### Porting Python code

- By default, hash randomization is turned on. To switch it off, give the [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED) environment variable a value of `0`. The [`object.__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method is also worth consulting.

- [bpo-12326](https://bugs.python.org/issue?@action=redirect&bpo=12326): Under Linux, the major version no longer appears in sys.platform. Regardless of which Linux release built Python, the value reads ‘linux’ now rather than the former ‘linux2’ or ‘linux3’. Swap sys.platform == ‘linux2’ for sys.platform.startswith(‘linux’); or, when backward support for older Python releases isn't a concern, just use sys.platform == ‘linux’.

- [bpo-13847](https://bugs.python.org/issue?@action=redirect&bpo=13847), [bpo-14180](https://bugs.python.org/issue?@action=redirect&bpo=14180): within [`time`](https://docs.python.org/3.14/library/time.html#module-time) and [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime), a timestamp falling outside the valid range now triggers [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) where it once triggered [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Should the C functions `gmtime()` or `localtime()` fail, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is what gets raised.

- Import's default finders now keep a cache describing the contents of each particular directory. Whenever you add a Python source file or a sourceless bytecode file, be sure to invoke [`importlib.invalidate_caches()`](https://docs.python.org/3.14/library/importlib.html#importlib.invalidate_caches) so the cache is cleared and the finders pick up your new file.

- The module name carried by [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) is now the fully qualified one for whichever module the import targeted. Any doctests that inspect ImportErrors' message must be revised to expect that full module name rather than merely the trailing portion.

- For [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__), the *index* argument now defaults to 0 in place of -1 and rejects negative values entirely. Leaving that default at -1 was an oversight at the time [**PEP 328**](https://peps.python.org/pep-0328/) landed. Where you still must do a relative import and then an absolute one, run the relative import at an index of 1, then issue a second import at an index of 0. The recommended route, however, is to rely on [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) instead of calling `__import__()` yourself.

- When dealing with top-level modules, [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) now refuses any index value besides 0. So, for instance, `__import__('sys', level=1)` is now an error.

- Since [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) and [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) ship with finders already populated by default, adding your own entry to those lists is best done with [`list.insert()`](https://docs.python.org/3.14/library/stdtypes.html#list.insert) rather than [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append).

- Given that `None` now gets placed into [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache), staying backwards-compatible while purging finder-less path entries from that dictionary means dropping keys whose value is `None` **and** those whose value is `imp.NullImporter`. On older Python releases this incurs some additional cost, because they re-insert `None` into `sys.path_importer_cache` to mark implicit finders, yet the meaning is unaffected.

- An abstract `find_module()` method that subclasses had to provide is no longer declared by `importlib.abc.Finder`. If your code counted on subclasses supplying that method, test for its presence before use. That said, when you're dealing with [path entry finders](https://docs.python.org/3.14/glossary.html#term-path-entry-finder), it's `find_loader()` you'll generally want to look for first.

- Internally, [`pkgutil`](https://docs.python.org/3.14/library/pkgutil.html#module-pkgutil) has been reworked to rely on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib). Doing so removes numerous corner cases in which the former [**PEP 302**](https://peps.python.org/pep-0302/) import emulation diverged from how the actual import system behaves. That emulation hasn't gone away, but it is deprecated now. Because [`pkgutil.iter_importers()`](https://docs.python.org/3.14/library/pkgutil.html#pkgutil.iter_importers) along with [`pkgutil.walk_packages()`](https://docs.python.org/3.14/library/pkgutil.html#pkgutil.walk_packages) handle the standard import hooks as special cases, those hooks keep working despite lacking the non-standard `iter_modules()` method.

- A long-standing RFC-compliance defect ([bpo-1079](https://bugs.python.org/issue?@action=redirect&bpo=1079)) affecting the parsing performed by [`email.header.decode_header()`](https://docs.python.org/3.14/library/email.header.html#email.header.decode_header) is now resolved. The customary pattern for turning encoded headers into unicode (`str(make_header(decode_header(h))`) behaves exactly as before, but anything that examines the separate tuples coming back from decode_header will notice that whitespace sitting just before or after `ASCII` sections is now folded into the `ASCII` section. Header-building code that goes through `make_header` likewise carries on unchanged, since `make_header` still inserts whitespace between `ASCII` and non-`ASCII` sections whenever the input strings don't already supply it.

- Given non-`ASCII` display names, [`email.utils.formataddr()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.formataddr) now applies the proper content transfer encoding. Code that leaned on the earlier faulty behavior, which left the non-`ASCII` unicode intact within the formatted output string, has to be updated ([bpo-1690608](https://bugs.python.org/issue?@action=redirect&bpo=1690608)).

- In line with every other `poplib` method, [`poplib.POP3.quit()`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3.quit) can now surface protocol errors. If a given application runs into errors on `quit`, code written on the assumption that `quit` never raises [`poplib.error_proto`](https://docs.python.org/3.14/library/poplib.html#poplib.error_proto) errors may have to be adjusted ([bpo-11291](https://bugs.python.org/issue?@action=redirect&bpo=11291)).

- On [`email.parser.Parser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.Parser), the `strict` argument — deprecated all the way back in Python 2.4 — is gone at last.

- The `unittest.TestCase.assertSameElements` method, long deprecated, has been dropped.

- The deprecated `time.accept2dyear` variable has been taken out.

- Within the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module, the deprecated `Context._clamp` attribute is gone; the public attribute [`clamp`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.clamp) had already taken its place earlier. (See [bpo-8540](https://bugs.python.org/issue?@action=redirect&bpo=8540).)

- From [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib), the undocumented internal helper class `SSLFakeFile` has been removed, given that [`socket.socket.makefile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.makefile) has long offered the same capability directly.

- Handing a negative value to [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) on Windows now produces an error rather than sleeping indefinitely. On posix it has always raised an error.

-

Removal of the `ast.__version__` constant means that, to branch on the AST version, you should consult [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info) instead.

- Any code that worked around the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module's use of factory functions by subclassing its private classes must be switched over to subclass the classes that are now public.

- The threading module's undocumented debugging machinery has been excised, which streamlines the code. Production code shouldn't feel any effect; it's noted here only on the chance that some application debug framework was hooking into it ([bpo-13550](https://bugs.python.org/issue?@action=redirect&bpo=13550)).

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-3.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](porting-c-code.md)
