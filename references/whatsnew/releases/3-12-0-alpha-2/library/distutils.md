# Python 3.12.0 alpha 2 / library / distutils

[gh-92584](https://github.com/python/cpython/issues/92584): Delete the `distutils` package. [**PEP 632**](https://peps.python.org/pep-0632/) "Deprecate distutils module" marked it deprecated back in Python 3.10. Projects that still lean on `distutils` and cannot move off it can install the `setuptools` project, which continues to supply `distutils`. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
