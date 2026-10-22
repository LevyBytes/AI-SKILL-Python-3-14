# Python 3.12.0 alpha 1 / library / subprocess

[gh-90473](https://github.com/python/cpython/issues/90473): [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) now bails out early on the Emscripten and WASI platforms, sidestepping the absent [`os.pipe()`](https://docs.python.org/3.14/library/os.html#os.pipe) on WASI.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
