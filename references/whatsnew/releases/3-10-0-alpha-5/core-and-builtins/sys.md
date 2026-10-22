# Python 3.10.0 alpha 5 / core and builtins / sys

[bpo-38631](https://bugs.python.org/issue?@action=redirect&bpo=38631): Swap out the compiler's [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) calls for ordinary [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) exceptions. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
