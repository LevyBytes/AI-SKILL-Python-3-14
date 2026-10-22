# Python 3.14.1 final / library / ctypes

[gh-138008](https://github.com/python/cpython/issues/138008): Corrects segmentation faults within the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module brought on by invalid [`argtypes`](https://docs.python.org/3.14/library/ctypes.html#ctypes._CFuncPtr.argtypes). Dung Nguyen authored the patch.

[gh-140041](https://github.com/python/cpython/issues/140041): Corrects importing [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) on Android and Cygwin whenever ABI flags are in play.

[gh-83424](https://github.com/python/cpython/issues/83424): Permits building a [`ctypes.CDLL`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CDLL) with no name once a handle is supplied as the argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
