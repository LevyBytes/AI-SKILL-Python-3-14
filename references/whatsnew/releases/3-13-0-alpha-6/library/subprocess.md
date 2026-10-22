# Python 3.13.0 alpha 6 / library / subprocess

[gh-90872](https://github.com/python/cpython/issues/90872): Under Windows, [`subprocess.Popen.wait()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.wait) no longer hands `WaitForSingleObject()` a negative timeout: a negative timeout now passes `0` ms instead. Victor Stinner contributed the patch.

[gh-98966](https://github.com/python/cpython/issues/98966): Inside [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess), surface a more helpful message whenever `stdout=STDOUT`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
