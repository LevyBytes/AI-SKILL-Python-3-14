# Python 3.14.0 alpha 1 / library / pty

[gh-118824](https://github.com/python/cpython/issues/118824): The deprecated `pty.master_open()` and `pty.slave_open()` are gone; reach for [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty) in their place. Nikita Sobolev wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
