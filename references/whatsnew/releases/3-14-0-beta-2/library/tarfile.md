# Python 3.14.0 beta 2 / library / tarfile

[gh-133890](https://github.com/python/cpython/issues/133890): The [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module now treats [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) just like [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) whenever a member cannot be extracted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
