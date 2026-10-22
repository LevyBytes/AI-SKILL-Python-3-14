# Python 3.14.3 final / library / sys

[gh-143547](https://github.com/python/cpython/issues/143547): [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) is fixed for the case where the hook itself raises an exception and replaces `sys.unraisablehook()`: a strong reference to the prior hook is now retained. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
