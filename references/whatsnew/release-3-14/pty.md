# What's new in Python 3.14 / pty - pty

### pty

- The `master_open()` along with `slave_open()` functions are gone; each had been deprecated as of Python 3.12. Reach for [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty) in their place. (Contributed by Nikita Sobolev in [gh-118824](https://github.com/python/cpython/issues/118824).)

[Subject index](INDEX.md) · [Previous source section](pkgutil.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md)
