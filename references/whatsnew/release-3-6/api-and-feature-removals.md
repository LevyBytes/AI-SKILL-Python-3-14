# What's New In Python 3.6 / API and Feature Removals - inspect, io, re, tkinter, traceback, zipfile

### Removed

### API and Feature Removals

- Within regular expressions, escapes that are unknown and consist of `'\'` plus an ASCII letter will from now on raise an error. Inside replacement templates passed to [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) such escapes remain permitted, though deprecated. Pairing the [`re.LOCALE`](https://docs.python.org/3.14/library/re.html#re.LOCALE) flag is restricted to binary patterns going forward.

- The `inspect.getmoduleinfo()` function is gone (its deprecation dated back to CPython 3.3). To resolve a module name from a path, lean on [`inspect.getmodulename()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmodulename) instead. (Contributed by Yury Selivanov in [bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248).)

- The `traceback.Ignore` class along with the `traceback.usage`, `traceback.modname`, `traceback.fullmodname`, `traceback.find_lines_from_code`, `traceback.find_lines`, `traceback.find_strings`, `traceback.find_executable_lines` methods are gone from the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module. These were undocumented methods, deprecated as far back as Python 3.2, and matching behaviour can be reached through private methods.

- Within the [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) widget classes, the placeholder `tk_menuBar()` and `tk_bindForTraversal()` methods are gone (the matching Tk commands had been obsolete ever since Tk 4.0).

- For the [`zipfile.ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile) class, its [`open()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile.open) method has dropped the `'U'` mode (deprecated as of Python 3.4). To read compressed text in [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) mode, turn to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper).

- The undocumented `IN`, `CDROM`, `DLFCN`, `TYPES`, `CDIO`, and `STROPTS` modules are gone. They used to live inside the platform specific `Lib/plat-*/` directories, yet they stayed perpetually stale, were not uniformly present across platforms, and lacked upkeep. You can still find the generator that produced them within the source distribution at [Tools/scripts/h2py.py](https://github.com/python/cpython/blob/v3.6.15/Tools/scripts/h2py.py).

- Gone now is the deprecated `asynchat.fifo` class.

[Subject index](INDEX.md) · [Previous source section](deprecated-build-options.md) · [Next source section](porting-to-python-3-6.md) · [Release/subject declaration](summary-release-highlights.md)
