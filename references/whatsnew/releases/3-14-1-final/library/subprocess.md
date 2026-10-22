# Python 3.14.1 final / library / subprocess

[gh-141473](https://github.com/python/cpython/issues/141473): A second invocation of [`subprocess.Popen.communicate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.communicate) ? after the first one passed *input* plus a *timeout* and raised [`TimeoutExpired`](https://docs.python.org/3.14/library/subprocess.html#subprocess.TimeoutExpired) while the child was still alive ? will now avoid hanging.

[gh-134453](https://github.com/python/cpython/issues/134453): Corrected how [`subprocess.Popen.communicate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.communicate) treats its `input=` argument for [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects shaped as non-bytes under POSIX. Such views now get correctly recast into a byte shaped view rather than the input being cut short. The defect never affected Windows.

[gh-74389](https://github.com/python/cpython/issues/74389): Should the stdin used by a [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) instance already be closed, [`subprocess.Popen.communicate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.communicate) now disregards that instead of leaving the class in an inconsistent state.

[gh-87512](https://github.com/python/cpython/issues/87512): Correct [`subprocess.Popen.communicate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.communicate) timeout handling on Windows while large input is written. Earlier the timeout went unheeded during the stdin write, so the method could block forever when the child process drained input slowly. That stdin write now happens on a background thread, which lets the timeout be enforced as intended.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
