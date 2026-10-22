# Python 3.12.0 alpha 1 / windows / files and paths

[gh-93824](https://github.com/python/cpython/issues/93824): On Windows ARM64, you can now drag Python files and drop them onto each other in Windows Explorer.

[gh-92817](https://github.com/python/cpython/issues/92817): Guarantees `py.exe` favors an active virtual environment ahead of default tags declared via environment variables or inside a `py.ini` file.

[gh-98414](https://github.com/python/cpython/issues/98414): Corrects how the `py.exe` launcher treats the `-V:*<company>*/` option once default preferences are already declared through environment variables or in configuration files.

[gh-97649](https://github.com/python/cpython/issues/97649): The `Tools` directory is no longer installed on Windows

[gh-96559](https://github.com/python/cpython/issues/96559): Addresses the Windows launcher failing to apply the compatible reading of default tags from configuration files in the case where the command supplied no tag.

[gh-94781](https://github.com/python/cpython/issues/94781): Correct `pcbuild.proj` so it wipes earlier copies of output files inside the `Python\deepfreeze` and `Python\frozen_modules` directories on Windows. Charlie Zhao contributed the patch.

[gh-94399](https://github.com/python/cpython/issues/94399): Brings back how the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) treats `/usr/bin/env` shebang lines: it once again scans `PATH` for an executable that matches the named command, falling back to the standard search when nothing turns up.

[gh-95445](https://github.com/python/cpython/issues/95445): Corrects the failure to delete the HTML document directory during an uninstall performed through the Windows msi.

[gh-95359](https://github.com/python/cpython/issues/95359): Repairs how the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) processes `py.ini` commands (it had wrongly looked for a `py_` prefix on the keys) plus crashes encountered while loading the per-user configuration file.

[gh-90844](https://github.com/python/cpython/issues/90844): Let virtual environments start up properly even when their path contains spaces.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
