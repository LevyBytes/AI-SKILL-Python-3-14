# Python 3.14.0 beta 4 / library / exceptions

[gh-135836](https://github.com/python/cpython/issues/135836): An [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) inside [`asyncio.loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) was fixed; it could arise when a non-[`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is thrown during connection and the socket’s `close()` throws `OSError`.

[gh-135836](https://github.com/python/cpython/issues/135836): An [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) inside [`asyncio.loop.create_connection()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_connection) was fixed; it could arise when the Happy Eyeballs algorithm left an empty exceptions list during connection attempts.

[gh-135855](https://github.com/python/cpython/issues/135855): A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is now raised rather than a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) whenever `_interpreters.set___main___attrs()` receives an object that is not a dict. Brian Schubert authored this patch.

[gh-135646](https://github.com/python/cpython/issues/135646): Consistent [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exceptions are now raised within [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
