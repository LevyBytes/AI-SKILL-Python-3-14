# What’s New In Python 3.12 / distutils

### distutils

- Drop the `distutils` package. [**PEP 632**](https://peps.python.org/pep-0632/) "Deprecate distutils module" deprecated it back in Python 3.10. Where a project still leans on `distutils` and cannot migrate elsewhere, installing the `setuptools` project remains an option: it continues to ship `distutils`. (Contributed by Victor Stinner in [gh-92584](https://github.com/python/cpython/issues/92584).)

[Subject index](INDEX.md) · [Previous source section](configparser.md) · [Next source section](ensurepip.md) · [Release/subject declaration](summary-release-highlights.md)
