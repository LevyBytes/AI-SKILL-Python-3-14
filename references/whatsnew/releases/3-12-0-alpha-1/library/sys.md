# Python 3.12.0 alpha 1 / library / sys

[gh-98257](https://github.com/python/cpython/issues/98257): Makes the [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) and [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) functions reentrant. They no longer fail with: `RuntimeError("Cannot install a trace function while another trace function is being installed")`. Victor Stinner wrote the patch.

[gh-94510](https://github.com/python/cpython/issues/94510): Re-entrant invocations of [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) along with [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) now throw [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
