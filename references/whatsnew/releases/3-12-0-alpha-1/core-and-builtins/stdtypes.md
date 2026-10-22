# Python 3.12.0 alpha 1 / core and builtins / stdtypes

[gh-91146](https://github.com/python/cpython/issues/91146): Shrink the allocation size of the [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) produced by [`str.split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split) and [`str.rsplit()`](https://docs.python.org/3.14/library/stdtypes.html#str.rsplit). Donghee Na and Inada Naoki wrote the patch.

[gh-90751](https://github.com/python/cpython/issues/90751): [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) now handles half-floats. Donghee Na and Antoine Pitrou wrote the patch.

[gh-91153](https://github.com/python/cpython/issues/91153): Resolves a case where assigning to a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) item could crash whenever the new value's `__index__()` method resizes it.

[bpo-47091](https://bugs.python.org/issue?@action=redirect&bpo=47091): Speeds up repetition of [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) by copying the data with `memcpy` and applying all the reference increments together in one step.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
