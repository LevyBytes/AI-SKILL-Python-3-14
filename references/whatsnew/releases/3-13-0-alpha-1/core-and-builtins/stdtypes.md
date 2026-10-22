# Python 3.13.0 alpha 1 / core and builtins / stdtypes

[gh-106487](https://github.com/python/cpython/issues/106487): Permit the *count* parameter of [`str.replace()`](https://docs.python.org/3.14/library/stdtypes.html#str.replace) to be passed by keyword. Hugo van Kemenade prepared the patch.

[gh-96844](https://github.com/python/cpython/issues/96844): Sharpen the error text produced by [`list.remove()`](https://docs.python.org/3.14/library/stdtypes.html#list.remove). Donghee Na supplied the patch.

[gh-110688](https://github.com/python/cpython/issues/110688): The undocumented `test_c_api` method was dropped from [`set`](https://docs.python.org/3.14/library/stdtypes.html#set); it had existed solely for testing under `Py_DEBUG`. Proper CAPI tests now exist instead.

[gh-107596](https://github.com/python/cpython/issues/107596): Subscripting [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects with [`int`](https://docs.python.org/3.14/library/functions.html#int) indexes is now specialized.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
