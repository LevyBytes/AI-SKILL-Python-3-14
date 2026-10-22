# Python 3.13.0 alpha 1 / library / functions and types

[gh-104783](https://github.com/python/cpython/issues/104783): Deleted the `locale.resetlocale()` function that had been deprecated in Python 3.11. Victor Stinner authored the change.

[gh-104992](https://github.com/python/cpython/issues/104992): Deleted the untested and undocumented `unittest.TestProgram.usageExit()` method, which had been deprecated in Python 3.11. Hugo van Kemenade authored the change.

[gh-105808](https://github.com/python/cpython/issues/105808): Address a regression that arrived via [gh-101251](https://github.com/python/cpython/issues/101251) for 3.12, where `gzip.GzipFile.flush()` failed to flush the compressor (and skipped passing along the `zip_mode` argument).

[gh-105745](https://github.com/python/cpython/issues/105745): Repair the `webbrowser.Konqueror.open` method.

[gh-109599](https://github.com/python/cpython/issues/109599): Surface the type of PyCapsule objects under the name `types.CapsuleType`.

[gh-105545](https://github.com/python/cpython/issues/105545): Drop the `webbrowser.MacOSXOSAScript._name` attribute that was deprecated back in 3.11.

[gh-89812](https://github.com/python/cpython/issues/89812): Introduce the private `pathlib._PathBase` class, offering experimental backing for virtual filesystems and possibly becoming public in some later version of Python.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
