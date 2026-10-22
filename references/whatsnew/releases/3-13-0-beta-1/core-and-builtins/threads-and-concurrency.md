# Python 3.13.0 beta 1 / core and builtins / threads and concurrency

[gh-116322](https://github.com/python/cpython/issues/116322): Within `--disable-gil` builds, the GIL stays enabled during the loading of C extension modules. Should a module signal that it tolerates running GIL-free, the GIL switches off once loading wraps up. Otherwise it stays on for the rest of the interpreter's life. None of this applies once the GIL has been explicitly turned on or off through `PYTHON_GIL` or `-Xgil`.

[gh-117514](https://github.com/python/cpython/issues/117514): Introduce a `sys._is_gil_enabled()` function reporting whether the GIL is presently active. Within the default build it returns `True` every time, since the GIL is forever active. In the free-threaded build the answer can be either `True` or `False`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
