# Python 3.14.0 alpha 1 / library / os path

[gh-124917](https://github.com/python/cpython/issues/124917): Permits keyword arguments when invoking [`os.path.exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists) and [`os.path.lexists()`](https://docs.python.org/3.14/library/os.path.html#os.path.lexists) on Windows. This repairs a regression introduced in 3.13.0.

[gh-118507](https://github.com/python/cpython/issues/118507): On Windows, [`os.path.isfile()`](https://docs.python.org/3.14/library/os.path.html#os.path.isfile) is fixed for pipes. A native implementation also makes [`os.path.isjunction()`](https://docs.python.org/3.14/library/os.path.html#os.path.isjunction) and [`os.path.lexists()`](https://docs.python.org/3.14/library/os.path.html#os.path.lexists) faster on Windows.

[gh-110863](https://github.com/python/cpython/issues/110863): With *strict* mode off (the default), [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) now silences any [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) coming out of [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink).

[gh-118263](https://github.com/python/cpython/issues/118263): A direct C call now accelerates [`os.path.splitroot()`](https://docs.python.org/3.14/library/os.path.html#os.path.splitroot) & [`os.path.normpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.normpath).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
