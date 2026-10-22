# Python 3.14.4 final / core and builtins / stdtypes

[gh-145036](https://github.com/python/cpython/issues/145036): Within the free-threaded build, corrects a race condition triggered by calling `__sizeof__()` upon a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)

[gh-130555](https://github.com/python/cpython/issues/130555): Corrects a use-after-free within [`dict.clear()`](https://docs.python.org/3.14/library/stdtypes.html#dict.clear) that struck when the dictionary values sit embedded inside an object and a destructor sets off re-entrant mutation of the dictionary.

[gh-145142](https://github.com/python/cpython/issues/145142): Corrects a crash inside the free-threaded build whenever the dictionary handed to [`str.maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#str.maketrans) gets concurrently modified.

[gh-145713](https://github.com/python/cpython/issues/145713): Renders [`bytearray.resize()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.resize) thread-safe within the free-threaded build through a critical section together with the lock-held flavor of the resize routine.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
