# What's New In Python 3.13 / Changes in the Python API - functools, getpass, gzip, mailbox, pathlib, threading, zipfile

### Changes in the Python API

- Several shifts in the semantics of [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) and [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) arrive with PEP 667:

  - Invoking [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) within an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope) now yields a fresh, independent snapshot every time, so it stops silently refreshing references handed back earlier. To reproduce the old CPython behavior you must now explicitly fold the results of later `locals()` calls into the dictionary returned the first time. Functions that run code while implicitly aiming at `locals()` (`exec` and `eval` among them) have to receive an explicit namespace if you want to read their results inside an optimized scope. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)

  - Invoking [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) from a comprehension at module or class scope (whether through `exec` or `eval`) again acts as though the comprehension ran as a standalone nested function — that is, the locals of the enclosing scope are left out. Python 3.12 had altered this to pull in the enclosing scope's locals while implementing [**PEP 709**](https://peps.python.org/pep-0709/). (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)

  - Reading [`FrameType.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) inside an [optimized scope](https://docs.python.org/3.14/glossary.html#term-optimized-scope) now hands back a write-through proxy in place of a snapshot refreshed at vaguely defined moments. When you do want a snapshot, build one yourself with `dict` or the proxy's `.copy()` method. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/).)

- Used as a method, [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) now raises a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning). Later Python releases will change how it behaves. To hold onto the former behavior, wrap it in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod). (Contributed by Serhiy Storchaka in [gh-121027](https://github.com/python/cpython/issues/121027).)

- Whenever [`getpass.getuser()`](https://docs.python.org/3.14/library/getpass.html#getpass.getuser) cannot obtain a username, it now raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) — rather than [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) on platforms that aren't Unix, or [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) on Unix platforms whose password database holds nothing.

- On [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) the `mode` attribute now holds a string (`'rb'` or `'wb'`) where before it held an integer (`1` or `2`). For the readable file-like object that [`zipfile.ZipFile.open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) returns, the `mode` attribute is now `'rb'` rather than `'r'`. (Contributed by Serhiy Storchaka in [gh-115961](https://github.com/python/cpython/issues/115961).)

- [`mailbox.Maildir`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Maildir) now ignores files with a leading dot (`.`). (Contributed by Zackery Spytz in [gh-65559](https://github.com/python/cpython/issues/65559).)

- When handed a pattern closing with “`**`”, [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) now yield files alongside directories instead of directories alone. Append a trailing slash to retain the old behavior and match directories only.

- The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module now counts on the `_thread` module to supply an `_is_main_interpreter()` function. That function accepts no arguments and gives back `True` when the interpreter in play is the main one.

Should a library or application ship its own `_thread` module, it has to include `_is_main_interpreter()` too, on par with the module's remaining “private” attributes. ([gh-112826](https://github.com/python/cpython/issues/112826).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-13.md) · [Next source section](c-api-trashcan-migration.md) · [Release/subject declaration](summary-release-highlights.md)
