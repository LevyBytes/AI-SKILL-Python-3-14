# Python 3.12.0 alpha 6 / c api / exceptions

[gh-101578](https://github.com/python/cpython/issues/101578): Introduce [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) plus [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) so the active exception can be stored and reinstated. Each of these works with one exception object instead of the three-argument form used by the now-deprecated [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch) and [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore). That cuts down on mistakes and runs slightly faster.

Also adds [`PyException_GetArgs()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyException_GetArgs) and [`PyException_SetArgs()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyException_SetArgs) as helpers for reading and changing the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) handed to the exception’s constructor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
