# Python 3.14.1 final / library / locale

[gh-130567](https://github.com/python/cpython/issues/130567): Heads off a possible crash in [`locale.strxfrm()`](https://docs.python.org/3.14/library/locale.html#locale.strxfrm) that stems from a platform bug on macOS.

[gh-60462](https://github.com/python/cpython/issues/60462): Corrects [`locale.strxfrm()`](https://docs.python.org/3.14/library/locale.html#locale.strxfrm) on Solaris (and conceivably elsewhere too).

[gh-137273](https://github.com/python/cpython/issues/137273): Resolve a debug assertion failure that occurred under Windows within [`locale.setlocale()`](https://docs.python.org/3.14/library/locale.html#locale.setlocale).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
