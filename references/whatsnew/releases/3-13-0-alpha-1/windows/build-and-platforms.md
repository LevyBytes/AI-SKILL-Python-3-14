# Python 3.13.0 alpha 1 / windows / build and platforms

[gh-109286](https://github.com/python/cpython/issues/109286): Bumped the Windows installer over to SQLite 3.43.1.

[gh-109991](https://github.com/python/cpython/issues/109991): Bumped the Windows build over to OpenSSL 3.0.11.

[gh-83180](https://github.com/python/cpython/issues/83180): Adjusts the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) so it favors an active virtual environment once the launched script carries a shebang line using a Unix-like virtual command, even where that command asks for a particular version of Python.

[gh-105436](https://github.com/python/cpython/issues/105436): Make sure an empty environment block ends with two null characters, just as Windows requires.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
