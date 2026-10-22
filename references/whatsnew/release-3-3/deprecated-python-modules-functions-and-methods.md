# What's New In Python 3.3 / Deprecated Python modules, functions and methods — abc, ftplib, importlib, os, subprocess, time

### Deprecated Python modules, functions and methods

- Handing a non-empty string to `object.__format__()` is deprecated and will raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) once Python 3.4 lands ([bpo-9856](https://bugs.python.org/issue?@action=redirect&bpo=9856)).

- On account of [**PEP 393**](https://peps.python.org/pep-0393/), the `unicode_internal` codec is deprecated; reach instead for UTF-8, UTF-16 (`utf-16-le` or `utf-16-be`), or UTF-32 (`utf-32-le` or `utf-32-be`)

- [`ftplib.FTP.nlst()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.nlst) and [`ftplib.FTP.dir()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.dir): use [`ftplib.FTP.mlsd()`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP.mlsd)

- `platform.popen()`: use the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module. Check especially the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3.14/library/subprocess.html#subprocess-replacements) section ([bpo-11377](https://bugs.python.org/issue?@action=redirect&bpo=11377)).

- [bpo-13374](https://bugs.python.org/issue?@action=redirect&bpo=13374): Within the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module, the Windows bytes API is now deprecated. Prefer Unicode filenames over bytes ones, so you stop relying on the ANSI code page and can handle any filename.

- [bpo-13988](https://bugs.python.org/issue?@action=redirect&bpo=13988): The `xml.etree.cElementTree` module is deprecated. Whenever the accelerator exists, it is engaged automatically.

- How `time.clock()` behaves varies by platform: switch to the new [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) or [`time.process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time) function, picking whichever suits your needs, for behaviour that is well defined.

- The `os.stat_float_times()` function is deprecated.

- [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module:

  - [`abc.abstractproperty`](https://docs.python.org/3.14/library/abc.html#abc.abstractproperty) has been deprecated, use [`property`](https://docs.python.org/3.14/library/functions.html#property) with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) instead.

  - [`abc.abstractclassmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractclassmethod) has been deprecated, use [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) instead.

  - [`abc.abstractstaticmethod`](https://docs.python.org/3.14/library/abc.html#abc.abstractstaticmethod) has been deprecated, use [`staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) with [`abc.abstractmethod()`](https://docs.python.org/3.14/library/abc.html#abc.abstractmethod) instead.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) package:

  - [`importlib.abc.SourceLoader.path_mtime()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.SourceLoader.path_mtime) is deprecated now, with [`importlib.abc.SourceLoader.path_stats()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.SourceLoader.path_stats) preferred, because bytecode files presently keep both the size and the modification time of whatever source they were compiled from.

[Subject index](INDEX.md) · [Previous source section](unsupported-operating-systems.md) · [Next source section](deprecated-functions-and-types-of-the-c-api.md) · [Release/subject declaration](summary-release-highlights.md)
