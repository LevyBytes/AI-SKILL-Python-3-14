# Python 3.13.0 alpha 6 / library / exceptions

[gh-114848](https://github.com/python/cpython/issues/114848): Throw [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) once `getcwd()` hands back ?(unreachable)?, a situation possible on Linux >= 2.6.36 paired with glibc < 2.27.

[gh-117459](https://github.com/python/cpython/issues/117459): `asyncio.asyncio.run_coroutine_threadsafe()` now retains the traceback for `CancelledError`, [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError), and `InvalidStateError` whenever the coroutine raises them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
