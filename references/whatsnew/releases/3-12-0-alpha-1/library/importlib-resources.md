# Python 3.12.0 alpha 1 / library / importlib resources

[gh-93353](https://github.com/python/cpython/issues/93353): Patch the [`importlib.resources.as_file()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.as_file) context manager so the temporary file is still deleted even when teardown happens late in Python finalization: it now retains a local handle to the [`os.remove()`](https://docs.python.org/3.14/library/os.html#os.remove) function. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
