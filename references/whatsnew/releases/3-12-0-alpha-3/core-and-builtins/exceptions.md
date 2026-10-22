# Python 3.12.0 alpha 3 / core and builtins / exceptions

[bpo-31718](https://bugs.python.org/issue?@action=redirect&bpo=31718): Throw [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) once methods on uninitialized [`io.IncrementalNewlineDecoder`](https://docs.python.org/3.14/library/io.html#io.IncrementalNewlineDecoder) objects get invoked. Oren Milman contributed the patch.

[gh-99553](https://github.com/python/cpython/issues/99553): Resolve a defect where an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) subclass could wrap a [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
