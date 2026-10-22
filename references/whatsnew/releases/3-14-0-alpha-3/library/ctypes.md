# Python 3.14.0 alpha 3 / library / ctypes

[gh-127870](https://github.com/python/cpython/issues/127870): Spot recursive invocations during ctypes `_as_parameter_` processing. Victor Stinner supplied the patch.

[gh-127255](https://github.com/python/cpython/issues/127255): The [`CopyComPointer()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CopyComPointer) function has been made public. It used to be private and reachable only through `_ctypes`.

[gh-126615](https://github.com/python/cpython/issues/126615): The [`COMError`](https://docs.python.org/3.14/library/ctypes.html#ctypes.COMError) exception has been made public. It used to be private and reachable only through `_ctypes`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
