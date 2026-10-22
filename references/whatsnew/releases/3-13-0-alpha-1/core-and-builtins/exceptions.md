# Python 3.13.0 alpha 1 / core and builtins / exceptions

[gh-109179](https://github.com/python/cpython/issues/109179): A bug was fixed in which the C traceback display loses notes attached to [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

[gh-105730](https://github.com/python/cpython/issues/105730): Accept any callable apart from type objects as the condition predicate handed to [`BaseExceptionGroup.split()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.split) and [`BaseExceptionGroup.subgroup()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.subgroup).

[gh-98931](https://github.com/python/cpython/issues/98931): Make sure custom [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) messages get raised on invalid imports that name several targets. Pablo Galindo authored this.

[gh-105800](https://github.com/python/cpython/issues/105800): Properly emit [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) inside f-strings whenever invalid sequences appear. Pablo Galindo authored this.

[gh-105331](https://github.com/python/cpython/issues/105331): Throw [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the `delay` parameter handed to [`asyncio.sleep()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.sleep) is a NaN (mirroring [`time.sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep)).

[gh-89091](https://github.com/python/cpython/issues/89091): Emit [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) for unawaited async generator methods such as [`asend()`](https://docs.python.org/3.14/reference/expressions.html#agen.asend), [`athrow()`](https://docs.python.org/3.14/reference/expressions.html#agen.athrow) and [`aclose()`](https://docs.python.org/3.14/reference/expressions.html#agen.aclose). Kumar Aditya prepared the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
