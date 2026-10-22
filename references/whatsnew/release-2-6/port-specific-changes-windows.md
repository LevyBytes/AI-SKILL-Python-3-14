# What’s New in Python 2.6 / Port-Specific Changes: Windows — msvcrt, os.path, socket, winreg

### Port-Specific Changes: Windows

- Support for Windows 95, 98, ME and NT4 has gone away. Python 2.6 calls for Windows 2000 SP4 or newer.

- On Windows the new default compiler is Visual Studio 2008 (version 9.0). The build directories belonging to Visual Studio 2003 (version 7.1) and 2005 (version 8.0) were relocated into the PC/ directory. The new `PCbuild` directory handles cross compilation for X64, debug builds, and Profile Guided Optimization (PGO). A PGO build comes out roughly 10% faster than an ordinary build. (Contributed by Christian Heimes, who had help from Amaury Forgeot d'Arc and Martin von Löwis.)

- For the console I/O API, the [`msvcrt`](https://docs.python.org/3.14/library/msvcrt.html#module-msvcrt) module now covers both the ordinary and the wide-char flavors. A keypress is read by the [`getwch()`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.getwch) function, which gives back a Unicode value, and the [`getwche()`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.getwche) function behaves the same way. The [`putwch()`](https://docs.python.org/3.14/library/msvcrt.html#msvcrt.putwch) function takes a Unicode character and writes it out to the console. (Contributed by Christian Heimes.)

- [`os.path.expandvars()`](https://docs.python.org/3.14/library/os.path.html#os.path.expandvars) now expands environment variables written as "%var%", and "~user" expands into that user's home directory path. (Contributed by Josiah Carlson; [bpo-957650](https://bugs.python.org/issue?@action=redirect&bpo=957650).)

- Socket objects from the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now carry an [`ioctl()`](https://docs.python.org/3.14/library/socket.html#socket.socket.ioctl) method, giving a narrow interface onto the `WSAIoctl()` system interface.

- The [`_winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg) module now offers a function, [`ExpandEnvironmentStrings()`](https://docs.python.org/3.14/library/winreg.html#winreg.ExpandEnvironmentStrings), that expands environment variable references such as `%NAME%` inside an input string. The handle objects this module supplies now honor the context protocol, so they work inside [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements. (Contributed by Christian Heimes.)

[`_winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg) also handles x64 systems better, surfacing the [`DisableReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.DisableReflectionKey), [`EnableReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.EnableReflectionKey), and [`QueryReflectionKey()`](https://docs.python.org/3.14/library/winreg.html#winreg.QueryReflectionKey) functions, which turn registry reflection on and off for 32-bit processes that run on 64-bit systems. ([bpo-1753245](https://bugs.python.org/issue?@action=redirect&bpo=1753245))

- The `Record` object in the `msilib` module picked up `GetInteger()` and `GetString()` methods that hand back field values as an integer or a string. (Contributed by Floris Bruynooghe; [bpo-2125](https://bugs.python.org/issue?@action=redirect&bpo=2125).)

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Next source section](port-specific-changes-mac-os-x.md) · [Release/subject declaration](python-3-0.md)
