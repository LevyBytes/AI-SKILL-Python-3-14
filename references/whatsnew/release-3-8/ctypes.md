# What’s New In Python 3.8 / ctypes - ctypes, os

> (Contributed by Serhiy Storchaka in [bpo-31680](https://bugs.python.org/issue?@action=redirect&bpo=31680).)

### ctypes

Under Windows, [`CDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CDLL) plus its subclasses now take a *winmode* parameter for setting flags on the `LoadLibraryEx` call beneath. By default those flags pull DLL dependencies only from trusted spots, covering the directory where the DLL lives (when you load the first DLL by full or partial path) together with any locations registered via [`add_dll_directory()`](https://docs.python.org/3.14/library/os.html#os.add_dll_directory).

[Subject index](INDEX.md) · [Previous source section](curses.md) · [Next source section](datetime.md) · [Release/subject declaration](assignment-expressions.md)
